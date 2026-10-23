secret_number = 12
attempts = 0
guessed_correctly = False

while attempts < 5 and guessed_correctly == False:
    guess = input("Guess a number (1 to 20): ")

    if guess.isdigit():
        guess_val = int(guess)

        if guess_val < 1 or guess_val > 20:
            print("The correct range is 1 to 20.")
        else:
            attempts += 1

            if guess_val == secret_number:
                print("Hao, CORRECT!")
                guessed_correctly = True
            elif guess_val < secret_number:
                print("Too low!")
            else:
                print("Too high!")
    else:
        print("Invalid input. Please enter a whole number.")

if guessed_correctly == False:
    print(f"Failed to guess. The secret number is {secret_number}.")