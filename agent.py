def determine_tone(user_input):
    user_input = user_input.lower()

    if "professor" in user_input:
        return "formal"
    elif "internship" in user_input:
        return "professional"
    return "neutral"


def generate_output(user_input, context, tone):
    prompt = f"""
You are a professional academic assistant.

Example:
Input: Email professor about missing assignment
Output: Dear Professor, I sincerely apologize...

Input: Follow up internship
Output: Hello, I hope you're doing well...

Now respond:

Input: {user_input}
Context: {context}
Tone: {tone}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


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


def classify_input(user_input):
    if "professor" in user_input.lower():
        return "academic_email"
    elif "internship" in user_input.lower():
        return "professional_email"
    return "general"

def run_agent_steps(user_input, template, tone):
    steps = {}

    steps["plan"] = f"Identify tone: {tone}, Use template: yes"

    draft = generate_output(user_input, template, tone)
    steps["draft"] = draft

    critique = critique_output(draft)
    steps["critique"] = critique

    final = refine_output(draft, critique)
    steps["final"] = final

    return steps