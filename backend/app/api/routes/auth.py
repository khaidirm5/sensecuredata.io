from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import (
    get_current_user,
    oauth2_scheme,
    require_roles,
)
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import (
    LogoutResponse,
    RefreshTokenRequest,
    Token,
    TokenPair,
    UserCreate,
    UserResponse,
)
from app.services.auth import logout
from app.services.user import (
    authenticate_user,
    refresh_access_token,
    register_user,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
) -> UserResponse:
    """Register a new user."""

    try:
        return register_user(db, user)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.post(
    "/login",
    response_model=TokenPair,
    status_code=status.HTTP_200_OK,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> TokenPair:
    """Authenticate a user."""

    try:
        return authenticate_user(
            db=db,
            email=form_data.username,
            password=form_data.password,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc


@router.post(
    "/refresh",
    response_model=Token,
    status_code=status.HTTP_200_OK,
)
def refresh(
    request: RefreshTokenRequest,
) -> Token:
    """Generate a new access token using a refresh token."""

    try:
        return refresh_access_token(
            request.refresh_token,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc


@router.post(
    "/logout",
    response_model=LogoutResponse,
    status_code=status.HTTP_200_OK,
)
def logout_user(
    current_user: User = Depends(get_current_user),
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> LogoutResponse:
    """Log out the authenticated user."""

    logout(
        db=db,
        token=token,
    )

    return LogoutResponse(
        message="Logout successful.",
    )


@router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def get_me(
    current_user: User = Depends(get_current_user),
) -> UserResponse:
    """Return the currently authenticated user."""

    return current_user


@router.get(
    "/check-role",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def check_role(
    current_user: User = Depends(
        require_roles(
            "admin",
            "analyst",
            "user",
        ),
    ),
) -> UserResponse:
    """Validate the authenticated user's role."""

    return current_user
