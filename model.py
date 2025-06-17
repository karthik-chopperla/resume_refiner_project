import spacy

nlp = spacy.load("en_core_web_sm")

def evaluate_formality(text):
    doc = nlp(text)
    long_sentences = sum(1 for sent in doc.sents if len(sent.text.split()) > 20)
    contractions = sum(1 for token in doc if token.text.lower() in ["don't", "can't", "won't", "isn't"])
    passive_voice = sum(1 for token in doc if token.dep_ == "auxpass")
    
    score = 100
    score -= long_sentences * 5
    score -= contractions * 10
    score -= passive_voice * 7
    score = max(score, 0)
    
    return score, {
        "long_sentences": long_sentences,
        "contractions": contractions,
        "passive_voice": passive_voice
    }

def rewrite_resume(text):
    doc = nlp(text)
    rewritten = []

    for sent in doc.sents:
        new_sent = sent.text

        # Replace contractions
        contractions_map = {
            "don't": "do not", "can't": "cannot", "won't": "will not", "isn't": "is not"
        }
        for k, v in contractions_map.items():
            new_sent = new_sent.replace(k, v)

        # Simplify passive voice (rudimentary)
        if "was" in new_sent and "by" in new_sent:
            new_sent = new_sent.replace("was", "").replace("by", "")
            new_sent = "Consider rewriting this in active voice: " + new_sent.strip()

        rewritten.append(new_sent)

    return " ".join(rewritten)
