from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas.error import ErrorResponse


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        return JSONResponse(
            status_code=422,
            content=ErrorResponse(
                message="Validation failed.",
                error=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(
        request: Request,
        exc: ValueError,
    ):
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(
                message="Request failed.",
                error=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(
        request: Request,
        exc: Exception,
    ):
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                message="Internal server error.",
                error="Unexpected server error.",
            ).model_dump(),
        )
