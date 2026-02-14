import random
lowest = 1
highest = 100
answer = random.randint(lowest, highest)
is_correct = False
count = 0
print(*"******************************")
print("Welcome to the Guess the Number Game!")
print("want to Try Your Luck! today?")
print(f"I'm thinking of a number between {lowest} and {highest}. Can you guess it?")
print(*"******************************")
while not is_correct:
    user_input = input("Enter your Number: ").strip()
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid integer.")
        continue
    guess = int(user_input)
    if guess < lowest or guess > highest:
        print(f"Please enter a number between {lowest} and {highest}.")
        continue
    count += 1
    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(("******************************"))
        print(f"Congratulations! You've guessed the number correctly!")
        print(f"The correct number was: {answer}")
        print(f"It took you {count} attempts to guess the number.")
        print(("******************************"))
        is_correct = True