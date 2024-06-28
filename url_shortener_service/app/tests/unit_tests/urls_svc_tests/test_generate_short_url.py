import unittest
from unittest.mock import MagicMock

from fastapi import Depends

from services.urls.urls_svc import URLsSVC


class TestGenerateShortURL(unittest.TestCase):
    def setUp(self):
        self.mock_url_repo = MagicMock()
        self.mock_redis_client = MagicMock()

        self.urls_svc = URLsSVC(
            url_repo=self.mock_url_repo,
            redis_client=self.mock_redis_client,
        )

    def test_generate_short_url_basic(self):
        self.assertEqual(self.urls_svc.generate_short_url(0), 'a')
        self.assertEqual(self.urls_svc.generate_short_url(1), 'b')
        self.assertEqual(self.urls_svc.generate_short_url(61), '9')
        self.assertEqual(self.urls_svc.generate_short_url(62), 'ba')
        self.assertEqual(self.urls_svc.generate_short_url(123), 'b9')

    def test_generate_short_url_invalid_type(self):
        with self.assertRaises(TypeError):
            self.urls_svc.generate_short_url("100")

    def test_generate_short_url_negative_number(self):
        with self.assertRaises(ValueError):
            self.urls_svc.generate_short_url(-1)


if __name__ == '__main__':
    unittest.main()
