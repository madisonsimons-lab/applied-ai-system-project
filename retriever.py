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

def load_all_data():
    files = [
        "data/email_templates.txt",
        "data/notes.txt",
        "data/tone_guidelines.txt"
    ]

    data = []
    for f in files:
        with open(f, "r") as file:
            data.extend(file.readlines())

    return data