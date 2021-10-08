f_3_check_contents_of_the_redis_db.py

"""
This script is a Python counterpart to doing the following in the Redis CLI:

```
$ redis-cli -n 1
127.0.0.1:6379[1]> HGETALL hat:56854717
1) "color"
2) "green"
3) "price"
4) "99.99"
5) "style"
6) "baseball"
7) "quantity"
8) "200"
9) "npurchased"
10) "0"

127.0.0.1:6379[1]> KEYS '*'
1) "hat:1326692461"
2) "hat:56854717"
3) "hat:1236154736"
```
"""
import redis


if __name__ == '__main__':
    r = redis.Redis(
        host='localhost',
        port=6379,
        db=1,
    )

    a = r.hgetall('hat:56854717')
    print(a)

    b = r.keys()  # time complexity: O(n), n := # of entries in the Redis DB
    print(b)
