import random
lowest = 1
highest = 100
answer = random.randint(lowest, highest)
is_correct = False
print("Welcome to the Guess the Number Game!")
print("Try Your Luck!")
print(f"I'm thinking of a number between {lowest} and {highest}. Can you guess it?")
while not is_correct:
    user_input = input("Enter your Number: ").strip()
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid integer.")
        continue
    guess = int(user_input)
    if guess < lowest or guess > highest:
        print(f"Please enter a number between {lowest} and {highest}.")
        continue
    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(("******************************"))
        print(f"Congratulations! You've guessed the number correctly!")
        print(f"The correct number was: {answer}")
        print(("******************************"))
        is_correct = True