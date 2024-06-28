from pydantic import BaseModel, HttpUrl


class ShortenURLAPIVLD(BaseModel):
    url: HttpUrl
