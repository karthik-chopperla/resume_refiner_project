import spacy
from spacy.cli import download

# Try loading spaCy model; download if missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def evaluate_formality(text):
    doc = nlp(text)
    score = sum(token.is_stop for token in doc) / len(doc)
    return round(score * 100, 2)

def rewrite_resume(text):
    doc = nlp(text)
    return " ".join([sent.text.capitalize() for sent in doc.sents])
