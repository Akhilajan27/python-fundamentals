questions = [
    {
        "prompt" : "Which country was the first to land a man on the moon?",
        "options" : ["A) Soviet Union","B) United States","C) China","D) France"],
        "answer" : "B"
    },
    {
        "prompt" : "Who was the first female Prime Minister in the world?",
        "options" : ["A) Indira Gandhi","B) Margaret Thatcher","C) Sirimavo Bandaranaike","D) Golda Meir"],
        "answer" : "C"
    },
    {
        "prompt" : "What is the smallest prime number ?",
        "options" : ["A) 1","B) 2","C) 3","D) 5"],
        "answer" : "B"
    },
    {
        "prompt" : "Which is the largest country in the world by area?",
        "options" : ["A) Canada","B) United States","C) China","D) Russia"],
        "answer" : "D"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C or D):").upper()
        if answer == question["answer"]:
            print("correct")
            score +=1
        else:
            print("Wrong ! The correct answer was ", question["answer"],"\n")
    print(f"you got {score} out of {len(questions)} correct.")

run_quiz(questions)