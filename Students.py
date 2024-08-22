def manage_student_database():
    names = []
    count = 0
    Id = 1
    max_length_name = ""
    max_length = 0


    while True:
        Student_name = input("Please enter the student's name (or type 'stop' to finish): ")
        if Student_name == "stop":
            break
        
        # Check if the name is already in the list
        name_exists = any(name[1] == Student_name for name in names)
        if name_exists:
            print("This name is already in the list.")
        else:
            count += 1
            data = (Id, Student_name)
            names.append(data)
            Id += 1

    print(f"Total number of students are {count}")
    print(names)
    student_names : str = [name[1] for name in names]
    length_of_name : int = [len(name[1]) for name in names]
    all_names : str = ''.join(student_names)
    print(f"Total length of all student names combined: {len(all_names)}")

    for name_tuple in names:
        # Access the first element (Id)
        id_value = name_tuple[0]
        # Access the second element (Student_name)
        student_name = name_tuple[1]
        
        print(f"ID: {id_value}, Name: {student_name}")


    for name_tuple in names:
        student_name = name_tuple[1]
        
        # Check if the current name is longer than the previously found longest name
        if len(student_name) > max_length:
            max_length = len(student_name)
            max_length_name = student_name

    print(f"The name with the maximum length is: {max_length_name}")

    min_length_name = names[0][1]
    min_length = len(min_length_name)

    # Iterate over each tuple in the list
    for name_tuple in names:
        student_name = name_tuple[1]
        
        # Check if the current name is shorter than the previously found shortest name
        if len(student_name) < min_length:
            min_length = len(student_name)
            min_length_name = student_name

    print(f"The name with the minimum length is: {min_length_name}")


manage_student_database()