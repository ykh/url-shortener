from pydantic import BaseModel, HttpUrl


class ShortenURLSVCVLD(BaseModel):
    url: HttpUrl
