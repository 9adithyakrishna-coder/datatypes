try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    else:
        print("Age entered correctly!")
        if age % 2 == 0:
            print("your age is even.")
        else:
            print("your age is odd.")
except ValueError as e:
    print("invalid input:", e)
except Exception:
    print("An unexpected error occured.")