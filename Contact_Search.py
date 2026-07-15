phonebook = {
    "Ahmed": "0300-1234567",
    "Bilal": "0301-7654321",
    "Sara": "0333-9876543"
}

search_name = input("\nKis dost ka number search karna hai: ")
number = phonebook.get(search_name, "Contact Not Found")
print(number)
