from typing import Annotated

from fastapi import APIRouter, Depends, Query
from pydantic import HttpUrl

from routers.validators.shorten_url_vld import ShortenURLAPIVLD
from services.urls.urls_svc import URLsSVC
from services.urls.validators.shorten_vld import ShortenURLSVCVLD

router = APIRouter(prefix="/api")


@router.post("/shorten", tags=["URLs"])
async def shorten_url(
        request: ShortenURLAPIVLD,
        urls_svc: Annotated[URLsSVC, Depends(URLsSVC)],
):
    result = await urls_svc.shorten_url(
        ShortenURLSVCVLD(
            url=request.url
        )
    )

    return result


@router.get("/redirect", tags=["URLs"])
async def get_url(
        urls_svc: Annotated[URLsSVC, Depends(URLsSVC)],
        url: HttpUrl = Query(),
):
    result = await urls_svc.get_url(url=url)

    return result
