import datetime
from retriever import load_data, retrieve_relevant
from agent import determine_tone, generate_output, critique_output, refine_output
from guardrails import check_output
from evaluator import evaluate


def log_run(user_input, output, evaluation):
    with open("logs/run_log.txt", "a") as f:
        f.write(f"\n--- {datetime.datetime.now()} ---\n")
        f.write(f"INPUT: {user_input}\n")
        f.write(f"OUTPUT: {output}\n")
        f.write(f"EVAL: {evaluation}\n")
        f.write(f"CLASS: N/A\n")
        f.write(f"CONFIDENCE: {evaluation.get('confidence', 'N/A')}\n")

def run_system(user_input):
    from retriever import load_all_data

    templates = load_all_data()

    # Retrieval (RAG)
    template = retrieve_relevant(user_input, templates)

    # Reasoning
    tone = determine_tone(user_input)

    # Agent Workflow
    output = generate_output(user_input, template, tone)

    for _ in range(2):
        issues = critique_output(output)
        if not issues:
            break
        output = refine_output(output, issues)

    # Guardrails
    if not check_output(output):
        output = "Output blocked due to unsafe content."

    # Evaluation
    evaluation = evaluate(output)

    # Logging
    log_run(user_input, output, evaluation)

    return output, evaluation


if __name__ == "__main__":
    test_inputs = [
        "Write an email to my professor about missing an assignment",
        "Follow up on internship application",
        "Ask for clarification on homework",
        "Email professor about missing assignment",
        "Email professor asking for extension",
        "Follow up internship application",
        "Ask TA for clarification",
        "Write professional apology email"
    ]

    for inp in test_inputs:
        print("\n==========================")
        print("INPUT:", inp)
        output, eval_data = run_system(inp)
        print("OUTPUT:\n", output)
        print("EVAL:", eval_data)
