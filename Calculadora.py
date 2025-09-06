print("Hello World")

operator = input("ESCOLHA ENTRE (+ - * /): ")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Agora digite o segundo numero: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} não e valido!")