import os
from os import getenv

import uvicorn
from fastapi import FastAPI

from middlewares.auth_mdw import AuthMDW
from routers import urls_routes, users_routes
from settings.db import DB


def create_app(debug=False) -> FastAPI:
    return FastAPI(debug=debug)


app = create_app(True if getenv("DEBUG") == "true" else False)

app.add_middleware(AuthMDW)


@app.on_event("startup")
async def startup_app_event():
    app.include_router(urls_routes.router)
    app.include_router(users_routes.router)

    if os.getenv("IS_TEST") == "true":
        print("##########################################")
        print("##### App Is Running in Test Mode.")
        print("##########################################")
        await DB(is_test=True).init()
    else:
        await DB(is_test=False).init()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=getenv("APP_HOST"),
        port=int(getenv("APP_PORT")),
        reload=True,
    )
