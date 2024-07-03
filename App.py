from flask import Flask, request, render_template
import numpy as np
import joblib

# Load the saved model
model = joblib.load("logistic_regression_model.pkl")

# Initialize the Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    carbohydrates = float(request.form['carbohydrates'])
    protein = float(request.form['protein'])
    fat = float(request.form['fat'])
    preservatives = float(request.form['preservatives'])
    artificial_sweeteners = float(request.form['artificial_sweeteners'])
    sugar = float(request.form['sugar'])

    # Prepare the input data
    input_data = np.array([[carbohydrates, protein, fat, preservatives, artificial_sweeteners, sugar]])
    
    # Make the prediction
    prediction = model.predict(input_data)
    prediction_label = "Adulterated" if prediction[0] == 1 else "Not Adulterated"

    # Render the result
    return render_template('result.html', prediction=prediction_label)

if __name__ == "__main__":
    app.run(debug=True)
