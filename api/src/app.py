from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import tempfile
import generate_data

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['JSON_SORT_KEYS'] = False

@app.route("/api")
def hello():
    return "Hello, World!"

@app.route("/api/provinces")
def listOfProvinces():
    return jsonify(
        {
            "provinces":[
                {
                    "saskatchewan": {
                        "capital":"regina", 
                        "abr":"sk"
                    }, 
                    "manitoba": { 
                        "capital":"winnipeg",
                        "abr":"mb"
                    }
                }
            ]
        }
    )

@app.route("/api/draws")
def listOfDraws():
    summary = request.args.get('summary')
    draw_id = request.args.get('draw_id')

    if summary:
        resp = generate_data.get_draws_summary()
        return jsonify(resp)
    elif draw_id:
        resp = generate_data.get_draws_details(draw_id)
        return jsonify(resp)
    else:
        return jsonify({'response': 'parameters required'})

@app.route("/api/nocs/<noc_id>")
def listOfNocs(noc_id):
    resp = generate_data.get_nocs(noc_id)
    return jsonify(resp)
