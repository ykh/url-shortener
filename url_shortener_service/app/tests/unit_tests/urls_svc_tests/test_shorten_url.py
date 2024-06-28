import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

from pydantic import HttpUrl

from exceptions import http_exceptions
from services.urls.urls_svc import URLsSVC
from services.urls.validators.shorten_vld import ShortenURLSVCVLD


class TestURLsSVC(unittest.IsolatedAsyncioTestCase):
    @patch("settings.zookeeper.ZooKeeper.get_next_counter")
    async def test_shorten_url_success(
            self,
            mock_zk_get_next_counter: MagicMock,
    ):
        input_params = SimpleNamespace()
        input_params.url = HttpUrl("https://to_be_short.long")

        expected = SimpleNamespace()
        expected.short_url = HttpUrl(
            "https://sh.rt/b9",
        )  # Base62 of 123 is "b9"
        expected.url = input_params.url

        mock_values = SimpleNamespace()
        mock_values.zk_get_next_counter = 123

        mock_values.urls_repo_create_url = SimpleNamespace()
        mock_values.urls_repo_create_url.url = HttpUrl(
            "https://to_be_short.long",
        )
        mock_values.urls_repo_create_url.short_url = HttpUrl(
            "https://sh.rt/b9",
        )

        mock_redis_client = MagicMock()
        mock_urls_repo = AsyncMock()

        mock_zk_get_next_counter.return_value = mock_values.zk_get_next_counter

        mock_urls_repo.create_url.return_value = mock_values.urls_repo_create_url

        urls_svc = URLsSVC(
            url_repo=mock_urls_repo,
            redis_client=mock_redis_client,
        )

        result = await urls_svc.shorten_url(
            ShortenURLSVCVLD(url=input_params.url),
        )

        self.assertEqual(result["url"], expected.url)
        self.assertEqual(result["short_url"], expected.short_url)

    @patch("settings.zookeeper.ZooKeeper.get_next_counter")
    async def test_zookeeper_get_next_counter_error(
            self,
            mock_zk_get_next_counter: MagicMock,
    ):
        input_params = SimpleNamespace()
        input_params.url = HttpUrl("https://to_be_short.long")

        mock_zk_get_next_counter.side_effect = Exception("ZooKeeper is down!")

        mock_redis_client = MagicMock()
        mock_urls_repo = AsyncMock()

        urls_svc = URLsSVC(
            url_repo=mock_urls_repo,
            redis_client=mock_redis_client,
        )

        with self.assertRaises(
                http_exceptions.InternalServerError500Exception,
        ):
            await urls_svc.shorten_url(
                ShortenURLSVCVLD(url=input_params.url),
            )


if __name__ == "__main__":
    unittest.main()
