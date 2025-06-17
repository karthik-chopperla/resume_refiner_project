# model.py
import re

# Dummy list of informal words for simple formality check
INFORMAL_WORDS = [
    "stuff", "cool", "awesome", "gotta", "wanna", "kinda", "sorta", "ya", "dude", "bro", "okay"
]

def evaluate_formality(text):
    """Check how many informal words appear."""
    words = re.findall(r'\b\w+\b', text.lower())
    informal_found = [word for word in words if word in INFORMAL_WORDS]
    score = 1 - (len(informal_found) / max(len(words), 1))
    return round(score, 2)

def rewrite_resume(text):
    """Simple rewrite: replace informal words with formal alternatives."""
    replacements = {
        "stuff": "items",
        "cool": "impressive",
        "awesome": "excellent",
        "gotta": "have to",
        "wanna": "want to",
        "kinda": "somewhat",
        "sorta": "approximately",
        "ya": "you",
        "dude": "person",
        "bro": "colleague",
        "okay": "acceptable"
    }
    pattern = re.compile(r'\b(' + '|'.join(replacements.keys()) + r')\b', flags=re.IGNORECASE)

    def replace(match):
        word = match.group(0)
        return replacements.get(word.lower(), word)

    return pattern.sub(replace, text)
