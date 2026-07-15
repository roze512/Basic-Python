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
