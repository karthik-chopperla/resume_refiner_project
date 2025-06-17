# model.py

from textblob import TextBlob

def evaluate_formality(text):
    informal_keywords = ["got", "stuff", "things", "a lot", "bunch", "cool", "okay", "ok", "yeah", "wanna", "gonna"]
    informal_count = sum(text.lower().count(word) for word in informal_keywords)
    total_words = len(text.split())
    score = max(0.0, 1.0 - (informal_count / total_words)) if total_words else 0
    return round(score, 2)

def rewrite_resume(text):
    blob = TextBlob(text)
    corrected = str(blob.correct())
    return corrected
