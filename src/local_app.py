# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

from flask import Flask, request, jsonify
from mlxtend.utils.data import load_model
from .front import front
from .. import __version__ as version

app = Flask(__name__)

model = load_model(project="gmsc", version=version)

@app.route('/realtime', methods=['POST'])
def realtime():
    return jsonify(front(request.get_json(),
                         model,
                         env="local"))

@app.route('/batch', methods=['POST'])
def batch():
    # TODO: get and return CSV file URIs
    return