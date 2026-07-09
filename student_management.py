students = {}

print("=== Student Management System ===")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        mark = input("Enter Student Mark: ")
        students[name] = mark
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\nStudent Records:")
            for name, mark in students.items():
                print(name, ":", mark)

    elif choice == "3":
        search = input("Enter Student Name: ")
        if search in students:
            print("Mark:", students[search])
        else:
            print("Student Not Found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
