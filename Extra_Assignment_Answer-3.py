# print 'CORRECT' if i == 10
i = 10
if i == 10:
    for i in range(0, 21):
        value = i
        if value == 10:  # Check inside loop
            print('CORRECT')

# Check the password, using if and else
password = "HOPE@123"
if password == "HOPE@123":
    print("Your password is correct")
else:
    print("Your password is incorrect")

# Catagory the people by their age like children, adult, citizen, senior citizen...
age= 20
result = "if, elif, elif, else"
if age < 13:
    result = "Children"
elif age < 18:
    result = "Teenager"
elif age < 60:
    result = "Adult"
else:
    result = "Senior Citizen"
print(result)

# Find whether given number is positive or negative
num = int(input("Enter any number:"))
if num > 0:
    print("No is positive")
elif num < 0:
    print("No is negative")
else:
    print("No is zero")

# Check whether the given number is divisible by 5

num = int(input("Enter a number to check:"))
if num % 5 == 0:
    print("No is divisible by 5")
else:
    print("No is not divisible by 5")
