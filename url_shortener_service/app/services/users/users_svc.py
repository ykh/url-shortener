import os
from datetime import datetime, timedelta
from typing import Optional

import jwt


class UsersSVC:
    algorithm = os.getenv("JWT_ALGORITHM")
    secret_key = os.getenv("JWT_SECRET_KEY")
    access_token_expire_minutes = int(os.getenv("JWT_EXPIRE_MINUTES"))

    def create_access_token(
            self,
            data: dict,
            expires_delta: Optional[timedelta] = None
    ):
        _data = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=self.access_token_expire_minutes,
            )

        _data.update({"exp": expire})

        encoded_jwt = jwt.encode(
            _data,
            self.secret_key,
            algorithm=self.algorithm,
        )

        return encoded_jwt
