# Text_Extractor_using_flask
This README file provides an overview of the project, instructions on how to download the MNIST dataset, and how to run the provided script.

markdown
Copy code
# MNIST Dataset Downloader

This repository contains a script to download and save the MNIST dataset locally using TensorFlow. The MNIST dataset is a large database of handwritten digits commonly used for training various image processing systems.

## Contents

- `download_mnist.py`: Script to download and save the MNIST dataset.

## Requirements

- Python 3.x
- TensorFlow
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sahil762/mnist-dataset-downloader.git
   cd mnist-dataset-downloader
Install the required Python packages:

bash
Copy code
pip install tensorflow numpy
Usage
To download the MNIST dataset and save it locally, run the download_mnist.py script:

bash
Copy code
python download_mnist.py
This will download the MNIST dataset and save it in a directory named mnist_dataset as compressed .npz files:

train_images.npz
train_labels.npz
test_images.npz
test_labels.npz
Files
download_mnist.py: The script to download and save the MNIST dataset.
