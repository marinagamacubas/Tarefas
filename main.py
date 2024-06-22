from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse, JSONResponse

from config.log_config import setup_logging
from controller.task_controller import task_router

app = FastAPI(
    title="Tasks API",
    description="Sistema de Gerenciamento de Tarefas",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None
)

app.include_router(task_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred"}
    )


@app.get("/", tags=["Redirect"], include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/docs", tags=["Redirect"], include_in_schema=False)
async def get_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Swagger UI"
    )


@app.get("/openapi.json", tags=["Redirect"], include_in_schema=False)
async def get_openapi():
    return get_swagger_ui(
        title="tasks API",
        version="1.0.0",
        description="API para gerenciamento de tarefas",
        routes=app.routes,
    )


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
