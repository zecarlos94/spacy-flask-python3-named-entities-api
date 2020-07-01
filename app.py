import spacy
from spacy import displacy
from flask import Flask, jsonify, request
from utils import *
from settings import *

nlpSmallDatasetPT  = spacy.load("pt_core_news_sm")
nlpMediumDatasetPT = spacy.load("pt_core_news_md")
#nlpLargeDatasetPT  = spacy.load("pt_core_news_lg")
nlpSmallDatasetEN  = spacy.load("en_core_web_sm")
#nlpMediumDatasetEN = spacy.load("en_core_web_md")
#nlpLargeDatasetEN  = spacy.load("en_core_web_lg")

app = Flask(__name__)

def visualizeUtterance(utterance):
    doc = nlpSmallDatasetPT(utterance)
    return displacy.render(doc, style="ent")

def processUtterance(utterance, model, language):
    result = dict()

    if not stringIsNullOrEmpty(utterance) and not stringIsNullOrEmpty(model) and not stringIsNullOrEmpty(language):
        if pt in language:
            if smallDataset in model:
                result.update({'model': smallDataset})
                doc = nlpSmallDatasetPT(utterance)
            elif mediumDataset in model:
                result.update({'model': mediumDataset})
                doc = nlpMediumDatasetPT(utterance)
            elif largeDataset in model:
                result.update({'model': largeDataset})
                doc = nlpLargeDatasetPT(utterance)
            else:
                # model not supported
                return result
        elif en in language: 
            if smallDataset in model:
                result.update({'model': smallDataset})
                doc = nlpSmallDatasetEN(utterance)
            elif mediumDataset in model:
                result.update({'model': mediumDataset})
                doc = nlpMediumDatasetEN(utterance)
            elif largeDataset in model:
                result.update({'model': largeDataset})
                doc = nlpLargeDatasetEN(utterance)
            else:
                # model not supported
                return result
        else: 
            # language not supported
            return result

        ents = displacy.parse_ents(doc)
        deps = displacy.parse_deps(doc)
        
        result.update(ents)
        result.update(deps)

    return result

@app.route('/classify', methods=['GET','POST'])
def classify():
  if request.method == 'POST':
    try:
        # get desired model and language
        req_data = request.get_json()
        model = req_data['model']
        language = req_data['language']

        if isinstance(model, str) and isinstance(language, str):
            utterance = request.args.get('utterance')
            if isinstance(utterance, str): 
                data = processUtterance(utterance, model, language)

        return jsonify({'data': data}) 
    except Exception:
        pass
        return ('', 204)
  elif request.method == 'GET':
    try:
        utterance = request.args.get('utterance')

        if isinstance(utterance, str) and not stringIsNullOrEmpty(utterance):
            return visualizeUtterance(utterance)

        return ('', 400)
    except Exception:
        pass
        return ('', 400)