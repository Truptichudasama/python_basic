#intializing two numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter ssecond number: "))
#various mathematical opertion
addition = number1 + number2
subtract = number1 - number2
mulitiplication = number1 * number2
if number2 != 0 :
    division = number1 / number2
else:
    division = "Division by 0 is not possible."
#print result of opertions.
print("Addition: " , addition)
print("subtraction: ", subtract)
print("Multiplication: ", mulitiplication)
print("Division: ", division)
