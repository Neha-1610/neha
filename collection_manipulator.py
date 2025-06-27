students = []
subjects_offered = set()

while True:
    print("Welcome to the Student Data Organizer!")
    print( )
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        print( )
        print("Enter student details:")
        stud_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")
      
        id_dob = (stud_id, dob)  
        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)
        subjects_offered.update(subjects)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records.")
        else:
            print( )
            print("--- Student Records ---")
            for i in students:
                stud_id, dob = i["id_dob"]
                print(f"ID: {stud_id} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']} | Subjects: {(i['subjects'])}")

    elif choice == "3":
        
        student_id = input("Enter Student ID to update: ")
        found = False
        for i in students:
            if i["id_dob"][0] == stud_id:
                found = True
                field = input("Enter field to update (age/subjects): ").lower()
                if field == "age":
                    i["age"] = int(input("Enter new age: "))
                    print("Age updated!")
                elif field == "subjects":
                    new_subjects = input("Enter new subjects (comma-separated): ")
                    i["subjects"] = [sub for sub in subjects_offered]
                    subjects_offered.update(i["subjects"])
                    print("Subjects updated!")
                else:
                    print("Invalid field.")
        if not found:
            print("Student ID not found!")

    elif choice == "4":
        stud_id = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i]["id_dob"][0] == stud_id:
                del students[i]
                print("Student deleted.")
                
        else:
            print("Student not found.")

    elif choice == "5":
        print( )
        print("--- Subjects Offered ---")
        for subject in sorted(subjects_offered):
            print(subject)

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice. Try again.")