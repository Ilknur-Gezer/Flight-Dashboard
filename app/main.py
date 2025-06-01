from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from app.routes import flights
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(flights.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
