
students = []



def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    print("Enter 3 subject marks")
    mark1 = int(input("Mark 1: "))
    mark2 = int(input("Mark 2: "))
    mark3 = int(input("Mark 3: "))

    
    marks = (mark1, mark2, mark3)

    
    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    
    students.append(student)

    print("Student added successfully!\n")



def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Details")
        print("---------------------")

        
        for student in students:
            print("Name :", student["name"])
            print("Age  :", student["age"])
            print("Marks:", student["marks"])

            
            average = sum(student["marks"]) / len(student["marks"])
            print("Average Marks:", average)
            print("---------------------")



def find_topper():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        topper = students[0]
        highest_average = sum(topper["marks"]) / len(topper["marks"])

        for student in students:
            average = sum(student["marks"]) / len(student["marks"])

            if average > highest_average:
                highest_average = average
                topper = student

        print("\nTopper Details")
        print("---------------------")
        print("Name :", topper["name"])
        print("Age  :", topper["age"])
        print("Marks:", topper["marks"])
        print("Average Marks:", highest_average)
        print("---------------------")



while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        find_topper()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")