first_num = int(input("Enter the value for first number: "))

second_num = int(input("Enter the value for second number: "))

operation = input("Choose math operation (+, -, *, /): ")

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)
else:
    print("You did not provide the correct math operation.")