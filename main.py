import datetime

# -----------------------------
# 📚 RETRIEVER (RAG)
# -----------------------------
def load_templates():
    return [
        "Dear Professor, I apologize for missing the deadline due to unforeseen circumstances...",
        "Hello, I hope you're doing well. I wanted to follow up regarding...",
        "Good morning, I am writing to ask for clarification about..."
    ]

def retrieve_relevant_template(user_input, templates):
    for t in templates:
        if "late" in user_input.lower() or "missing" in user_input.lower():
            return t
    return templates[0]


# -----------------------------
# 🧠 REASONING ENGINE
# -----------------------------
def determine_tone(user_input):
    if "professor" in user_input.lower():
        return "formal"
    elif "internship" in user_input.lower():
        return "professional"
    return "neutral"


# -----------------------------
# 🤖 GENERATION (SIMULATED LLM)
# -----------------------------
def generate_output(user_input, template, tone):
    return f"{template}\n\nRequest: {user_input}\n\nTone: {tone}"


# -----------------------------
# 🔍 SELF-CRITIQUE
# -----------------------------
def critique_output(output):
    issues = []
    if "apologize" not in output.lower():
        issues.append("Missing apology")
    if len(output) < 50:
        issues.append("Too short")
    return issues


# -----------------------------
# 🔁 REFINEMENT
# -----------------------------
def refine_output(output, issues):
    if "Missing apology" in issues:
        output = "I sincerely apologize.\n" + output
    if "Too short" in issues:
        output += "\nPlease let me know if any additional steps are required."
    return output


# -----------------------------
# 🚧 GUARDRAILS
# -----------------------------
def guardrails_check(output):
    banned_words = ["hate", "stupid"]
    for word in banned_words:
        if word in output.lower():
            return False
    return True


# -----------------------------
# 📊 EVALUATION
# -----------------------------
def evaluate_output(output):
    score = 0
    if "apologize" in output.lower():
        score += 1
    if len(output) > 80:
        score += 1
    return {
        "score": score,
        "length": len(output)
    }


# -----------------------------
# 📝 LOGGING
# -----------------------------
def log_run(user_input, output, evaluation):
    with open("run_log.txt", "a") as f:
        f.write(f"\n--- {datetime.datetime.now()} ---\n")
        f.write(f"INPUT: {user_input}\n")
        f.write(f"OUTPUT: {output}\n")
        f.write(f"EVAL: {evaluation}\n")


# -----------------------------
# 🚀 MAIN SYSTEM (PIPELINE)
# -----------------------------
def run_system(user_input):
    templates = load_templates()

    # Retrieval
    template = retrieve_relevant_template(user_input, templates)

    # Reasoning
    tone = determine_tone(user_input)

    # Agent Workflow
    output = generate_output(user_input, template, tone)

    for _ in range(2):  # limited refinement loop
        issues = critique_output(output)
        if not issues:
            break
        output = refine_output(output, issues)

    # Guardrails
    if not guardrails_check(output):
        output = "Output blocked due to unsafe content."

    # Evaluation
    evaluation = evaluate_output(output)

    # Logging
    log_run(user_input, output, evaluation)

    return output, evaluation


# -----------------------------
# 🧪 TEST CASES
# -----------------------------
if __name__ == "__main__":
    test_inputs = [
        "Write an email to my professor about missing an assignment",
        "Help me follow up on an internship",
        "Ask for clarification on homework"
    ]

    for inp in test_inputs:
        print("\n==============================")
        print(f"INPUT: {inp}")
        output, eval_data = run_system(inp)
        print("OUTPUT:\n", output)
        print("EVALUATION:", eval_data)