from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.exception_handler import register_exception_handlers

app = FastAPI(
    title="Sentinel Secure Data Intelligence Platform API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_exception_handlers(app)


app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    """Health check endpoint."""

    return {
        "message": "Welcome to Sentinel Secure Data Intelligence Platform API",
    }
