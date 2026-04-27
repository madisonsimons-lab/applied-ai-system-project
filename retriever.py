def load_data(file_path):
    with open(file_path, "r") as f:
        return f.readlines()

def retrieve_relevant(user_input, templates):
    user_input = user_input.lower()

    for t in templates:
        if "late" in user_input or "missing" in user_input:
            if "apologize" in t.lower():
                return t.strip()

    return templates[0].strip()