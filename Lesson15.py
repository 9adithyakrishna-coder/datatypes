a = 5   # binary: 0101

b = 3   # binary: 0011


print(a & b)   # AND: 0101 & 0011 = 0001 = 1

print(a | b)   # OR: 0101 | 0011 = 0111 = 7

print(a ^ b)   # XOR: 0101 ^ 0011 = 0110 = 6

print(~b)      # NOT: flips all bits of 3 = -4

print(a << b)  # left shift: 5 shifted left by 3 = 40

print(a >> b)  # right shift: 5 shifted right by 3 = 0
