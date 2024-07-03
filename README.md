
# Food Adulteration Classification

This repository contains a Flask application that uses a logistic regression model to classify whether a food product is adulterated based on its nutritional composition.

## Requirements

- Python 3.x
- Flask
- NumPy
- Joblib

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/food-adulteration-classification.git
   cd food-adulteration-classification
Usage
Home Page:

The home page contains a form where you can input the quantities per 100 grams of the food product:

Carbohydrates (grams)
Protein (grams)
Fat (grams)
Preservatives (grams)
Artificial Sweeteners (grams)
Sugar (grams)
Prediction:

After filling out the form, submit it to get the prediction result. The application will display whether the food product is "Adulterated" or "Not Adulterated".

File Structure
app.py: The main Flask application.
logistic_regression_model.pkl: The pre-trained logistic regression model.
templates/
index.html: The main page template with the input form.
result.html: The result page template displaying the prediction.
License
This project is licensed under the MIT License.



Ensure your project directory has the following structure:

food-adulteration-classification/
│
├── app.py
├── logistic_regression_model.pkl
├── templates/
│ ├── index.html
│ └── result.html
└── README.md
