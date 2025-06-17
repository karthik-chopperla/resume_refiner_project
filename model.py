import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def evaluate_formality(text):
    informal_words = set(["cool", "okay", "ok", "awesome", "stuff", "things", "a lot", "kinda", "gonna"])
    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalpha() and w not in stopwords.words('english')]
    if not words:
        return 0.0
    informal_count = sum(1 for w in words if w in informal_words)
    score = 1 - informal_count / len(words)
    return max(0.0, min(1.0, score))

def rewrite_resume(text):
    replacements = {
        "okay": "acceptable",
        "ok": "satisfactory",
        "cool": "impressive",
        "stuff": "materials",
        "things": "items",
        "a lot": "many",
        "kinda": "somewhat",
        "gonna": "going to",
        "awesome": "outstanding"
    }
    for informal, formal in replacements.items():
        text = re.sub(rf"\b{informal}\b", formal, text, flags=re.IGNORECASE)
    return text