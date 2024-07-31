# Text_Extractor_using_flask
This README file provides an overview of the project, instructions on how to download the MNIST dataset, and  setting up the Flask application for recognizing digits from uploaded images.


# MNIST Dataset Downloader and Flask Application

This repository contains a script to download and save the MNIST dataset locally using TensorFlow, as well as a Flask application that uses a pre-trained MNIST model to recognize digits from uploaded images.

## Contents

- `download_mnist.py`: Script to download and save the MNIST dataset.
- `mnist_flask_app.py`: Flask application for digit recognition using the MNIST model.
- `templates/`: Directory containing HTML templates for the Flask application.

## Requirements

- Python 3.x
- Flask
- TensorFlow
- NumPy
- Pillow (PIL)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mnist-dataset-downloader.git
   cd mnist-dataset-downloader
Install the required Python packages:

bash
Copy code
pip install flask tensorflow numpy pillow
Downloading the MNIST Dataset
To download the MNIST dataset and save it locally, run the download_mnist.py script:

bash
Copy code
python download_mnist.py
This will download the MNIST dataset and save it in a directory named mnist_dataset as compressed .npz files:

train_images.npz
train_labels.npz
test_images.npz
test_labels.npz
Setting Up the Flask Application
Ensure you have the pre-trained MNIST model saved as mnist_model.h5 in the project directory. If not, train the model using the script provided above.

Run the Flask application:

bash
Copy code
python mnist_flask_app.py
Open your web browser and navigate to http://127.0.0.1:5000/ to use the application.

Flask Application Usage
Home Page: Upload an image containing a handwritten digit.
Result Page: View the predicted digit and download the processed image.
Files
download_mnist.py: The script to download and save the MNIST dataset.
mnist_flask_app.py: The Flask application for digit recognition.
templates/index.html: The HTML template for the home page.
templates/results.html: The HTML template for the result page.
