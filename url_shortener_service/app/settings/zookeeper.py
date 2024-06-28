import os

from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock


class ZooKeeper:
    client = None
    base_path = "url"
    range_counter_path = f"{base_path}/range_counter"
    counter_path = None
    range_size = int(os.getenv("COUNTER_RANGE_SIZE"))
    start_range = None
    end_range = None

    @classmethod
    def get_next_counter(cls):
        with cls.client.transaction() as ct:
            current_value = int(
                cls.client.get(ZooKeeper.counter_path)[0].decode(),
            )

            new_value = current_value + 1

            if new_value >= ZooKeeper.end_range:
                ZooKeeper.get_new_range()

                current_value = int(
                    cls.client.get(ZooKeeper.counter_path)[0].decode(),
                )

                new_value = current_value
            else:
                ct.set_data(ZooKeeper.counter_path, str(new_value).encode())

        return new_value

    @classmethod
    def get_new_range(cls):
        if cls.client is None:
            raise ValueError("ZooKeeper client is not initialized.")

        lock = Lock(cls.client, cls.range_counter_path)

        with lock:
            last_range_counter, stat = cls.client.get(cls.range_counter_path)
            last_range_counter = int(last_range_counter.decode('utf-8'))

            cls.start_range = last_range_counter * cls.range_size
            cls.end_range = cls.start_range + cls.range_size

            cls.client.set(
                cls.range_counter_path,
                str(last_range_counter + 1).encode("utf-8"),
            )

            cls.counter_path = f"{cls.base_path}/c{last_range_counter + 1}"

            if not cls.client.exists(cls.counter_path):
                cls.client.create(
                    cls.counter_path,
                    value=f"{cls.start_range}".encode("utf-8"),
                )

    @classmethod
    def init(cls):
        auth = {
            "username": os.getenv('ZOOKEEPER_AUTH_USERNAME'),
            "password": os.getenv('ZOOKEEPER_AUTH_PASSWORD'),
        }

        cls.client = KazooClient(
            hosts=os.getenv("ZOOKEEPER_ADDRESS"),
            auth_data=[
                (
                    "digest",
                    f"{auth['username']}:{auth['password']}"
                )
            ],
        )

        cls.client.start()

        cls.client.ensure_path(cls.base_path)

        if not cls.client.exists(cls.range_counter_path):
            cls.client.create(cls.range_counter_path, b'0')

        cls.get_new_range()

        return cls.client


ZooKeeper.init()
