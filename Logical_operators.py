# logical operators = used on conditional statements

#             and = checks tho or more conditions if True
#              or = checks if at least one condition is True
#             not = True if condition is False, and vice versa

temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The Temperature is bad!")
else:
    print("The Temperature is good!")

if not sunny:
    print("It is cloudy outside!")
else:
    print("It is sunny outside!")