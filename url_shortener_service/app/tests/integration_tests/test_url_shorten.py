import unittest

from settings.db import DB


class TestURLShorten(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Reset DB.
        db = DB(is_test=True)
        await db.init()
        await db.drop_collection("urls")

        # todo: Reset ZooKeeper paths value.
