from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
TEMPLATES = Jinja2Templates(directory="templates")


@router.get("/tutorials")
def tutorials(request: Request):
    return TEMPLATES.TemplateResponse("tutorials/home.html", {"request": request})


@router.get("/tutorials/deep_learning")
def tutorials_deep_learning(request: Request):
    return TEMPLATES.TemplateResponse("tutorials/deep_learning.html", {"request": request})

@router.get("/tutorials/feature_reduction")
def tutorials_feature_reduction(request: Request):
    return TEMPLATES.TemplateResponse("tutorials/feature_reduction.html", {"request": request})
