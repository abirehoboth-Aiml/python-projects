contacts = {}

print("=== Contact Book ===")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found!")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        search = input("Enter Name to Search: ")
        if search in contacts:
            print("Phone Number:", contacts[search])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
