import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

smallDataset  = os.environ.get("SMALL")
mediumDataset = os.environ.get("MEDIUM")
largeDataset  = os.environ.get("LARGE")

pt = os.environ.get("PORTUGUESE_LANG")
en = os.environ.get("ENGLISH_LANG")