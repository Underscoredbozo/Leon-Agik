print("Handmade Calculator")
num1 = float(input())
num2 = float(input())
opperation = input()
if opperation =="+":
    print(num1 + num2)
elif opperation == "-":
    print(num1 - num2 )
elif opperation == "*":
    print(num1 * num2)
elif opperation == "/":
    print(num1 / num2)
else:
    print("Invalid opperation")
