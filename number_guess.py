import random

leaderboard = []

#opening function
def print_instructions():
    print("\nWelcome to 'Guess the Number'!")
    print("Objective: Guess the randomly generated number within a specific range.")
    print("Try to guess the number in as fewest attempts as possible.")
    print("You’ll get helpful hints along the way!\n")

#difficulty selection
def get_difficulty_level():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard (1–100, 10 attempts)")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        return (1, 10, 5)
    elif choice == '2':
        return (1, 50, 7)
    elif choice == '3':
        return (1, 100, 10)
    else:
        print("Invalid choice. Defaulting to Medium.")
        return (1, 50, 7)

#custom range
def set_custom_range():
    while True:
        try:
            start = int(input("Enter the range starting point: "))
            end = int(input("Enter the range ending point: "))
            if start >= end:
                print("Start must be less than end.")
                continue
            attempts = int(input("Number of attempts: "))
            if attempts <= 0:
                print("Attempts must be a positive number.")
                continue
            return (start, end, attempts)
        except ValueError:
            print("Please enter valid integers.")

#leaderboard view
def view_leaderboard():
    if not leaderboard:
        print("\nLeaderboard is empty.\n")
        return
    print("\n🏆 Leaderboard:")
    for idx, entry in enumerate(sorted(leaderboard, key=lambda x: x['score'], reverse=True), start=1):
        print(f"{idx}. {entry['name']} - {entry['score']} points")
    print()

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

#hints
def provide_hint(number_to_guess, guess):
    hints = []
    hints.append("Even" if number_to_guess % 2 == 0 else "Odd")
    if guess != 0:
        if number_to_guess % guess == 0:
            hints.append(f"Divisible by your guess ({guess})")
        else:
            hints.append(f"Not divisible by your guess ({guess})")
    if is_prime(number_to_guess):
        hints.append("It's a prime number.")
    else:
        hints.append("It's not a prime number.")
    print("Hints:", ", ".join(hints))

#game
def play_round(start, end, max_attempts):
    number_to_guess = random.randint(start, end)
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess ({start} to {end}): "))
            if guess < start or guess > end:
                print(f"Please guess a number between {start} and {end}.")
                continue
            attempts += 1
            if guess == number_to_guess:
                print("🎉 Correct! You guessed the number.")
                score = (max_attempts - attempts + 1) * 10
                return score
            elif guess < number_to_guess:
                print("Too low.")
            else:
                print("Too high.")
            provide_hint(number_to_guess, guess)
        except ValueError:
            print("Please enter a valid number.")
    print(f"❌ You are out of attempts! The number was {number_to_guess}.")
    return 0

#menu
def settings_menu():
    while True:
        print("\n⚙️ Settings Menu:")
        print("1. Select Difficulty Level")
        print("2. Set Custom Range")
        print("3. View Leaderboard")
        print("4. Exit Settings")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            return get_difficulty_level()
        elif choice == '2':
            return set_custom_range()
        elif choice == '3':
            view_leaderboard()
        elif choice == '4':
            return None
        else:
            print("Invalid option. Try again.")

#game
def guess_the_number():
    print_instructions()
    settings = None
    while settings is None:
        settings = settings_menu()

    start, end, max_attempts = settings

    while True:
        name = input("\nEnter your name: ")
        score = play_round(start, end, max_attempts)
        leaderboard.append({"name": name, "score": score})
        print(f"{name}, your score this round: {score}\n")
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye!👋")
            break
        settings = settings_menu()
        if settings:
            start, end, max_attempts = settings

# game
if __name__ == "__main__":
    guess_the_number()
#by: Muhammad Shameer Asim