def determine_tone(user_input):
    user_input = user_input.lower()

    if "professor" in user_input:
        return "formal"
    elif "internship" in user_input:
        return "professional"
    return "neutral"


def generate_output(user_input, template, tone):
    return f"{template}\n\nRequest: {user_input}\nTone: {tone}"


def critique_output(output):
    issues = []

    if "apologize" not in output.lower():
        issues.append("Missing apology")

    if len(output) < 80:
        issues.append("Too short")

    return issues


def refine_output(output, issues):
    if "Missing apology" in issues:
        output = "I sincerely apologize.\n" + output

    if "Too short" in issues:
        output += "\nPlease let me know if you need anything else."

    return output