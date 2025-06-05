# simple calculator using ladder statements

operator = input("Enter an operator(+,-,*,/):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter the second number:"))


# perform for calculation

if operator =='+':
    result = num1 + num2
    print(f"sum of {num1} + {num2} = {result}")

elif operator =='*':
    result = num1 * num2
    print(f"sum of {num1} * {num2} = {result}")

elif operator =='/':
    result = num1 / num2
    print(f"sum of {num1} / {num2} = {result}")

elif operator =='-':
    result = num1 - num2
    print(f"sum of {num1} - {num2} = {result}")
    
    

else:
    print("This operator is not found")
