a = input("Input: ").split()
b = []
for i in a:
    if i not in b:
        b.append(i)
print("Output: ", b)