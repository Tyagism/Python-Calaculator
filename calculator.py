def cal(pi=3.1415):
    dash = "-" * 300
    arrow = "->"* 35
    thinking_face = "🤔" * 5
    sad_face = ":(" *6
    emojii = "😆" *100
    print(f"{dash}\nThis is a simple calculator program.")  
    while True:
        choices = [1, 2, 3, 4, 5, 6]
        print(f"{dash}{dash}\n\nChoose the operation you want to perform:", choices)
        print("Your Choice\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Area of Circle\n6. Exit\nEnter 1-6: \n")

        # Get a valid menu choice
        while True:
            try:
                user = int(input())
            except ValueError:
                print("Invalid input. Enter an integer 1-6.")
                continue
            if user in choices:
                break
            print("Please enter a choice between 1 and 6.")

        if user == 5:
            try:
                r = float(input("Enter the radius: "))
            except ValueError:
                print("Invalid radius. Please enter a number.")
                continue
            # Area of a circle: A = π r^2
            area = pi * r * r
            print(f"{arrow}\n        Calculation of Area of Circle is: {area}   \n{arrow}")
            continue
        if user == 6:
            print(f"Exiting the calculator. Goodbye!!! {sad_face}")
            break

        # Otherwise get two numbers
        try:
            x = float(input(f"{thinking_face}    Enter the first number: "))
            y = float(input(f"{thinking_face}    Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if user == 1:
            print(f"{arrow}\n     Result: {x + y}     \n{arrow}")
        elif user == 2:
            print(f"{arrow}\n     Result: {x - y}     \n{arrow}")
        elif user == 3:
            print(f"{arrow}\n     Result: {x * y}     \n{arrow}")
        elif user == 4:
            if y == 0:
                print(f"Cannot divide by zero. LOL !!!\n{emojii}")
            else:
                print(f"{arrow}\n     Result: {x / y}     \n{arrow}")

if __name__ == '__main__':
    cal()