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

@app.route('/run_model', methods=['POST'])
def run_model():
    if request.method == 'POST':
        # Extract the data from the form
        gender = float(request.form['gender'])
        age = float(request.form['age'])
        hypertension = float(request.form['hypertension'])
        heart_disease = float(request.form['heart_disease'])
        smoking_history = float(request.form['smoking_history'])
        bmi = float(request.form['bmi'])
        HbA1c_level = float(request.form['HbA1c_level'])
        blood_glucose_level = float(request.form['blood_glucose_level'])
        
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
