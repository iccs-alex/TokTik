import redis
import config
from json import loads


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
    print("ADASDASDASDASDASD")
    _, message_json = redisDB.brpop(config.REDIS_QUEUE_NAME)
    return message_json


def process_message(redisDB, message_json: str):
    message = loads(message_json)
    print(f"Message received: id={message['id']}, message={message}.")


try:
    redisDB = redis_db()
    pubsub = redisDB.pubsub()
    pubsub.subscribe("convert")
    messages = []
    for message in pubsub.listen():
        messages.append(message)
        channel = message['channel']
        data = message['data']
        print("Message data: " + str(data))
except Exception as e:
    print(f"An error occured: {e}")
