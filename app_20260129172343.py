from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('churn_model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        age = int(request.form['age'])
        charges = float(request.form['charges'])
        tenure = int(request.form['tenure'])

        result = model.predict([[age, charges, tenure]])

        if result[0] == 1:
            prediction = "Customer Will Churn ❌"
        else:
            prediction = "Customer Will Stay ✅"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
python app.py