#my mini quize project 
# Quiz Game in Python

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        try:
            answer = int(input("Enter your choice (1-4): "))
            if q["options"][answer - 1].lower() == q["answer"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("⚠ Invalid input, skipping this question!")

    print(f"\nYour final score: {score}/{len(questions)}")

# Questions for quiz
quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which of these is not an operating system?",
        "options": ["Windows", "Linux", "Oracle", "MacOS"],
        "answer": "Oracle"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", 
                    "Hyper Text Marketing Language", "High Text Machine Language"],
        "answer": "Hyper Text Markup Language"
    }
]

# Run the quiz
print("🎮 Welcome to the Python Quiz Game! 🎮")
run_quiz(quiz_questions)
print("Thanks for playing!")

