from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("fraud_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    policy_premium = float(request.form["policy_premium"])
    total_claim = float(request.form["total_claim_amount"])
    age = float(request.form["age"])
    vehicle_claim = float(request.form["vehicle_claim"])

    data = [[policy_premium, total_claim, age, vehicle_claim]]
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "⚠️ High Risk: Potential Fraud Detected"
    else:
        result = "✅ Low Risk: Legitimate Claim"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
