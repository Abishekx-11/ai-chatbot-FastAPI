
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


chat_history = []



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

    chat_history.append({               # appending user message in list as dictionary
        "role": "user",
        "content":user_message
    })

    conversation = ""           #created empty string 

    for every_dict in chat_history:                     #created a conversation by appending every dictionary 
        conversation += f"{every_dict["role"]}: {every_dict["content"]}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation                   #passing the conversation to AI
    )


    ai_message = response.text 

    chat_history.append({
        "role":"AI",
        "content":ai_message
    })

    return {
        "message": ai_message
    }











