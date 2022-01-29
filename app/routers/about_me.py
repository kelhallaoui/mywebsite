from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
TEMPLATES = Jinja2Templates(directory="templates")


@router.get("/about_me", response_class=HTMLResponse)
def tutorials(request: Request):
    return TEMPLATES.TemplateResponse("about_me.html", {"request": request})
