def evaluate(output):
    score = 0

    if "apologize" in output.lower():
        score += 1

    if len(output) > 100:
        score += 1

    return {
        "score": score,
        "length": len(output)
    }
def confidence_score(output):
    score = 0

    if len(output) > 100:
        score += 1
    if "I recommend" in output:
        score += 1
    if "sincerely" in output.lower():
        score += 1

    return {
        "confidence": score / 3
    }