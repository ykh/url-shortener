# URL Shortener Project

## How to Run The Project

### Step 1: Run ZooKeeper Service

```shell
cd to/counter_service/directory

# OPTIONAL: Take a look on the ZooKeeper config file at `configs/zoo.cfg` for any desire changes.
vim ./configs/zoo.cfg

# To build docker image and up a container:
make up
# in case for detached mode, run following:
make up-detached

# For more information and examples:
make help
```

### Step 2: Run App

```shell
cd to/url_shortner_service/directory

# Create env files using their templates.
cp ./envs/app.env.example ./envs/app.env
cp ./envs/app_db.env.example ./envs/app_db.env
cp ./envs/redis.env.example ./envs/redis.env
cp ./env.example ./.env

# Adjust env variables with appropriate values.
vim ./envs/app.env
vim ./envs/app_db.env
vim ./envs/redis.env
vim ./.env

# To build docker image and up a container:
make build-up
# in case for detached mode, run following:
make build-up-detached

# For more information and examples:
make help
```

## How to Run Unit and Integration Tests

```bash
cd to/url_shortner_service/directory

# To run unit tests:
make tests-unit

# To run integration tests:
make tests-integration

# For more information and examples:
make help
```

## How to Run Load-Tests, Using Locust in Multiple Machines Mode

```shell
cd to/load_test_service/directory

# Create env files using their templates.
cp ./envs/locust.env.example ./envs/locust.env
cp ./env.example ./.env

# Adjust env variables with appropriate values.
vim ./envs/locust.env
vim ./.env

# Build and up Locust master container.
make build-up-master

# Build, up and scale Locust worker containers with 5 instances.
make build-up-scale-workers scale=5

# Now, you can see the Locust web interface for running the tests on `LOCUST_EXPOSED_PORT` port number.
# e.g http://127.0.0.1:7357/

# For more information and examples:
make help
```

## Documents

- [Architecture](https://miro.com/app/board/uXjVKACD9EA=/?moveToWidget=3458764591002584020&cot=14)
- [Estimations Doc](https://docs.google.com/spreadsheets/d/1NlhiovBjk0BgpbUxUV8Ku2w3fl3gbwFw5Cth-t5_viw/edit#gid=0)
- [Requests Flow Diagram](https://miro.com/app/board/uXjVKACD9EA=/?moveToWidget=3458764591002584020&cot=14)
- [Load-Tests Report](https://miro.com/app/board/uXjVKACD9EA=/?moveToWidget=3458764591634823490&cot=10)
- [Project Management Board](https://trello.com/b/Gv3WS2Qn/url-shortener-project)
- [Local API URL](http://127.0.0.1:8000/)
- [Local API Doc](http://127.0.0.1:8000/docs#)
