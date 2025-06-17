def text_diff(original, revised):
    original_lines = original.split(". ")
    revised_lines = revised.split(". ")

    diffs = []
    for i, (orig, rev) in enumerate(zip(original_lines, revised_lines)):
        if orig.strip() != rev.strip():
            diffs.append(f"🔄 Sentence {i+1} changed:\n📝 Before: {orig.strip()}\n✅ After: {rev.strip()}")
    return "\n\n".join(diffs) if diffs else "✅ No major changes detected."
