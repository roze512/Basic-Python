


# SIMPLE QUESTIONS (1 - 10)


# Question 01: User Registration System
name = input("Apna naam enter karein: ")
age = input("Apni age enter karein: ")
city = input("Apna city enter karein: ")
print(f"Welcome {name} from {city}")


# Question 02: Smart Home Doorbell
time = int(input("\nAbhi kitne baje hain (24 hour format): "))
if time > 10:
    print("Silent Mode On")
else:
    print("Ring Loud")


# Question 03: Shopping Cart Initialization
cart = []
cart.append("Milk")
cart.append("Eggs")
cart.append("Bread")
print("\nShopping Cart:", cart)


# Question 04: Contact Directory
contact = {
    "name": "Hamza",
    "phone_number": "0300-1112223"
}
contact["phone_number"] = "0333-9998887"
print("\nUpdated Contact:", contact)


# Question 05: Security Login Lockout
print()
attempt = 1
while attempt <= 3:
    print("Login Attempt", attempt)
    attempt = attempt + 1


# Question 06: Blog Tags Filter (Duplicates)
blog_tags = ["tech", "python", "tech"]
unique_tags = set(blog_tags)
print("\nUnique Tags:", unique_tags)


# Question 07: Automated Welcome Email
def send_welcome(name):
    print(f"Hi {name}, welcome to our platform!")

send_welcome("Ayesha")


# Question 08: Immutable DB Credentials
db_credentials = ("localhost", 3306)
print("\nDB Credentials:", db_credentials)
# neeche wali line change karne ki koshish hai, isko run karne se error aayega
# db_credentials[0] = "newhost"
# TypeError: 'tuple' object does not support item assignment
print("Tuples immutable hote hain isliye value change nahi ho sakti")


# Question 09: Discount Calculator
price = input("\nProduct ki price enter karein: ")
price = int(price)
final_price = price - (price * 10 / 100)
print("Discount ke baad final price:", final_price)


# Question 10: Server Ping Test
print()
for server in range(1, 6):
    print(f"Pinging Server {server}...")



# INTERMEDIATE QUESTIONS (11 - 20)

# Question 11: Traffic Light Controller
light = input("\nLight ka color enter karein (Red/Yellow/Green): ")
if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Slow Down")
elif light == "Green":
    print("Go")
else:
    print("Invalid Input")


# Question 12: Odd/Even ID Batching
print()
id_number = 1
while id_number <= 20:
    if id_number % 2 == 0:
        print(id_number, "-> Process Batch A")
    else:
        print(id_number, "-> Process Batch B")
    id_number = id_number + 1


# Question 13: Automated Grade Calculator
def calculate_grade(marks):
    if marks > 90:
        return "A"
    elif marks > 80:
        return "B"
    else:
        return "C"

print("\nGrade:", calculate_grade(95))
print("Grade:", calculate_grade(85))
print("Grade:", calculate_grade(60))


# Question 14: Customer Data Cleaning
emails = ["ali@gmail.com", "sara@gmail.com", "ali@gmail.com"]
unique_emails = set(emails)
unique_emails.add("new_customer@gmail.com")
print("\nCleaned Emails:", unique_emails)


# Question 15: Student Result Privacy
student = {
    "name": "Bilal",
    "roll_no": 22,
    "marks": 89
}
student.pop("marks")
print("\nUpdated Student Data:", student)


# Question 16: Notification Skipper
print()
for user_id in range(1, 11):
    if user_id == 5:
        continue   # yeh banned user hai isliye skip kar diya
    print("Notification sent to user", user_id)


# Question 17: Space Rocket Countdown
start_number = int(input("\nCountdown kis number se start karein: "))
while start_number >= 0:
    print(start_number)
    start_number = start_number - 1


# Question 18: Automated Tax Billing
def calculate_bill(price, tax=5):
    total = price + (price * tax / 100)
    return total

print("\nBill with default tax:", calculate_bill(1000))
print("Bill with custom tax:", calculate_bill(1000, 10))


# Question 19: Leaderboard Analytics
scores = [45, 78, 90, 34, 66]
print("\nHighest Score:", max(scores))
print("Lowest Score:", min(scores))


# Question 20: Up-Next Playlist
songs = ["Song A", "Song B", "Song C", "Song D", "Song E"]
up_next = songs[1:4]
print("\nUp Next:", up_next)



# HARD QUESTIONS (21 - 25)


# Question 21: Tweet Text Analyzer
def analyze_tweet(tweet):
    vowels = 0
    consonants = 0
    for char in tweet:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    return vowels, consonants

v, c = analyze_tweet("Python is amazing")
print("\nVowels:", v, "Consonants:", c)


# Question 22: ATM Withdrawal Logic
balance = 10000
while True:
    withdraw_amount = float(input("\nWithdraw amount enter karein: "))
    if withdraw_amount > balance:
        print("Insufficient")
    elif withdraw_amount == balance:
        balance = 0
        print("Balance khatam ho gaya, transaction complete")
        break
    else:
        balance = balance - withdraw_amount
        print("Remaining Balance:", balance)


# Question 23: Employee Registry System
employees = {}
for i in range(3):
    emp_name = input("\nEmployee ka naam enter karein: ")
    emp_salary = input("Employee ki salary enter karein: ")
    employees[emp_name] = emp_salary

print("\nEmployee Registry:", employees)


# Question 24: Multi-Step Math Engine
def sum_till_n(n):
    total = 0
    counter = 1
    while counter <= n:
        total = total + counter
        counter = counter + 1
    return total

print("\nSum till 10:", sum_till_n(10))


# Question 25: E-Commerce Discount Engine
cart_prices = [50, 120, 0, 200, 0, 80]
print()
for item_price in cart_prices:
    if item_price == 0:
        continue   # free item hai isliye skip kar diya
    if item_price > 100:
        discounted_price = item_price - (item_price * 10 / 100)
        print("Discounted Price:", discounted_price)
    else:
        print("Price (no discount):", item_price)
