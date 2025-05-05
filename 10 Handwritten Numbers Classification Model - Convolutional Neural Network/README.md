# Handwritten Numbers Classification Model - Convolutional Neural Network

## Objective

This project implements a Convolutional Neural Network (CNN) in TensorFlow/Keras to classify handwritten digits using the MNIST dataset. Additionally, the trained model is used to predict custom images of digits saved locally.

## Steps Followed

- **Importing Libraries**  
- **Importing the Dataset**  
- **Model Architecture**  
- **Testing the Model**  

## **Importing Libraries**

The following Python libraries were used in this project:

- **tensorflow/keras** – to build and train the CNN  
- **numpy** – for numerical operations  
- **matplotlib.pyplot** – for visualizing predictions  
- **Pillow (PIL)** – to load and process images  
- **scikit-learn (sklearn)** – for evaluation and confusion matrix  

## Dataset

- **Training/Testing:** MNIST dataset (60,000 training + 10,000 testing samples)
- **Custom Testing:** 6 user-provided digit images stored in `images/` folder

## Model Architecture

The CNN model was created following this format:

- Conv2D (32 filters, 3x3 kernel, ReLU activation)
- MaxPooling2D (2x2)
- Conv2D (64 filters, 3x3 kernel, ReLU activation)
- MaxPooling2D (2x2)
- Flatten
- Dense (64 units, ReLU)
- Dense (10 units, Softmax) — output layer for 10 digit classes (0-9)

## Testing model

- Achieved high accuracy on clean MNIST test data
- Struggled with custom handwritten images, especially those with less clearly defined digits