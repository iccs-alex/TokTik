import redis
import config
from json import loads
from convert import convert_to_mp4
from s3 import getVideo, putVideo
import io

def redis_db():
    redisDB = redis.Redis(host=config.REDIS_HOST,
                          port=config.REDIS_PORT,
                          db=config.REDIS_DB_NUM,
                          decode_responses=True
                          )
    return redisDB


def redis_queue_push(redisDB, message):
    redisDB.lpush(config.REDIS_QUEUE_NAME, message)


def redis_queue_pop(redisDB):
    _, message_json = redisDB.brpop(config.REDIS_QUEUE_NAME)
    return message_json


def process_message(redisDB, message_json: str):
    message = loads(message_json)
    print(f"Message received: id={message['id']}, message={message}.")


def main():
    redisDB = redis_db()
    pubsub = redisDB.pubsub()
    pubsub.subscribe("convert")
    messages = []
    for message in pubsub.listen():
        channel = message['channel']
        data = message['data']
        if type(data) is not str:
            print("Invalid data type: " + str(type(data)))
            continue
        messages.append(message)
        print("Message data: " + str(data))
        videoFile = getVideo(data)
        videoBytes = videoFile["Body"].read()

        videoMp4 = convert_to_mp4(videoBytes)
        putVideo("test", videoMp4)


if __name__ == "__main__":
    main()
