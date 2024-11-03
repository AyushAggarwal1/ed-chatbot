from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import openai
import logging
import os

# Directly assign the OpenAI API key (be cautious with this approach)
# openai.api_key = "<your-api-key>"

# get api key from env
# openai.api_key = os.env("openai_key")


# Initialize FastAPI app and logger
app = FastAPI()
logging.basicConfig(level=logging.ERROR)
templates = Jinja2Templates(directory="templates")

# import static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message")
        if not user_message:
            raise HTTPException(status_code=400, detail="Message field is required.")

        # Generate AI response using OpenAI's gpt-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        
        # Extract and return the AI response
        ai_response = response.choices[0].message['content'].strip()
        return {"response": ai_response}
    
    except openai.error.RateLimitError:
        logging.error("Rate limit exceeded.")
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
    
    except openai.error.InvalidRequestError as e:
        logging.error(f"Invalid request error: {e}")
        raise HTTPException(status_code=400, detail="Invalid request. Please check your input.")
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)