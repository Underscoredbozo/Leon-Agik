print("Handmade Calculator")
num1 = int(input())
num2 = int(input())
opperation = input()
if opperation =="+":
    print(num1 + num2)
elif opperation == "-":
    print(num1 - num2)
elif opperation == "*":
    print(num1 * num2)
elif opperation == "/":
    print(num1 / num2)
else:
    print("Invalid opperation")
