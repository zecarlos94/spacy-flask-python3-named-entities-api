import spacy
from spacy import displacy
from settings import *

nlpSmallDatasetPT  = spacy.load("pt_core_news_sm")
nlpMediumDatasetPT = spacy.load("pt_core_news_md")
nlpLargeDatasetPT  = spacy.load("pt_core_news_lg")
nlpSmallDatasetEN  = spacy.load("en_core_web_sm")
nlpMediumDatasetEN = spacy.load("en_core_web_md")
nlpLargeDatasetEN  = spacy.load("en_core_web_lg")

def stringIsNullOrEmpty(string):
    return not string or string.isspace()

def processRequiredModelAndLanguageParams(request):
    # get desired model and language
    req_data = request.get_json()
    model = req_data['model']
    language = req_data['language']
    return model, language

def getDocBasedOnDesiredModelAndLanguage(utterance, model, language):
    result = dict()
    doc = None

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

    return doc, result
            
def visualizeUtterance(utterance, model, language):
    try:
        doc, result = getDocBasedOnDesiredModelAndLanguage(utterance, model, language)

        if doc is not None:
            return displacy.render(doc, style="ent")
    except Exception:
        pass

    return ('', 400)

def processUtterance(utterance, model, language):
    result = dict()

    try:
        doc, result = getDocBasedOnDesiredModelAndLanguage(utterance, model, language)

        if doc is not None:
            ents = displacy.parse_ents(doc)
            deps = displacy.parse_deps(doc)
            
            result.update(ents)
            result.update(deps)
    except Exception:
        pass   

    return result