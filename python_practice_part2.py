# Python Practice - Part 2
# Logic, Lists/Slicing aur Dictionaries ke sawalat is file mein solve kiye hain


# ==========================================
# CATEGORY: Logic & Conditionals (If-Elif-Else)
# ==========================================

# Q1: Smart Grading System
marks = int(input("Apne marks (0-100) enter karein: "))
if marks > 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")


# Q2: ATM Withdrawal Logic
balance = 5000
withdrawal_amount = float(input("\nWithdrawal amount enter karein: "))
if withdrawal_amount > balance:
    print("Insufficient Funds")
else:
    remaining_balance = balance - withdrawal_amount
    print("Remaining Balance:", remaining_balance)


# Q3: Ride-Sharing Fare
distance = float(input("\nDistance (km) enter karein: "))
if distance < 5:
    fare = 100
elif distance <= 15:
    fare = 250
else:
    fare = 500
print("Aapka fare hai:", fare, "PKR")


# ==========================================
# CATEGORY: Lists & Slicing
# ==========================================

# Q1: Product Inventory
products = ["Shampoo", "Soap", "Toothpaste", "Perfume", "Lotion"]
sixth_product = input("\n6th product ka naam enter karein: ")
products.append(sixth_product)
print("Total products:", len(products))
print("Updated Inventory:", products)


# Q2: News Feed Slicer
news_headlines = [
    "Headline 1", "Headline 2", "Headline 3", "Headline 4", "Headline 5",
    "Headline 6", "Headline 7", "Headline 8", "Headline 9", "Headline 10"
]
top_3 = news_headlines[0:3]
bottom_2 = news_headlines[-2:]
print("\nTop 3 Headlines:", top_3)
print("Bottom 2 Headlines:", bottom_2)


# Q3: Leaderboard Cleanup
scoreboard = [55, 89, 72, 95, 40, 63]
scoreboard.remove(min(scoreboard))   # sab se kam marks nikal diye
scoreboard.sort(reverse=True)        # descending order mein sort kar diya
print("\nFinal Leaderboard:", scoreboard)


# ==========================================
# CATEGORY: Dictionaries (Key-Value Pairs)
# ==========================================

# Q1: Employee Database
employee = {
    "name": "Ali Raza",
    "designation": "Software Engineer",
    "salary": 80000
}

new_salary = float(input("\nEmployee ki nayi salary enter karein: "))
employee["salary"] = new_salary
employee["department"] = "IT Department"
print("Updated Employee Data:", employee)


# Q2: Login System Mockup
login_data = {
    "username": "student123",
    "password": "mypassword"
}

entered_username = input("\nUsername enter karein: ")
entered_password = input("Password enter karein: ")

if entered_username == login_data["username"] and entered_password == login_data["password"]:
    print("Login Successful")
else:
    print("Login Failed")


# Q3: Contact Search
phonebook = {
    "Ahmed": "0300-1234567",
    "Bilal": "0301-7654321",
    "Sara": "0333-9876543"
}

search_name = input("\nKis dost ka number search karna hai: ")
number = phonebook.get(search_name, "Contact Not Found")
print(number)
