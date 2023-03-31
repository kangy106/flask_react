# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request, jsonify
from pprint import pprint


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = request.get_json()
        pprint(result)
        return jsonify({"test_post": f"OK: {result}"})
      
    return render_template('index.html')

      
if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)