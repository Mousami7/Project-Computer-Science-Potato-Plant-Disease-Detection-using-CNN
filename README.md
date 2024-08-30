# CropWatch: Revolutionizing Precision Farming with CNNs
CropWatch is a web-based application designed to detect diseases in potato plants using machine learning techniques. The application allows users to upload images of potato plants for disease prediction and provides real-time detection capabilities using a camera.

![Screenshot 2024-08-20 142252](https://github.com/user-attachments/assets/183bccf9-9446-481c-b7d0-4bae7d9dcf54)

## Features
- Image upload for disease detection
- Real-time disease detection using a camera
- User-friendly web interface
- Accurate predictions using a Convolutional Neural Network (CNN)
## Technologies Used
- Django (Python Web Framework)
- TensorFlow and Keras (Machine Learning)
- HTML, CSS, JavaScript (Frontend)
- SQLite (Database)

# Potato Plant Disease Detection using CNN - Setup Guide

## Prerequisites
- **Python**: Ensure Python 3.7.7 or higher is installed on your system. You can download it from [python.org](https://www.python.org/).
- **pip**: Ensure pip (Python package installer) is installed. It usually comes with Python.

## Setup Instructions

# Step 1: Download or Clone the Project

![1](https://github.com/user-attachments/assets/7799b3e6-44b9-4839-b7b2-f19a53742f42)

# Step 2: Navigate to the Project Directory
Once the project is downloaded:
Using File Explorer:
Open File Explorer and navigate to the folder where the project was downloaded or extracted (e.g., C:\Users\YourUsername\Downloads\Project-Computer-Science-Potato-Plant-Disease-Detection-using-CNN).

![2](https://github.com/user-attachments/assets/002a2bfa-ae89-4e1d-8c62-89c51b288b8a)

## 3. Open Command Prompt from the Project Directory
To open Command Prompt from the project directory:
Using File Explorer:
Open the project folder in File Explorer.
In the address bar, type cmd and press Enter.

![3](https://github.com/user-attachments/assets/61bc0cc6-a9a9-4619-a341-deb2f9c9a120)

# Step 4: Install Project Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Step 5: Check Project Directory
Ensure you are in the directory that contains the manage.py file. If not, navigate to that directory:
```bash
cd 'path/to/the/project/folder/consisting/manage.py'
```

## Step 6: Run the Development Server

![4](https://github.com/user-attachments/assets/9f33ae68-7c1c-4d45-8b73-d2bc436c513b)

After installing all dependencies, start the development server by running:
on command prompt write the following command and Start the development server:
```bash
python manage.py runserver
```

## Step 7: Access the Application

![5](https://github.com/user-attachments/assets/98e021ae-f08c-46bd-a1ee-9d3b060e333d)

Open your Chrome browser and go to: http://localhost:8000

## Alternate way
1.Open command prompt and paste the project path which consists manage.py [cd 'path/to/the/project/folder/consisting/manage.py']

2.After going to the respective directory run the command "python manage.py runserver"

3.Open google chrome and type "localhost:8000

## Usage
- **Upload Image:** Go to the home page and upload an image of a potato plant. The system will process the image and display the disease detection results.
![UploadImage](https://github.com/user-attachments/assets/76419598-dc31-44e6-81df-43d6dd2eb25e)

![Prediction Result](https://github.com/user-attachments/assets/c8d9a649-6ef0-4e50-bed8-644ae5dce2a6)

- **Real-Time Detection:** Navigate to the real-time detection page, enable your camera, and show a potato plant leaf. The system will provide an immediate diagnosis.

![Real Time Detection](https://github.com/user-attachments/assets/a084b5f0-0c04-4dcf-b213-7fed5d05fa75)

## Dataset
The model is trained using the Plant Village dataset from Kaggle, focusing specifically on potato plant data.
this is the link to dataset [https://www.kaggle.com/datasets/arjuntejaswi/plant-village]
## Acknowledgements
- Prof. Dr. Oezdemir Cetin for guidance and support.
- The Kaggleb & Plant Village team for providing the dataset.
