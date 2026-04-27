from main import run_system

test_cases = [
    "Email professor about missing assignment",
    "Follow up internship application",
    "Ask TA for help",
    "Request extension on deadline"
]

results = []

for test in test_cases:
    output, eval_data = run_system(test)

    results.append({
        "input": test,
        "score": eval_data["score"],
        "length": eval_data["length"]
    })

print("\n=== TEST SUMMARY ===")
for r in results:
    print(r)

avg_score = sum(r["score"] for r in results) / len(results)

print("\nAVERAGE SCORE:", avg_score)