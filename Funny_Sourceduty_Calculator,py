import random

def sourceduty_calculator():
    print("Welcome to the Sourceduty Calculator! Let’s measure your coding sins. 😈\n")

    # User Inputs
    print("1. How many lines of code have you 'borrowed'?\n")
    print("   a) 0 - I’m original, like a blank Word doc")
    print("   b) 1-50 - Just a light sprinkle from Stack Overflow")
    print("   c) 51-200 - I forked and prospered")
    print("   d) 201+ - I am the Frankenstein of open source")
    borrowed_input = input("Enter your choice (a/b/c/d): ").lower()

    borrowed_lines = {"a": 0, "b": 50, "c": 200, "d": 500}.get(borrowed_input, 50)

    print("\n2. How many bugs are lurking in your code?\n")
    bug_count = int(input("Enter the number of bugs you know about (be honest, no judgment!): "))

    print("\n3. How many hours have you spent debugging?\n")
    debug_hours = int(input("Enter the number of hours spent debugging (including existential crises): "))

    print("\n4. How many cups of coffee/tea have you consumed?\n")
    coffee_count = int(input("Enter the number of caffeinated drinks consumed while coding: "))

    # Calculations
    karma_debt = borrowed_lines * 0.5  # Each line "borrowed" adds to your karma debt
    bug_to_caffeine_ratio = bug_count / max(coffee_count, 1)  # Avoid division by zero
    sourceduty_score = (bug_count * debug_hours) + karma_debt  # A weighted total score

    # Fun commentary based on score
    if sourceduty_score < 100:
        level = "Coding Angel 😇"
        comment = "Your code is pristine, like freshly formatted Python!"
    elif 100 <= sourceduty_score < 500:
        level = "Casual Borrower 🧑‍💻"
        comment = "Your code is decent, but that Stack Overflow history tho..."
    else:
        level = "Summoned the Debugging Demon 😈"
        comment = "Your code is held together by dreams and duct tape. Sleep?"

    # Results
    print("\n--- Sourceduty Calculator Results ---")
    print(f"Open-Source Karma Debt: {karma_debt:.2f}")
    print(f"Bug-to-Caffeine Ratio: {bug_to_caffeine_ratio:.2f} bugs per caffeinated drink")
    print(f"Total Sourceduty Score: {sourceduty_score:.2f}")
    print(f"Level: {level}")
    print(f"Comment: {comment}")

    # Random Meme/Quote
    quotes = [
        "Debugging is like being the detective of a crime you committed.",
        "There’s no such thing as a bug-free code. Only a developer-free blame.",
        "Your code doesn’t run? Congrats, it’s a feature now."
    ]
    print(f"\nRandom Motivation: {random.choice(quotes)}")

# Run the calculator
if __name__ == "__main__":
    sourceduty_calculator()
