from flask import Flask, render_template, request
from model import predict_traffic_alert

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    city_name = request.form.get('city_name')
    prediction = predict_traffic_alert(city_name)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
