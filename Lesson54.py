def calculate_change(cost, paid):
    if paid < cost:
        print("Not enough money paid.")
    else:
        change = paid - cost
        print(f"Return amount: ${change:.2f}")


# Example
cost = 2.50
paid = 4.00

calculate_change(cost, paid)