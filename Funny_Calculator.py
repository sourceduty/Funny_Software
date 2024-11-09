import random

def funny_calculator():
    print("Welcome to the Funny Calculator! 🤪")
    print("Where numbers meet jokes, and math makes you giggle!")
    print("--------------------------------------------------")
    
    while True:
        print("\nWhat would you like to do? Pick an option:")
        print("1. Add (+) \n2. Subtract (-) \n3. Multiply (*) \n4. Divide (/) \n5. Surprise Me! 🎉 \n6. Exit (💨)")
        choice = input("Enter the number of your choice: ")

        if choice == '6':
            print("Thanks for using the Funny Calculator! Stay quirky! ✌️")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Uh-oh! Invalid choice. Did you trip over the keyboard? Try again!")
            continue
        
        if choice == '5':
            joke = [
                "Why did the student eat his math homework? Because the teacher said it was a piece of cake! 🍰",
                "Why was the equal sign so humble? It knew it wasn't less than or greater than anyone else. 😌",
                "I told my calculator a joke… now it’s dividing its sides laughing! 😂",
                "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them! 😅"
            ]
            print(random.choice(joke))
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"Adding them up... It’s {result}. Sweet as a donut! 🍩")
            elif choice == '2':
                result = num1 - num2
                print(f"Subtracting... Boom! {result}. Like taking candy from a calculator. 🍬")
            elif choice == '3':
                result = num1 * num2
                print(f"Multiplying... and voila! {result}. That’s a lot of cookies! 🍪")
            elif choice == '4':
                if num2 == 0:
                    print("Dividing by zero? Bold move, Einstein! Here’s infinity instead: ♾️")
                else:
                    result = num1 / num2
                    print(f"Dividing... Your answer is {result}. That’s smooth like butter. 🧈")
        except ValueError:
            print("Oops! That’s not a number. Are you typing with your elbows? Try again! 🤷")

# Run the funny calculator
if __name__ == "__main__":
    funny_calculator()
