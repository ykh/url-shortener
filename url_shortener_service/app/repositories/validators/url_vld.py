from pydantic import BaseModel, HttpUrl


class CreateURLREPVLD(BaseModel):
    url: HttpUrl
    short_url: HttpUrl
