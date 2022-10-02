from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.config import settings
from api.v1.api import v1_router
from api.v1.error.base_error import BaseError


app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")
app.include_router(router=v1_router, prefix=settings.API_V1_STR)


@app.exception_handler(BaseError)
async def unicorn_exception_handler(request: Request, exc: BaseError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")