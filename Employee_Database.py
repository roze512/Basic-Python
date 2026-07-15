employee = {
    "name": "Ali Raza",
    "designation": "Software Engineer",
    "salary": 80000
}

new_salary = float(input("\nEmployee ki nayi salary enter karein: "))
employee["salary"] = new_salary
employee["department"] = "IT Department"
print("Updated Employee Data:", employee)
