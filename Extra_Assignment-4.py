# Create a class and function, and list out the items in the list
class SubfieldsInAI:
    @staticmethod
    def Subfields():
        return [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
subfields = SubfieldsInAI.Subfields()
for field in subfields:
    print(field)

# Create a function that checks whether the given number is Odd or Even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    # Example usage
    print(int(input("Enter a number: ")))

# Create a function that checks whether the given number is Odd or even.
class OddEven:
    @staticmethod
    def OddEven(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
num = int(input("Enter a number: "))
result = OddEven.OddEven(num)
print(f"{num} is {result} number")

# Create a class for Marriage Eligibility
class MarriageEligibility:
    @staticmethod
    def check_eligibility(age, gender):
        if gender.lower() == "male":
            return age >= 21
        elif gender.lower() == "female":
            return age >= 18
        else:
            return False  # In case gender is neither male nor female
age = int(input("Your age: "))
gender = input("Your gender (male/female): ")
if MarriageEligibility.check_eligibility(age, gender):
    print("Your age: ",age)
    print("Your gender : ",gender)
    print("You are eligible for marriage.")
else:
    print("You are not eligible for marriage.")


from numpy import printoptions
class Find_Percent:
    @staticmethod
    def percentage():
        marks = []
        for i in range(1, 6):
            mark = int(input(f"Enter subject {i} marks: "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100")
                return
            marks.append(mark)

        total_marks = 500
        marks_obtained = sum(marks)
        percent = (marks_obtained / total_marks) * 100
        print(f"\nSubject1={marks[0]}, \nSubject2={marks[1]}, \nSubject3={marks[2]}, \nSubject4={marks[3]}, \nSubject5={marks[4]}.")
        print(f"\nTotal Marks Obtained: {marks_obtained}/500")
        print(f"Percentage: {percent:.2f}%")

Find_Percent.percentage()
#triangle.triangle()
class Triangle:
    def triangle(self):
        Height = 32
        Breadth = 34
        print("Height:", Height)
        print("Breadth:", Breadth)
        print("Area formula: (Height*Breadth)/2")
        Area = (Height * Breadth) / 2
        print("Area of Triangle:", Area)
        
        Height1 = 2
        Height2 = 4
        Breadth = 4
        print("Height1:", Height1)
        print("Height2:", Height2)
        print("Breadth:", Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1 + Height2 + Breadth
        print("Perimeter of Triangle:", Perimeter)

# Usage
t = Triangle()
t.triangle()
