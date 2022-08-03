## REST API APP ##
import json
import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app = FastAPI()

@app.get("/", response_class= HTMLResponse)
def home_view(request: Request):
    return templates.TemplatesResponse("home.html", {"request": request, "abc": 123})



@app.post("/")
def home_detail_view():
    return {"Hello": "World"}

## YOUTUBE TUTORIAL MIN: 28:27 ##