from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("churn_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        age = int(request.form["age"])
        charges = int(request.form["charges"])
        tenure = int(request.form["tenure"])

        data = np.array([[age, charges, tenure]])
        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "❌ Customer is likely to LEAVE"
        else:
            result = "✅ Customer will STAY"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
