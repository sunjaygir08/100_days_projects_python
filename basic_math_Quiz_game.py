#Basic Maths Quiz Game
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Division by zero is not allowed. Generating a new question.")
            return generate_question()
        answer = num1 / num2
    return f"{num1} {operator} {num2}", answer

def math_quiz():
    score = 0
    print("Welcome to the Basic Maths Quiz Game!")
    print("you will present with maths questions, answer them correctly to score points.")
    round = int(input("Enter the number of rounds you want to play: "))
    if round <= 0:
        print("Please enter a valid number of rounds.")
        return
    for i in range(round):  
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        # Accept float input for division, otherwise in int
        if '/' in question:
            user_answer = float(input("Your answer: "))
        else:
            user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    print("\n ----- Game Over -----")
    print(f"Your final score is {score} out of {round}.")
    if score == round:
        print("Congratulations! You are a Maths Genius!")
    elif score >= round // 2:
        print("Good job! You have a solid understanding of basic maths.")
    else:
        print("Keep practicing! You can improve your maths skills.")

math_quiz()