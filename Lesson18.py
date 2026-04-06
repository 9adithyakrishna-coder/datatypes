# Given numbers
a = 12
b = 5
c = 9

print("Original numbers:", a, b, c)

# Step 1: Compare a and b
if a > b:
    a, b = b, a
    print("After Step 1 (swap a and b):", a, b, c)

# Step 2: Compare b and c
if b > c:
    b, c = c, b
    print("After Step 2 (swap b and c):", a, b, c)

# Step 3: Compare a and b again
if a > b:
    a, b = b, a
    print("After Step 3 (swap a and b):", a, b, c)

print("Final sorted numbers:", a, b, c)