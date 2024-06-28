from pydantic import HttpUrl

from models.url_mdl import URLModel
from repositories.validators.url_vld import CreateURLREPVLD


class URLRepo:
    @staticmethod
    async def create_url(params: CreateURLREPVLD):
        url_doc = URLModel(
            url=params.url,
            short_url=params.short_url,
        )

        try:
            await url_doc.create()
        except Exception as error:
            raise error

        return url_doc

    @staticmethod
    async def get_url_by_short_url(short_url: HttpUrl):
        url_doc = await URLModel.find_one(URLModel.short_url == str(short_url))

        return url_doc
