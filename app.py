from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        age = int(request.form["age"])
        charges = int(request.form["charges"])
        tenure = int(request.form["tenure"])

        # SIMPLE & LOGICAL RULE
        if tenure < 3 and charges < 3000:
            result = "❌ Customer is likely to LEAVE"
        else:
            result = "✅ Customer will STAY"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
