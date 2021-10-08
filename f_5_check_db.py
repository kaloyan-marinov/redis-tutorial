import redis


if __name__ == '__main__':
    r = redis.Redis(
        host='localhost',
        port=6379,
        db=1,
    )

    a = r.hgetall('hat:56854717')

    print(a)