import spacy
import os
from spacy.cli import download

MODEL_NAME = "en_core_web_sm"
MODEL_PATH_FLAG = f"./{MODEL_NAME}_downloaded.txt"

# Only download if not already downloaded
if not os.path.exists(MODEL_PATH_FLAG):
    try:
        download(MODEL_NAME)
        with open(MODEL_PATH_FLAG, "w") as f:
            f.write("downloaded")
    except Exception as e:
        print(f"Failed to download spaCy model: {e}")

# Now load the model
nlp = spacy.load(MODEL_NAME)

def evaluate_formality(text):
    doc = nlp(text)
    score = sum(token.is_stop for token in doc) / len(doc)
    return round(score * 100, 2)

def rewrite_resume(text):
    doc = nlp(text)
    return " ".join([sent.text.capitalize() for sent in doc.sents])
