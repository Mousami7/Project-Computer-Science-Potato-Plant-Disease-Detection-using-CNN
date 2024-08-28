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

### Step 1: Download or Clone the Project
Clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/Mousami7/Potato-Plant-Disease-Detection-using-CNN.git
```
### Step 2: Navigate to the Project Directory
Change directory to the project folder:

```bash
cd Potato-Plant-Disease-Detection-using-CNN
```

Step 3: Create a Virtual Environment
Create a virtual environment:

```bash
python -m venv env
```

Step 4: Activate the Virtual Environment
Activate the virtual environment:

On Windows:
```bash
env\Scripts\activate
```

Step 5: Install Project Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Step 6: Check Project Directory
Ensure you are in the directory that contains the manage.py file. If not, navigate to that directory:
```bash
cd 'path/to/the/project/folder/consisting/manage.py'
```

Step 7: Apply Migrations
Apply the database migrations:
```bash
python manage.py migrate
```

Step 8: Run the Development Server
Start the development server:
```bash
python manage.py runserver
```

Step 9: Access the Application
Open your Chrome browser and go to: http://localhost:8000


## Alternate way
1.Open command prompt and paste the project path which consists manage.py [cd 'path/to/the/project/folder/consisting/manage.py']

2.After going to the respective directory run the command "python manage.py runserver"

3.Open google chrome and type "localhost:8000

## Usage
- **Upload Image:** Go to the home page and upload an image of a potato plant. The system will process the image and display the disease detection results.
- **Real-Time Detection:** Navigate to the real-time detection page, enable your camera, and show a potato plant leaf. The system will provide an immediate diagnosis.
## Dataset
The model is trained using the Plant Village dataset from Kaggle, focusing specifically on potato plant data.
this is the link to dataset [https://www.kaggle.com/datasets/arjuntejaswi/plant-village]
## Acknowledgements
- Prof. Dr. Oezdemir Cetin for guidance and support.
- The Kaggleb & Plant Village team for providing the dataset.
