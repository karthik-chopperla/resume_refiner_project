import spacy

nlp = spacy.load("en_core_web_sm")

def evaluate_formality(text):
    doc = nlp(text)
    score = sum(token.is_stop for token in doc) / len(doc)
    return round(score * 100, 2)

def rewrite_resume(text):
    doc = nlp(text)
    return " ".join([sent.text.capitalize() for sent in doc.sents])
