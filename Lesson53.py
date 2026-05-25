def shutdown(user_input):
    if user_input.lower() == "yes":
        print("Shutting down...")
    elif user_input.lower() == "no":
        print("Abort shutdown")
    else:
        print("Invalid input")


# Example usage
choice = input("Do you want to shutdown? (yes/no): ")
shutdown(choice)