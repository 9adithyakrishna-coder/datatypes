#Take input
print("half pyramid pattern of stars (*):")
n = int(input("enter the numbers of rows: "))
#outer loop to handle number of columns
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display results
        print("* ", end="")
    print()