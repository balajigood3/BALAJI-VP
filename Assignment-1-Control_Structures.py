#print statement
print("Welcome to Assignment-1")

#arithmetic operations
Num1 = 10
Num2 = 30
print("Add =", Num1 + Num2)

# BMI Categorization
BMI = float(input("Enter the BMI Index: "))
if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal weight")
elif BMI < 36:
    print("Over Weight")
elif BMI < 41:
    print("Very Over Weight")
else:
    print("Obesity")