from os import environ
import logging
import json
from flask import Flask, jsonify, Response, request
from flask import render_template

app = Flask(__name__)
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')
    return render_template('index.html', powered_by=environ.get('POWERED_BY', 'Antonio Silva'))


@app.route('/image/comparison')
def ir():
    data = [0]
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
