import uvicorn

from app.core.config import settings


def main():
    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_DEBUG,
    )
    print("Application server started.")


if __name__ == "__main__":
    main()
