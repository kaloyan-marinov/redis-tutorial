import redis

from initial_data import hats


if __name__ == '__main__':
    r = redis.Redis(
        host='localhost',
        port=6379,
        db=1,
    )
    
    # The concept of Redis "pipelining" is a way to decrease the # of
    # round-trip transactions that are needed to write data to and read data
    # from the targeted Redis server.
    #
    # With a pipeline, all the commands are buffered on the client side
    # and then sent across [to the server] at once.
    with r.pipeline() as pipe:
        for h_id, hat in hats.items():
            pipe.hmset(h_id, hat)
        pipe.execute()

    
    # Manually tell the Redis server to save its data to disk.
    # (The parent process uses the `fork()` system call to pass off
    # the time-intensive write to disk to a child process, so the parent
    # process can continue on its way. This is what the "bg"/"background"
    # refers to.)
    #r.bgsave()
