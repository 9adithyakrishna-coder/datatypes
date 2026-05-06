def add(P, Q):
   # this function is used for adding two numbers
   return P + Q
def subtract(P, Q):
   # this function is used for subtracting two numbers
   return P - Q
def multiply(P, Q):
   # this function is used for multiplying two numbers
   return P * Q
def divide(P, Q):
   # this function is used for dividing two numbers
   return P / Q

# Now we will take inputs from user 
print ("please select the operation.")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d/): ")

num_1 = int (input ("Please enter the first number: "))
num_2 = int (input ("Please enter the second number: "))

if choice == 'a':
   print (num_1, " + ", num_2, "=", add(num_1, num_2))

elif choice == 'b':
   (num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
   (num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'd':
   (num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
   print ("this is an invalid input")