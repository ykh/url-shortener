import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.url_mdl import URLModel


class DB:
    def __init__(self, is_test: bool = False):
        prefix = "TEST_" if is_test else ""

        self.host = os.getenv(f"{prefix}DB_HOST")
        self.port = os.getenv(f"{prefix}DB_PORT")
        self.username = os.getenv(f"{prefix}DB_USERNAME")
        self.password = os.getenv(f"{prefix}DB_PASSWORD")
        self.db_name = os.getenv(f"{prefix}DB_NAME")

        self.uri = (
            f"mongodb://{self.username}:{self.password}"
            f"@{self.host}:{self.port}/{self.db_name}"
        )

        self.client = None
        self.db = None

    async def init(self):
        self.client = AsyncIOMotorClient(
            self.uri,
            uuidRepresentation='standard',
        )

        self.db = self.client.get_database(self.db_name)

        await init_beanie(
            database=self.db,
            document_models=[
                URLModel,
            ]
        )

    async def drop_collection(self, collection: str):
        if self.client is None:
            raise ValueError("DB client has not initialized yet. Call init().")

        await self.db[collection].drop()
