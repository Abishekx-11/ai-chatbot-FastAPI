
from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message
    )

    return {
        "message": response.text
    }







