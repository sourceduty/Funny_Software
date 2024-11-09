import random
import time

def stoner_math(a, b):
    """Performs addition but with a twist."""
    forgetfulness_tax = random.choice([-1, 0, 0, 1])  # Randomly adjusts the result
    result = a + b + forgetfulness_tax
    commentary = random.choice([
        "Whoa, I think that's right... or close enough.",
        "Wait, was it 10? No, yeah, that's it.",
        "Math is hard when you're this chill, dude."
    ])
    print(f"The result is {result}. {commentary}")
    return result

def edible_dosage(thc_content, servings):
    """Calculates the approximate THC per serving."""
    thc_per_serving = thc_content / servings
    commentary = random.choice([
        "This batch might make you think your couch is a spaceship.",
        "Careful, this could knock out a walrus. Or you. Probably both.",
        "Perfect for a chill night... or an existential crisis."
    ])
    print(f"Each serving has about {thc_per_serving:.2f} mg of THC. {commentary}")
    return thc_per_serving

def stash_check(stash_size, daily_use):
    """Calculates how many days your stash will last."""
    days = stash_size / daily_use
    commentary = random.choice([
        "Better start texting your dealer now, just in case.",
        "You're good for a while. Enjoy the vibes!",
        "Time to consider growing your own supply, maybe?"
    ])
    print(f"Your stash will last approximately {days:.1f} days. {commentary}")
    return days

def surprise_message():
    """Outputs a random stoner fact or joke."""
    messages = [
        "Fun fact: Weed was once a required crop for farmers in Virginia!",
        "Bob Marley would be proud of your chill math skills.",
        "Why did the stoner become a baker? Because he was already high on dough!"
    ]
    print(random.choice(messages))

# Main menu
def weed_calculator():
    print("Welcome to the Funny Weed Calculator 🌿")
    print("Choose an option:")
    print("1. Stoner Math (Addition with a twist)")
    print("2. Edible Dosage Calculator")
    print("3. Stash Check")
    print("4. Surprise Message")
    print("5. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                stoner_math(a, b)
            elif choice == 2:
                thc = float(input("Enter total THC content in mg: "))
                servings = int(input("Enter number of servings: "))
                edible_dosage(thc, servings)
            elif choice == 3:
                stash = float(input("Enter your stash size in grams: "))
                daily = float(input("Enter your daily consumption in grams: "))
                stash_check(stash, daily)
            elif choice == 4:
                surprise_message()
            elif choice == 5:
                print("Catch you later, dude! Stay chill. 🌈")
                break
            else:
                print("Invalid choice. Try again!")
        except ValueError:
            print("Whoa, dude. Numbers only, please.")

# Run the calculator
if __name__ == "__main__":
    weed_calculator()
