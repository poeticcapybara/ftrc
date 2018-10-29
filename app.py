import json
import pickle
from pathlib import Path

from flask import Flask, jsonify, request, render_template
import pandas as pd

from forms import PredictionParametersForm
from DS.train_and_export import generate_model

app = Flask('Futurice')
app.config['SECRET_KEY'] = 'secret_key'
model_path = Path('.') / 'model_sklearn.pkl'

if not model_path.exists():
    generate_model(output_dir=Path(__file__).parent)

with open(model_path, 'rb') as f:
    model = pickle.load(f)


def single_prediction(X):
    if isinstance(model['model'], str):
        coeffs = model['coeffs']
        intercept = model['intercept']
        col_order = model['col_order']
        std_err = model['std_err']
        data = pd.DataFrame.from_dict(X, orient='index').T
        data_point = data[col_order]
        prediction = intercept+data_point.dot(coeffs)
    else:
        regression_model = model['model']
        std_err = model['std_err']
        col_order = model['col_order']
        data = pd.DataFrame.from_dict(X, orient='index').T
        data_point = data[col_order]
        prediction = regression_model.predict(data_point)[0]
    return prediction, std_err


@app.route('/predict', methods=['POST'])
def predict():
    if request.headers['Content-Type'] == 'application/json':
        json_data = request.json
    else:
        json_data = json.loads(request.data)
    form = PredictionParametersForm.from_json(json_data)
    if form.validate():
        prediction, std_err = single_prediction(json_data)
        return jsonify({'house_value': prediction, 'stddev': std_err})
    return render_template('400.html', errors=form.errors), 400


@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
