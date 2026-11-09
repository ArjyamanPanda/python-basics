print("WELCOME TO KAUN BANEGA CROREPATI")

questions = [
    "What is the capital of India?",
    "Who is known as the Father of the Nation?",
    "Which planet is known as the Red Planet?",
    "How many days are there in a leap year?",
    "Which is the largest ocean in the world?"
]

options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Nehru", "B. Bhagat Singh", "C. Mahatma Gandhi", "D. Subhash Bose"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    ["A. 365", "B. 366", "C. 364", "D. 360"],
    ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"]
]

answers = ["B", "C", "B", "B", "D"]

prize = 0

for i in range(5):

    print("\nQuestion", i + 1)
    print(questions[i])

    for j in options[i]:
        print(j)

    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == answers[i]:
        print("Correct Answer!")
        prize = prize + 1000
        print("You won Rs.", prize)

    else:
        print("Wrong Answer!")
        print("Correct answer is:", answers[i])
        break

print("\nGAME OVER")
print("Your total prize money is Rs.", prize)
print("THANK YOU FOR PLAYING KBC!")