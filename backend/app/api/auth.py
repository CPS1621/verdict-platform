from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.security.security import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Demo credentials
USERNAME = "admin"
PASSWORD = "admin123"


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Authenticate user and return JWT token.
    """

    if (
        form_data.username != USERNAME
        or form_data.password != PASSWORD
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": form_data.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }