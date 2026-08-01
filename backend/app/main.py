from fastapi import FastAPI

app = FastAPI(title="Sentinel Secure Data Intelligence Platform API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to Sentinel Secure Data Intelligence Platform API"}
