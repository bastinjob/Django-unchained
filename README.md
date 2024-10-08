# Django ML Deployment

This is a Django web application that deploys a simple machine learning model (RandomForestClassifier) trained on the Iris dataset from scikit-learn. Users can input feature values and receive predictions from the model.

## Project Structure

- `mlproject/`: Django project folder.
- `mlapp/`: Django app handling the ML model integration.
- `model/`: Contains the script to train the model and the saved model file.
- `templates/`: HTML templates for user input and displaying the result.

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/bastinjob/Django-unchained.git
   cd ml-deployment-project
