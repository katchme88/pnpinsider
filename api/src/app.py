from flask import Flask, jsonify
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
    x = generate_data.get_draws()
    return jsonify(x)

@app.route("/api/nocs/<noc_id>")
def listOfNocs(noc_id):
    x = generate_data.get_nocs(noc_id)
    return jsonify(x)
