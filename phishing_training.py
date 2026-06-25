import json

print("\nPHISHING AWARENESS TRAINING\n")

print("1. Never share passwords.")
print("2. Verify URLs before login.")
print("3. Avoid clicking suspicious links.")
print("4. Check sender email carefully.")
print("5. Enable Two Factor Authentication.\n")

with open("phishing_quiz.json", "r") as file:
    questions = json.load(file)

score = 0

for item in questions:
    print(item["question"])
    user_answer = input("Answer (yes/no): ").lower()

    if user_answer == item["answer"]:
        score += 1

print(f"\nQuiz Score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent Awareness!")
elif score >= 2:
    print("Good Awareness!")
else:
    print("Need More Training!")