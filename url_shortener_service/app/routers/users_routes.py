from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.users.users_svc import UsersSVC

router = APIRouter(prefix="/api/users")


# Routes
@router.post("/token")
async def login(
        users_svc: Annotated[UsersSVC, Depends(UsersSVC)],
        form_data: OAuth2PasswordRequestForm = Depends(),
):
    # It's a mock user, and always returns a valid token.
    # It's just for bringing an authentication functionality to this project.
    user = {
        "username": form_data.username,
        "full_name": form_data.username.upper(),
    }

    access_token = users_svc.create_access_token(
        data={
            "username": user.get("username")
        },
    )

    return {
        "access_token": access_token,
    }
