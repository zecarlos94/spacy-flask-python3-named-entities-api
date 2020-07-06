from flask import Flask, jsonify, request
from utils import *

app = Flask(__name__)

@app.route('/classify', methods=['GET','POST'])
def classify():
  if request.method == 'POST':
    try:
        model, language = processRequiredModelAndLanguageParams(request)

        if isinstance(model, str) and isinstance(language, str):
            utterance = request.args.get('utterance')
            if isinstance(utterance, str) and not stringIsNullOrEmpty(utterance):
                data = processUtterance(utterance, model, language)

        return jsonify({'data': data}) 
    except Exception:
        pass
        return ('', 204)
  elif request.method == 'GET':
    try:
        model = request.args.get('model')
        language = request.args.get('language')
        
        if isinstance(model, str) and isinstance(language, str):
            utterance = request.args.get('utterance')
            if isinstance(utterance, str) and not stringIsNullOrEmpty(utterance):
                return visualizeUtterance(utterance, model, language)

        return ('', 400)
    except Exception:
        pass
        return ('', 400)