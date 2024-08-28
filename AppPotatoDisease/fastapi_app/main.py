# main.py (FastAPI)
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Replace with your Django host
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Load the model
try:
    MODEL = tf.keras.models.load_model("/models/1")
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    try:
        image = np.array(Image.open(BytesIO(data)))
        logging.info(f"Image read successfully with shape: {image.shape}")
        return image
    except Exception as e:
        logging.error(f"Error reading image: {e}")
        raise HTTPException(status_code=400, detail="Invalid image file")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    logging.info(f"Received file: {file.filename}")
    
    try:
        # Read the file data
        contents = await file.read()
        logging.info(f"File size: {len(contents)} bytes")

        # Convert file data to image
        image = read_file_as_image(contents)
        logging.info(f"Image shape: {image.shape}")

        # Prepare image for model prediction
        img_batch = np.expand_dims(image, 0)
        logging.info(f"Image batch shape: {img_batch.shape}")

        # Make prediction
        predictions = MODEL.predict(img_batch)
        logging.info(f"Predictions: {predictions}")

        # Process prediction results
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        logging.error(f"Error processing prediction: {e}")
        raise HTTPException(status_code=500, detail="Failed to process image")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='localhost', port=8001)
