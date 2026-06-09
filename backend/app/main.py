from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.app.api.routes import router

app = FastAPI(
    title="GOVPESSOAS 360 MVP",
    version="0.1.0",
    description="MVP para governanca de pessoas, compliance trabalhista, previdenciario e SST em municipios.",
)

app.include_router(router, prefix="/api")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
