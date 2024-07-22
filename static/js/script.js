// document.getElementById('predictButton').addEventListener('click', function () {
//     const gender = document.getElementById('gender').value;
//     const age = document.getElementById('age').value;
//     const hypertension = document.getElementById('Hypertension').value;
//     const heartDisease = document.getElementById('heartDisease').value;
//     const smokingHistory = document.getElementById('smokingHistory').value;
//     const bmi = document.getElementById('bmi').value;
//     const HbA1c = document.getElementById('HbA1c').value;
//     const bloodGlucose = document.getElementById('bloodGlucose').value;


//     console.log(age);
  
//     fetch('http://127.0.0.1:5000/run_model', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify({
//         gender: gender,
//         age: age,
//         hypertension: hypertension,
//         heart_disease: heartDisease,
//         smoking_history: smokingHistory,
//         bmi: bmi,
//         HbA1c_level: HbA1c,
//         blood_glucose_level: bloodGlucose
//       }),
//     })
//     .then(response => response.json())
//     .then(data => {
//       const resultDiv = document.getElementById('result');
//       const resultText = document.getElementById('result-text');
      
//       if (data.error) {
//         resultText.textContent = `Error: ${data.error}`;
//       } else {
//         resultText.textContent = `Prediction: ${data.prediction}`;
//       }
  
//       resultDiv.style.display = 'block';
//     })
//     .catch(error => {
//       const resultDiv = document.getElementById('result');
//       const resultText = document.getElementById('result-text');
      
//       resultText.textContent = `Error: ${error}`;
//       resultDiv.style.display = 'block';
//     });
//   });
  