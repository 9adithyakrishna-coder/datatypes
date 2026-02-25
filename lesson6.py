# List of friends
friends = ["Aman", "Riya", "Karan", "Sneha", "Vikram"]

# Dictionary to store birthdays
birthdays = {}

# Collect birthdays
print("Raj: Hey friends! Can you all tell me your birthdays?\n")
birthdays = {
    "Aman": "12-03-2005",
    "Riya": "25-07-2004",
    "Karan": "09-11-2005",
    "Sneha": "18-01-2004",
    "Vikram": "30-09-2005"
}

# Print them
for name, birthday in birthdays.items():
    print(f"{name}'s birthday is on {birthday}")

# Print all birthdays
print("\nRaj: Let me read out all the birthdays:\n")
for name, birthday in birthdays.items():
    print(f"{name}'s birthday is on {birthday}")

# 🔎 Automatic Search Example
search_name = "Riya"
print(f"\nRaj is checking {search_name}'s birthday...\n")

if search_name in birthdays:
    print(f"My friend {search_name}'s birthday is on {birthdays[search_name]}")
else:
    print(f"Raj: Hmm... I don't have {search_name}'s birthday saved.")

# Final birthday list
print("\nRaj: Here is my final birthday list with dates:\n")
for name, birthday in birthdays.items():
    print(f"{name} → {birthday}")

   