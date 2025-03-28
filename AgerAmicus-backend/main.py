import os
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = FastAPI(title="AgerAmicus Backend API")

# Enable CORS for frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment variables
load_dotenv()

# Load CNN plant disease model
MODEL_PATH = os.path.join("models", "custom_plant_model.h5")
model = load_model(MODEL_PATH)

# Class labels used in CNN training
CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___healthy",
    "Tomato___Early_blight"
]

# Image preprocessing
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize((224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0
    return np.expand_dims(image_array, axis=0)

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to AgerAmicus!"}

# CNN Image Analysis Endpoint
@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPG and PNG allowed.")
    
    try:
        contents = await file.read()
        image_array = preprocess_image(contents)
        prediction = model.predict(image_array)
        top_index = np.argmax(prediction)
        predicted_class = CLASS_NAMES[top_index]
        confidence = round(float(prediction[0][top_index]) * 100, 2)

        return {"prediction": predicted_class, "confidence": confidence}
    
    except Exception:
        raise HTTPException(status_code=500, detail="Image processing failed.")

# Chat Request Model
class ChatRequest(BaseModel):
    prompt: str

# Chatbot Endpoint (API structure ready, logic placeholder)
@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    # Placeholder response for MVP
    return {
        "response": f"You asked: '{request.prompt}' — Chatbot feature coming soon!"
    }

