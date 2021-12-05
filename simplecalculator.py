
num_1 = float(input(" Input your first number: "))
op = input(" select a mathematical operator:")
num_2 = float(input(" Input your second number: "))
result = 0

if op == "+":
    result = num_1 + num_2
elif op == "-":
    result = num_1 - num_2
elif op == "/":
    result = num_1 / num_2
elif op == "*":
    result = num_1 * num_2

print("result = ", + result)
yes_no = (input(" do you want to do another? yes or no: "))

if yes_no == "yes":
    while yes_no == "yes":
        num_1 = float(input(" Input your first number: "))
        op = input(" select a mathematical operator:")
        num_2 = float(input(" Input your second number: "))

        if op == "+":
            result = num_1 + num_2
        elif op == "-":
            result = num_1 - num_2
        elif op == "/":
            result = num_1 / num_2
        elif op == "*":
            result = num_1 * num_2

        print("result = ", + result)
        yes_no = (input(" do you want to do another? yes or no: "))
    else:
        print("Thanks for using me! goodbye!")
