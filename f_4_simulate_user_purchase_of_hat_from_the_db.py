import redis


if __name__ == '__main__':
    r = redis.Redis(
        host='localhost',
        port=6379,
        db=1,
    )

    r.hincrby(
        "hat:56854717",
        "quantity",
        -1,
    )
    r.hincrby(
        "hat:56854717",
        "npurchased",
        1,
    )
