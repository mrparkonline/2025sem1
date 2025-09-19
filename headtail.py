# Head or Tails

from random import choice # choice is a function that randomly chooses from a list

while True:
    print("Welcome to our heads or tails game!")
    print("Please choose either heads or tails.")
    while True:
        user_input = input("User's choice: ")
        user_input = user_input.lower()
        if user_input in {"heads", "tails", "head", "tail"}:
            break
        else:
            print("please type in heads or tails. :)")
    flip_result = choice(["heads", "tails"])
    print(f"The computer flipped: {flip_result}.")
    if user_input in {"heads", "head"} and flip_result == "heads":
        print("The user guessed correctly!")
    elif user_input in {"tails", "tail"} and flip_result == "tails":
        print("The user guessed correctly!")
    else:
        print("HAHA YOU LOST BOZO!")
    user_input = input("Want to exit?: Yes/no: ")
    if user_input.lower() == "yes":
        break