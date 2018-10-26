import json

from flask import Flask, jsonify, request, render_template

from forms import PredictionParametersForm

app = Flask('Futurice')
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/predict', methods=['POST'])
def predict():
    if request.headers['Content-Type'] == 'application/json':
        json_data = request.json
    else:
        json_data = json.loads(request.data)
    form = PredictionParametersForm.from_json(json_data)
    if form.validate():
        return jsonify('Valid!')
    return render_template('400.html', errors=form.errors), 400


@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
