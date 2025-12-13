from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.inference import recommend_ads

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/recommend/{user_id}")
def recommend(user_id: int, k: int = 5):
    result = recommend_ads(user_id, k)
    return result.to_dict(orient="records")
