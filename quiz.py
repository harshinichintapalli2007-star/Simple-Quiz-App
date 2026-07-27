# Simple Quiz App

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for Python?",
        "options": ["A. HTML", "B. Java", "C. Python", "D. CSS"],
        "answer": "C"
    },
    {
        "question": "3. How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "5. What is 5 + 7?",
        "options": ["A. 10", "B. 12", "C. 13", "D. 14"],
        "answer": "B"
    }
]

score = 0

print("===== Welcome to the Quiz =====")

for q in questions:
    print()
    print(q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", q["answer"])

print("\n===== Quiz Finished =====")
print("Your Score:", score, "/", len(questions))
