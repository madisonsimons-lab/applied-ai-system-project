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