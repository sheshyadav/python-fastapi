from fastapi import FastAPI

# Setup the root application.
app = FastAPI(title="Chat Application API", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}
