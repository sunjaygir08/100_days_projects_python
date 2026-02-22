while True:
    print("\n" + "="*45)
    print("\t Welcome to Student Grading System")
    print("="*45 + "\n")
    name = input("Enter Student's Name          : ")       
    f_name = input("Enter Father's Name           : ")
    clas = input("Enter Class  : ")
    print("\nPlease enter marks out of 100:\n")
    try:
        math = int(input("Mathematics        : "))
        sci  = int(input("Science            : "))
        eng  = int(input("English            : "))
        urdu = int(input("Urdu               : "))
        sst  = int(input("Social Studies     : "))
        comp = int(input("Computer Science   : "))
        
        # Validate marks are within range
        marks_list = [math, sci, eng, urdu, sst, comp]
        if any(mark < 0 or mark > 100 for mark in marks_list):
            print("\nError: Marks must be between 0 and 100. Please try again.\n")
            continue
    except ValueError:
        print("\nError: Please enter valid numeric marks. Please try again.\n")
        continue
    subjects = {                        # Dictionary to hold subjects and marks
        "Mathematics": math,
        "Science": sci,
        "English": eng,
        "Urdu": urdu,
        "Social Studies": sst,
        "Computer Science": comp
    }
    total_marks = 600
    obtained_marks = sum(subjects.values())
    percentage = (obtained_marks / total_marks) * 100
    # Grade Calculation 
    if percentage >= 80:
        grade = "A1"
        remarks = "Outstanding Performance"
    elif percentage >= 70:
        grade = "A"
        remarks = "Excellent Work"
    elif percentage >= 60:
        grade = "B"
        remarks = "Good - Needs Improvement"
    elif percentage >= 50:
        grade = "C"
        remarks = "Average - Study More"
    elif percentage >= 40:
        grade = "D"
        remarks = "Poor - Must Work Harder"
    else:
        grade = "F"
        remarks = "Fail - Needs Serious Attention"
    print("\n" + "="*45)
    print("\t\tSTUDENT MARKSHEET")
    print("="*45)
    print(f"Name            : {name}")
    print(f"Father's Name   : {f_name}")
    print(f"Class           : {clas}")
    print("-"*45)
    print(f"{'S.No':<6}{'Subject':<20}{'Marks':<10}")
    print("-"*45)

    for i, (subject, marks) in enumerate(subjects.items(), 1): # Enumerate to get serial number
        print(f"{i:<6}{subject:<20}{marks:<10}")

    print("-"*45)
    print(f"{'Total Marks':<26}{obtained_marks} / {total_marks}")
    print(f"{'Percentage':<26}{percentage:.2f}%")
    print(f"{'Grade':<26}{grade}")
    print(f"{'Remarks':<26}{remarks}")
    print("="*45 + "\n")
    
    # Ask if user wants to continue
    continue_response = input("Do you want to continue for another student? (yes/no): ").strip().lower()
    if continue_response != "yes":
        print("\nThank you for using Student Grading System!")
        break