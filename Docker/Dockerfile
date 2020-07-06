FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm 
RUN python3 -m spacy download en_core_web_md 
RUN python3 -m spacy download en_core_web_lg 
RUN python3 -m spacy download pt_core_news_sm
RUN python3 -m spacy download pt_core_news_md
RUN python3 -m spacy download pt_core_news_lg
CMD python3 -m flask run app.py