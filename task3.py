#1
age=int(input("enter your age in years. "))
height= int(input("enter your heigt in cm. "))
if age >= 12 and height >= 140:
    print("you can ride the roller coaster.")
else:
    print("you cannot ride the roller coaster.")

#2
color=input("enter any color. ")
colour={
    'red':'stop',
    'yellow':'wait',
    'green':'go'
}
if color.lower() in colour:
   print(colour[color])
else:
   print("invalid color")

#3
num=int(input("enter a number between 1-4. "))
season={
    1:'spring',
    2:'winter',
    3:'autumn',
    4:'summer'
}
if num in season:
    print(season[num])
else:
    print('invalid number')

#4
username=input("enter your username")
if username == 'admin':
    print("valid username.")
    password=input("enter your password")
    if password == 'pass123':
        print("valid password.")
    else:
        print("invalid password")
else:
    print("invalid username")

#5
age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))
if age < 21 or age > 60:
    print("Loan rejected: Age condition failed")
elif income < 30000:
    print("Loan rejected: Income condition failed")
elif credit < 700:
    print("Loan rejected: Credit score condition failed")
else:
    print("Loan approved")

#6
age = int(input("Enter age: "))
member = input("Do you have membership? (yes/no): ").lower()
if age < 12:
    price = 0
elif age <= 60:
    if member == "yes":
        price = 150
    else:
        price = 200
else:
    price = 100

print("Ticket price is Rs.", price)

#7
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus amount:", bonus)
else:
    print("No bonus")

#8
radius = float(input("Enter radius: "))
area = 3.1416 * radius * radius
print("Area of circle:", area)

#9
age = int(input("Enter age: "))
gender = input("Enter gender: ").lower()
days = int(input("Enter number of days worked: "))
wage_per_day = 0
if age >= 18 and age < 30:
    if gender == "male":
        wage_per_day = 700
    elif gender == "female":
        wage_per_day = 750
    else:
        print("Invalid gender")
elif age >= 30 and age <= 40:
    if gender == "male":
        wage_per_day = 800
    elif gender == "female":
        wage_per_day = 850
    else:
        print("Invalid gender")
else:
    print("Age not in valid range")

if wage_per_day > 0:
    total = wage_per_day * days
    print("Total wages:", total)

#10
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)