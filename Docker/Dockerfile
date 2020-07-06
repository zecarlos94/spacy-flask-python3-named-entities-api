FROM python:3.7

# Copy the app
COPY /app /app
WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python3 -m spacy download en_core_web_sm 
RUN python3 -m spacy download en_core_web_md 
RUN python3 -m spacy download en_core_web_lg 
RUN python3 -m spacy download pt_core_news_sm
RUN python3 -m spacy download pt_core_news_md
RUN python3 -m spacy download pt_core_news_lg

# Bind docker localhost to external source localhost
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]