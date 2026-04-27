def check_output(output):
    banned_words = ["hate", "stupid", "idiot"]

    for word in banned_words:
        if word in output.lower():
            return False

    return True