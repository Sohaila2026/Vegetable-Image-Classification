# Vegetable Image Classification

## Project Overview
This project is a Deep Learning application that classifies vegetable images into 15 different categories using a Convolutional Neural Network (CNN).

The model was developed using TensorFlow and Keras and trained on the Vegetable Image Dataset.

## Dataset
The dataset contains 15 vegetable classes:

1. Bean
2. Bitter Gourd
3. Bottle Gourd
4. Brinjal
5. Broccoli
6. Cabbage
7. Capsicum
8. Carrot
9. Cauliflower
10. Cucumber
11. Papaya
12. Potato
13. Pumpkin
14. Radish
15. Tomato

The dataset is divided into:
- Training Set
- Validation Set
- Testing Set

## Technologies Used
- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Streamlit

## Deep Learning Model
A Convolutional Neural Network (CNN) was built and trained to classify vegetable images into 15 classes.

## Streamlit Application
The Streamlit application allows users to:
- Upload a vegetable image.
- Predict the vegetable category.
- Display the predicted class.
- Show the prediction confidence.

## Project Files
- `quize_dl.ipynb`: Model training and evaluation.
- `qizestrem.py`: Streamlit application.
- `class_names.json`: Class names mapping.
- `README.md`: Project documentation.

## Trained Model
The trained model is hosted on Google Drive because of its large file size.

**Model File:** `Vegetable_cnn.keras`

[Download the trained model](https://drive.google.com/file/d/10nIECptS4f7VypUfOHWq2DkIsLgDyokj/view?usp=sharing)

Download the model and place it in the project folder before running the application.

## How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App

```bash
streamlit run qizestrem.py
```

## Author
Sohaila Mohamed Anwar

GitHub: [Sohaila2026](https://github.com/Sohaila2026)
