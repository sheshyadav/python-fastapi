from fastapi import FastAPI
from app.core.config import settings

# Setup the root application.
app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)


@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}
