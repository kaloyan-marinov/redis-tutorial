# how to set up the project

```
$ python3 --version
3.8.3

$ python3 -m venv venv
$ source venv/bin/activate

(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt

$ docker --version
Docker version 20.10.5, build 55c4c88
```

# how to use the project

create a Docker network:
```
$ docker network create network-redis-tutorial
```

start a Redis instance:
```
$ docker run \
    --network network-redis-tutorial \
    --name container-redis-server \
    --publish 6379:6379 \
    redis:6.2.6-alpine
```

connect via the Redis CLI:
```
$ docker run \
    --network network-redis-tutorial \
    -it \
    --rm \
    redis:6.2.6-alpine \
    redis-cli \
        -h container-redis-server \
        -n 1
```

run the Python scripts in the following order:
```
(venv) $ python f_2_write_initial_data.py

(venv) $ python f_3_check_contents_of_the_redis_db.py

(venv) $ python f_4_simulate_user_purchase_of_hat_from_the_db.py

(venv) $ python f_5_check_db.py
```

# finally, clean up the Docker entities

```
$ docker container rm -f $(docker container ls -aq)

$ docker network rm network-redis-tutorial
```

