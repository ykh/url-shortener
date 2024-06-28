import os
from http import HTTPStatus

import jwt
from fastapi.responses import JSONResponse
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response


class AuthMDW(BaseHTTPMiddleware):
    @staticmethod
    def decode_access_token(token: str):
        try:
            payload = jwt.decode(
                token,
                os.getenv("JWT_SECRET_KEY"),
                algorithms=[os.getenv("JWT_ALGORITHM")],
            )

            return payload
        except jwt.PyJWTError:
            return None

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint,
    ) -> Response:
        if request.url.path in ["/api/users/token", ]:
            response = await call_next(request)

            return response

        token: str = request.headers.get("Authorization")

        if token:
            try:
                payload = self.decode_access_token(token)

                if payload is None:
                    return JSONResponse(
                        content={
                            "error": "Invalid token or expired token."
                        },
                        status_code=HTTPStatus.UNAUTHORIZED,
                    )

                request.state.user = payload
            except ValueError:
                return JSONResponse(
                    content={
                        "error": "Invalid authorization header."
                    },
                    status_code=HTTPStatus.UNAUTHORIZED,
                )
        else:
            return JSONResponse(
                content={
                    "error": "Not authorized."
                },
                status_code=HTTPStatus.UNAUTHORIZED,
            )

        response = await call_next(request)

        return response
