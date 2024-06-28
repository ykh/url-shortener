import os
from string import ascii_letters, digits
from typing import Annotated

from fastapi import Depends
from pydantic import HttpUrl

from exceptions import http_exceptions
from repositories.url_repo import URLRepo
from repositories.validators.url_vld import CreateURLREPVLD
from services.urls.validators.shorten_vld import ShortenURLSVCVLD
from settings.redis import Redis
from settings.zookeeper import ZooKeeper


class URLsSVC:
    def __init__(
            self,
            url_repo: Annotated[URLRepo, Depends(URLRepo)],
            redis_client=Depends(Redis.get_redis),
    ):
        self.url_repo = url_repo
        self.redis_client = redis_client

    @staticmethod
    def generate_short_url(num: int) -> str:
        characters = ascii_letters + digits
        base = len(characters)

        if not isinstance(num, int):
            raise TypeError("Input must be an integer.")
        if num < 0:
            raise ValueError("Input number cannot be negative.")

        if num == 0:
            return characters[0]

        short_url = ""

        while num > 0:
            remainder = num % base
            short_url = characters[remainder] + short_url
            num = num // base

        return short_url

    async def shorten_url(self, params: ShortenURLSVCVLD):
        try:
            counter_number = ZooKeeper.get_next_counter()
        except Exception as error:
            # raise error
            raise http_exceptions.InternalServerError500Exception(
                detail="Getting counter number failed."
            )

        # Generate a unique string for short URL.
        string = self.generate_short_url(counter_number)

        short_url = f"{os.getenv('SHORT_URL_ADDRESS')}/{string}"

        try:
            url = await self.url_repo.create_url(
                CreateURLREPVLD(
                    url=params.url,
                    short_url=short_url,
                )
            )
        except Exception as error:
            # raise error
            raise http_exceptions.InternalServerError500Exception(
                detail="Create URL has been failed."
            )

        return {
            "url": url.url,
            "short_url": url.short_url,
        }

    async def get_url(self, url: HttpUrl):
        original_url = await self.redis_client.get(str(url))

        if not original_url:
            url_doc = await self.url_repo.get_url_by_short_url(url)
            original_url = url_doc.url

            if url_doc is None:
                raise http_exceptions.NotFound404Exception(
                    detail="URL not found."
                )

            await self.redis_client.set(
                str(url_doc.short_url),
                str(url_doc.url),
            )

        # return RedirectResponse(url=url_doc.url)
        return {
            "url": original_url,
            "short_url": url,
        }
