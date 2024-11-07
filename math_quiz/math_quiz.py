import random


def random_num(min, max):
    """
    input: min and max value of integer for each variable
    goal: generating a random integer for both variables
    """
    return random.randint(min, max)


def chose_operator():
    """
    randomly choses one operator, either multiplication, addition or subtraction
    """
    return random.choice(['+', '-', '*'])


def calculate_solution(num1, num2, operator):
    """
    input: operator and two numbers for calculation
    generate a string with the task that has to be solved
    check which operator was chosen in chose_operator with an if else statement
    and perform calculation to calculate the right answer
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': answer = num1 + num2
    elif operator == '-': answer = num1 - num2
    else: answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0 #counter for right answers
    number_exercises = 5 #number of exercises quiz taker has to solve

    print("Welcome to the Math Quiz Game!") #welcome message
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_exercises):
        num1 = random_num(1, 10); num2 = random_num(1, 5); operator = chose_operator()

        problem, answer = calculate_solution(num1, num2, operator)
        print(f"\nQuestion: {problem}") #print task

        while True: #get user input until user inputs an integer
            user_answer = input("Your answer: ") #get user input
            try:
                user_answer = int(user_answer) #check if user input is integer
                break
            except ValueError:
                print("That's not a number. Please try again.") #if not integer then print error

        if user_answer == answer: #if user input is correct add one to score
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{number_exercises}") #after 5 runs end game and show results

if __name__ == "__main__":
    math_quiz()
