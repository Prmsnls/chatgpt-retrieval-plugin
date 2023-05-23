from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from database.queries import get_ads_data
from operator import itemgetter




app = FastAPI(
        title="telegram bot",
        openapi_tags=[
            {
                "name": "Backend",
                "description": "telegram bot",
            },
        ],
        docs_url="/docs",
        redoc_url=None,
        openapi_url=None,
    )

@app.get("/docs", include_in_schema=False)
async def get_swagger_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@app.get("/redoc", include_in_schema=False)
async def get_redoc_documentation():
    return get_redoc_html(openapi_url="/openapi.json", title="docs")

@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/.well-known", StaticFiles(directory=".well-known", html = True), name="site")


# @app.route("/.well-known/ai-plugin.json")
# async def get_manifest(request):
#     file_path = "./local_server/ai-plugin.json"
#     simple_headers = {}
#     simple_headers["Access-Control-Allow-Private-Network"] = "true"
#     return FileResponse(file_path, media_type="text/json", headers=simple_headers)


# @app.route("/.well-known/logo.png")
# async def get_logo(request):
#     file_path = "./local_server/logo.png"
#     return FileResponse(file_path, media_type="text/json")


# @app.route("/.well-known/openapi.yaml")
# async def get_openapi(request):
#     file_path = "./local_server/openapi.yaml"
#     return FileResponse(file_path, media_type="text/json")



@app.get("/ads")
def get_ads(
):
    response = get_ads_data()
    all_ads = response.get("data", {}).get("asyncnewui_ads", [])
    all_objects = [item['title'] for item in all_ads]
    return JSONResponse(status_code=200, content=all_objects)

