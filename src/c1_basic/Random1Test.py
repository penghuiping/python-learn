import random

digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

print(random.randint(100, 200))

combine = digit + lower + upper
print(combine)

result = ""
for tmp in range(20):
    i = random.randint(0, len(combine)-1)
    result += combine[i]
print(result)


