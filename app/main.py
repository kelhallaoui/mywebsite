from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from typing import Optional, Any
from pathlib import Path

from app.routers import tutorials, accordion, about_me

BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH.parent / "templates"))


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
app.mount(str(BASE_PATH.parent / "static"), StaticFiles(directory="static"), name="static")
api_router = APIRouter()


@api_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return TEMPLATES.TemplateResponse("homepage.html", {"request": request})


app.include_router(api_router)
app.include_router(accordion.router)
app.include_router(tutorials.router)
app.include_router(about_me.router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")