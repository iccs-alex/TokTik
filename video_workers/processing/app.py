import redis
import config
from json import loads
from process import process_mp4
import s3
import os

def redis_db():
    redisDB = redis.Redis(host=config.REDIS_HOST,
                          port=config.REDIS_PORT,
                          db=config.REDIS_DB_NUM,
                          decode_responses=True
                          )
    return redisDB


def redis_queue_pop(redisDB):
    _, message_json = redisDB.brpop(config.REDIS_QUEUE_NAME)
    return message_json


def process_message(redisDB, message_json: str):
    message = loads(message_json)
    print(f"Message received: id={message['id']}, message={message}.")


def main():
    redisDB = redis_db()
    pubsub = redisDB.pubsub()
    pubsub.subscribe(config.REDIS_LISTEN_QUEUE_NAME)
    messages = []
    for message in pubsub.listen():
        channel = message['channel']
        data = message['data']
        if type(data) is not str:
            print("Invalid data type: " + str(type(data)))
            continue
        messages.append(message)
        print("Message data: " + str(data))
        videoFile = s3.getVideo(data)
        videoBytes = videoFile["Body"].read()
        (videoChunks, output_folder) = process_mp4(videoBytes, 10)
        print("Processed video")
        # Upload chunks and linker file to S3
        for filename in videoChunks:
            chunkPath = os.path.join(output_folder, filename)
            chunkKey = os.path.join(data, filename)
            s3.putVideo('chunked_videos'+chunkKey, chunkPath)

        linker_file = os.path.join(output_folder, "linker.txt")
        linker_key = os.path.join(data, "linker.txt")
        s3.putVideo('chunked_videos'+linker_key, linker_file)

        redisDB.publish(config.REDIS_PUSH_QUEUE_NAME, data)
        print("Message processed")


if __name__ == "__main__":
    main()
