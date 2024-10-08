# mlapp/views.py
from django.shortcuts import render
import joblib
import numpy as np
import os

# Load the saved model
model_path = os.path.join(os.path.dirname(__file__), '../../model/model.joblib')
model = joblib.load(model_path)

def predict(request):
    if request.method == 'POST':
        # Get input data from the form
        input_data = [
            request.POST.get('feature1'),
            request.POST.get('feature2'),
            request.POST.get('feature3'),
            request.POST.get('feature4')
        ]
        input_data = np.array(input_data, dtype=float).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)[0]

        # Map the prediction to the Iris species
        iris_species = ['Setosa', 'Versicolor', 'Virginica']
        predicted_species = iris_species[prediction]

        # Render the result back to the user
        return render(request, 'result.html', {'prediction': predicted_species})
    
    return render(request, 'predict.html')
