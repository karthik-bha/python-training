raise RuntimeError("Testing runtime error")
num1 = float(input())
num2 = float(input())
operator = input()

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    raise ValueError("Invalid operator")
# going to trigger a eval