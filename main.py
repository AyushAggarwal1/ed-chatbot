from fastapi import FastAPI, Request, HTTPException
import openai
import logging

# Directly assign the OpenAI API key (be cautious with this approach)
openai.api_key - "<your-api-key>"

# Initialize FastAPI app and logger
app = FastAPI()
logging.basicConfig(level=logging.ERROR)

@app.get("/")
async def root():
    return {"message": "Welcome to the chatbot API"}
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