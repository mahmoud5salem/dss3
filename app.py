import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
# create flask application
app = Flask(__name__)

# load the pickle model
model = pickle.load(open("model.pkl", "rb"))

# go to home page
@app.route("/")
def Home():
    return render_template("page2.html")
# go to predict page
@app.route("/predict", methods= ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    return render_template("page2.html", prediction_text = "This car price is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)


