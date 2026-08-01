from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Sentinel Secure Data Intelligence Platform API",
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/")
def root():
    """Health check endpoint."""

    return {
        "message": "Welcome to Sentinel Secure Data Intelligence Platform API",
    }
