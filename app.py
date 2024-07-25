from flask import Flask, request, render_template
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_model', methods=['GET', 'POST'])
def run_model():
    if request.method == 'POST':
        # Extract the data from the form
        gender = str(request.form.get('gender'))
        age = float(request.form['age'])
        hypertension = str(request.form.get('hypertension'))
        heart_disease = str(request.form.get('heart_disease'))
        smoking_history = str(request.form.get('smoking_history'))
        feet = float(request.form['feet'])
        inches = float(request.form['inches'])
        weight = float(request.form['weight'])
        HbA1c_level = float(request.form['HbA1c_level'])
        blood_glucose_level = float(request.form['blood_glucose_level'])

        #calculations
        gender = 1 if gender == 'M' else 0
        hypertension = 1 if hypertension == 'Y' else 0
        heart_disease = 1 if heart_disease == 'Y' else 0
        smoking_history = 1 if smoking_history == 'Y' else 0
        height = (feet/3.281) + (inches/39.37)
        bmi = weight / (height**2)
        
        # Create the data list
        data = [gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]
        
        # Convert the list to a DataFrame
        columns = ["gender", "age", "hypertension", "heart_disease", "smoking_history", "bmi", "HbA1c_level", "blood_glucose_level"]
        input_data_df = pd.DataFrame([data], columns=columns)
        
        # Convert all columns to numeric types
        input_data_df = input_data_df.apply(pd.to_numeric, errors='coerce')

        # Make the prediction
        y_pred = model.predict(input_data_df)
        result = "Diabetic" if y_pred[0] == 1 else "Non-diabetic"
        
        # Render the result on the same page
        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
