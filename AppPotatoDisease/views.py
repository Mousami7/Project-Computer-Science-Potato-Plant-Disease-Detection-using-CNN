# views.py (Django)
from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
from django.shortcuts import render
from django.http import JsonResponse
import requests
import tensorflow as tf
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
import numpy as np
# Assuming your FastAPI server is running on localhost:8001
import cv2
import numpy as np
from django.http import StreamingHttpResponse
from django.shortcuts import render
from tensorflow.keras.models import load_model
def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

# Assuming your FastAPI server is running on localhost:8001

#MODEL = tf.keras.models.load_model("C:/workspace2/PotatoDisease/model.h5")
#MODEL1 = load_model("potatoes.h5")

MODEL = tf.keras.models.load_model("model.h5")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"] # Your class names

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        
        try:
            # Read the file data
            contents = image.read()

            # Convert file data to image
            image_data = read_file_as_image(contents)

            # Prepare image for model prediction
            img_batch = np.expand_dims(image_data, 0)

            # Make prediction
            predictions = MODEL.predict(img_batch)

            # Process prediction results
            predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
            confidence = np.max(predictions[0])
            
            context = {
                'class': predicted_class,
                'confidence': float(confidence)
            }
            return render(request, 'home.html', context)
        except Exception as e:
            error_message = str(e)
            context = {'error': error_message}
            return render(request, 'home.html', context)
    
    return redirect('home') 
def read_file_as_image(data) -> np.ndarray:
    try:
        image = np.array(Image.open(BytesIO(data)))
        return image
    except Exception as e:
        raise ValueError("Invalid image file")



def gen(camera):
    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()
        if not ret:
            break

        # Convert frame to appropriate format for model
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        print(frame_rgb)
        resized_frame = cv2.resize(frame_rgb, (224, 224))  # Resize as per your model requirement
        normalized_frame = resized_frame / 255.0  # Normalize if needed
        img_batch = np.expand_dims(resized_frame, axis=0)

        # Predict
        predictions = MODEL.predict(img_batch)
        predicted_classes = [CLASS_NAMES[i] for i, prob in enumerate(predictions[0]) if prob > 0.40]

        # Add text to frame
        text = ', '.join([f"{cls}: {prob:.2f}" for cls, prob in zip(predicted_classes, predictions[0])])
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Real-time Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()

def realtime_detection(request):
    camera = cv2.VideoCapture(0)  # 0 for default camera
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    gen(camera)
    return HttpResponse("Real-time detection completed.")



