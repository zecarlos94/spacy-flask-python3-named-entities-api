# Spacy Generic Named Entities Api Built With Flask and Python3

This repository provides a REST API that returns all named entities detected on a given utterance based on desired dataset and language using Flask and Spacy and Python3. At the moment this API supports the following models and languages (datasets):

* en_core_web_sm
* en_core_web_md
* en_core_web_lg
* pt_core_news_sm
* pt_core_news_md
* pt_core_news_lg

# Installation

You can setup your python3 venv environment using all commands provided on run.sh to download all dependencies (spacy datasets)

# Usage

## POST Request

To obtain all named entities and terms' dependencies on "eu quero marcar uma consulta de cardiologia para o dr. jorge lima na cuf porto"/"I want to schedule a cardiology appointment for dr. jorge lima at cuf porto" you can do it with the following curl request via Postman or Insomnia.

```
curl --request POST \
  --url 'http://127.0.0.1:50002/classify?utterance=eu%20quero%20marcar%20uma%20consulta%20de%20cardiologia%20para%20o%20dr%20jorge%20lima%20na%20cuf%20porto' \
  --header 'content-type: application/json' \
  --data '{
	"model": "md",
	"language": "pt"
}'
```

or

```
curl --request POST \
  --url 'http://127.0.0.1:50002/classify?utterance=i%20want%20to%20schedule%20a%20cardiology%20appointment%20for%20dr%20jorge%20lima%20at%20cuf%20porto' \
  --header 'content-type: application/json' \
  --data '{
	"model": "md",
	"language": "en"
}'
```

## POST Response

```
{
  "data": {
    "arcs": [
      {
        "dir": "left",
        "end": 1,
        "label": "nsubj",
        "start": 0
      },
      {
        "dir": "right",
        "end": 2,
        "label": "xcomp",
        "start": 1
      },
      {
        "dir": "left",
        "end": 4,
        "label": "det",
        "start": 3
      },
      {
        "dir": "right",
        "end": 4,
        "label": "obj",
        "start": 2
      },
      {
        "dir": "left",
        "end": 6,
        "label": "case",
        "start": 5
      },
      {
        "dir": "right",
        "end": 6,
        "label": "nmod",
        "start": 4
      },
      {
        "dir": "left",
        "end": 9,
        "label": "case",
        "start": 7
      },
      {
        "dir": "left",
        "end": 9,
        "label": "det",
        "start": 8
      },
      {
        "dir": "right",
        "end": 9,
        "label": "nmod",
        "start": 4
      },
      {
        "dir": "right",
        "end": 10,
        "label": "appos",
        "start": 9
      },
      {
        "dir": "right",
        "end": 11,
        "label": "flat:name",
        "start": 10
      },
      {
        "dir": "left",
        "end": 13,
        "label": "case",
        "start": 12
      },
      {
        "dir": "right",
        "end": 13,
        "label": "obl",
        "start": 2
      },
      {
        "dir": "right",
        "end": 14,
        "label": "flat:name",
        "start": 13
      }
    ],
    "ents": [
      {
        "end": 64,
        "label": "PER",
        "start": 54
      },
      {
        "end": 77,
        "label": "ORG",
        "start": 68
      }
    ],
    "model": "md",
    "settings": {
      "direction": "ltr",
      "lang": "pt"
    },
    "text": "eu quero marcar uma consulta de cardiologia para o dr jorge lima na cuf porto",
    "title": null,
    "words": [
      {
        "lemma": null,
        "tag": "PRON",
        "text": "eu"
      },
      {
        "lemma": null,
        "tag": "VERB",
        "text": "quero"
      },
      {
        "lemma": null,
        "tag": "VERB",
        "text": "marcar"
      },
      {
        "lemma": null,
        "tag": "DET",
        "text": "uma"
      },
      {
        "lemma": null,
        "tag": "NOUN",
        "text": "consulta"
      },
      {
        "lemma": null,
        "tag": "ADP",
        "text": "de"
      },
      {
        "lemma": null,
        "tag": "NOUN",
        "text": "cardiologia"
      },
      {
        "lemma": null,
        "tag": "ADP",
        "text": "para"
      },
      {
        "lemma": null,
        "tag": "DET",
        "text": "o"
      },
      {
        "lemma": null,
        "tag": "PROPN",
        "text": "dr"
      },
      {
        "lemma": null,
        "tag": "PROPN",
        "text": "jorge"
      },
      {
        "lemma": null,
        "tag": "PROPN",
        "text": "lima"
      },
      {
        "lemma": null,
        "tag": "DET",
        "text": "na"
      },
      {
        "lemma": null,
        "tag": "PROPN",
        "text": "cuf"
      },
      {
        "lemma": null,
        "tag": "PROPN",
        "text": "porto"
      }
    ]
  }
}
```

You can find all named entities appended on property *ents*

It's also supported GET requests to visualize all detected named entities using displacy from Spacy. You can send desired GET request either via Postman/Insomnia app or directly on your browser. The following GET request allows you to see all named entities detected on "eu quero marcar uma consulta de cardiologia para o dr jorge lima na cuf porto" with model "sm" (small spacy dataset) and with language "pt" (portuguese),

## Get Request

http://127.0.0.1:50002/classify?model=sm&language=pt&utterance=eu%20quero%20marcar%20uma%20consulta%20de%20cardiologia%20para%20o%20dr%20jorge%20lima%20na%20cuf%20porto

## Get Response

The following image depicts the respective result,

![Alt text](example/Spacy-Visualizer.png?raw=true "Spacy Visualizer")

# Documentation and Related Information

* [Go to the Spacy Web Site to see all available models](https://spacy.io/models/)
* [Go to the Spacy Web Site to see all available visualizers](https://spacy.io/usage/visualizers)
* [Go to the Spacy Web Site to see all built-in entity types](https://spacy.io/api/annotation#named-entities)
* [Go to the Flask Web Site to see available documentation regarding Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Get Insomnia app](https://insomnia.rest/)
* [Get Postman app](https://www.postman.com/)