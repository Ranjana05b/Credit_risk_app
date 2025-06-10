import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)

# Load the trained logistic regression model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract float inputs from form
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        
        # Apply scaling
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        prediction_proba = model.predict_proba(features_scaled)[0][1]  # Probability of default

        result_text = "Likely to Default" if prediction[0] == 1 else "Likely to Pay on Time"
        return render_template("index.html", prediction_text=f"Prediction: {result_text} (Probability: {prediction_proba:.2f})")
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    flask_app.run(debug=True)

