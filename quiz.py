questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which language is used to write web pages?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Control Power Unit", "C. Compute Power Unit", "D. Central Power Unit"],
        "answer": "A"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Elon Musk", "B. Bill Gates", "C. Guido van Rossum", "D. Dennis Ritchie"],
        "answer": "C"
    }
]

score = 0


for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer is {q['answer']}")


print(f"\n🎉 Quiz Completed! Your Score: {score}/{len(questions)}")
