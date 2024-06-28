from datetime import datetime
from typing import Annotated
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import Field, HttpUrl


class URLModel(Document):
    id: Annotated[UUID, Field(default_factory=uuid4)]

    url: HttpUrl

    short_url: Annotated[
        HttpUrl,
        Indexed(
            unique=True,
        ),
    ]

    created_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]

    class Settings:
        name = "urls"
