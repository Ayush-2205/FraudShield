from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get inputs from form
        premium = float(request.form["premium"])
        total_claim = float(request.form["total_claim"])
        age = float(request.form["age"])
        months = float(request.form["months"])

        # Simple intelligent rule
        if total_claim > premium * 20:
            prediction = 1  # High Risk
            result = "High Risk ⚠️"
            explanation = (
                "The total claim amount is extremely high compared to the annual premium. "
                "This pattern is often associated with fraudulent or suspicious claims."
            )
        else:
            prediction = 0  # Low Risk
            result = "Low Risk ✅"
            explanation = (
                "The claim amount is reasonable compared to the premium and user profile. "
                "This indicates a legitimate insurance claim."
            )

        return render_template(
            "index.html",
            prediction_text=result,
            explanation=explanation
        )

    except:
        return render_template(
            "index.html",
            prediction_text="Error ❌",
            explanation="Please enter valid numeric values in all fields."
        )

if __name__ == "__main__":
    app.run(debug=True)
