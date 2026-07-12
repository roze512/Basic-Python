# Python Practice - Part 1
# Category 1, 2, 3, 4 ke sawalat is file mein solve kiye hain


# ==========================================
# CATEGORY 1: Variables, Input aur Math (Basic)
# ==========================================

# Q1: User Profile
# user se naam, age, city lena hai aur sentence mein print karna hai
name = input("Apna naam likhein: ")
age = input("Apni age likhein: ")
city = input("Apna city likhein: ")

print("Mera naam " + name + " hai, meri age " + age + " saal hai aur main " + city + " mein rehta hoon.")


# Q2: Circle Area
# diameter lekar area nikalna hai (Area = 3.14 * (diameter/2)^2)
diameter = float(input("Circle ka diameter enter karein: "))
radius = diameter / 2
area = 3.14 * (radius ** 2)
print("Circle ka area hai:", area)


# Q3: Simple Interest
# principal, rate, time se simple interest nikalna hai
principal = float(input("Principal amount enter karein: "))
rate = float(input("Rate of interest enter karein: "))
time = float(input("Time (years) enter karein: "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest hai:", simple_interest)


# Q4: Temperature Converter
# celsius ko fahrenheit mein convert karna hai
celsius = float(input("Temperature in Celsius enter karein: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


# Q5: Multi-line Printing
# address ko 5 lines mein print karna hai but ek hi print() ke saath
address = "House no 123\nStreet 5\nModel Town\nMultan\nPunjab, Pakistan"
print(address)


# ==========================================
# CATEGORY 2: Logic aur Conditionals (If-Else)
# ==========================================

# Q1: Voting Eligibility
age2 = int(input("\nApni age enter karein: "))
if age2 >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")


# Q2: Smart Grading
marks = int(input("Apne marks (0-100) enter karein: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")


# Q3: Number Tester
number = int(input("Koi number enter karein: "))
if number > 0:
    print("Number Positive hai")
elif number < 0:
    print("Number Negative hai")
else:
    print("Number Zero hai")


# Q4: ATM Mockup
balance = 10000  # yeh humari fake balance hai
withdraw_amount = float(input("Withdraw karne wali amount enter karein: "))
if withdraw_amount <= balance:
    print("Success")
else:
    print("Insufficient Balance")


# Q5: Password Check
stored_password = "pakistan123"
user_password = input("Password enter karein: ")
if user_password == stored_password:
    print("Password match ho gaya")
else:
    print("Password galat hai")


# ==========================================
# CATEGORY 3: Lists aur Mutability (Intermediate)
# ==========================================

# Q1: Grocery List
grocery_list = ["Milk", "Bread", "Eggs"]
fourth_item = input("\n4th grocery item enter karein: ")
grocery_list.append(fourth_item)
print("Grocery List:", grocery_list)


# Q2: Length Checker
sample_list = [10, 20, 30, 40, 50]
print("List mein total items hain:", len(sample_list))


# Q3: Leaderboard Analysis
students_marks = [85, 92, 76, 88, 95]
print("Highest marks:", max(students_marks))
print("Lowest marks:", min(students_marks))


# Q4: Data Correction
numbers_list = [10, 20, 30, 40, 50]
numbers_list[2] = 35   # index 2 par 30 tha, use 35 se replace kar diya
print("Updated List:", numbers_list)


# Q5: Slicing Expert
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Papaya"]
middle_fruits = fruits[2:5]   # beech wale 3 fruits
print("Beech wale fruits:", middle_fruits)


# Q6: Priority Task
tasks = ["Assignment submit karna", "Meeting attend karna", "Report likhna"]
tasks.insert(0, "Urgent Task: Exam Prepare karna")
print("Updated Task List:", tasks)


# Q7: Remove Item
products = ["Sugar", "Rice", "Flour", "Salt"]
products.remove("Flour")
print("Products After Removal:", products)


# Q8: Pop Task
todo_list = ["Cooking", "Cleaning", "Studying"]
removed_item = todo_list.pop()
print("Yeh item remove hua:", removed_item)
print("Baki List:", todo_list)


# ==========================================
# CATEGORY 4: Tuples aur Mixed Logic
# ==========================================

# Q1: Fixed Identity (Tuple)
identity = ("12345-6789012-3", "01-Jan-2000")
print("\nMeri Identity:", identity)

# Neeche wali line ko run karne se error aayega kyun ke tuple immutable hota hai
# identity[0] = "99999-9999999-9"   # yeh line uncomment karke error check karein
# TypeError: 'tuple' object does not support item assignment


# Q2: Single Element Tuple
single_tuple = ("Python",)   # comma lagana zaroori hai warna yeh string ban jayega
print("Value:", single_tuple)
print("Type:", type(single_tuple))
