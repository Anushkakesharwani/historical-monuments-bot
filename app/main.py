from fastapi import FastAPI
from pydantic import BaseModel

# Step 1: Create FastAPI app
app = FastAPI()

# Step 2: Define the Request Body using Pydantic
class ChatRequest(BaseModel):
    message: str  # This means the user must send {"message": "something"}

# Step 3: Create a simple route
@app.get("/")
def home():
    return {"message": "Welcome to Historical Bot! Ask me about historical monuments."}

# Step 4: POST /chat expects a ChatRequest body
@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    # Simple response logic (you can make this smarter later)
    if "taj mahal" in user_message:
        reply = "Taj Mahal is a beautiful monument in Agra, India. It's one of the Seven Wonders of the World."
    else:
        reply = "I can help you with information about historical monuments around the world."

    return {"reply": reply}
