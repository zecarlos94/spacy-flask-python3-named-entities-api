python3 -m venv venv
. venv/bin/activate
pip3 install -U spacy
python3 -m spacy download en_core_web_sm 
python3 -m spacy download en_core_web_md 
python3 -m spacy download en_core_web_lg 
python3 -m spacy download pt_core_news_sm
python3 -m spacy download pt_core_news_md
python3 -m spacy download pt_core_news_lg
pip3 install Flask
pip3 install -U python-dotenv
python3 -m flask run