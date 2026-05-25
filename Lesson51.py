try:
    num1, num2 = eval(input("Enter two numbers, separated by a coma : "))
    results = num1 / num2
    print("reult is", results)
#using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("coma is missing. Enter numbers separated by coma like this 1, 2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")