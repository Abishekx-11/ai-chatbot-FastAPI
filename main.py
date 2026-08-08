
from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name = "index.html"

    )


@app.post("/chat")
async def Chat(request:Request):
    request_data = await request.json()
    user_message = request_data["message"]

    return { "message": f"You said {user_message}"}

