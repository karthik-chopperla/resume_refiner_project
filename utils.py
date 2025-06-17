# utils.py
import difflib

def text_diff(original, rewritten):
    diff = difflib.ndiff(original.split(), rewritten.split())
    return ' '.join([
        f"🟥{word[2:]}" if word.startswith('- ') else
        f"🟩{word[2:]}" if word.startswith('+ ') else
        word[2:]
        for word in diff if not word.startswith('? ')
    ])
