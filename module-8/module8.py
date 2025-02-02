import json


def print_students(students): #print function for student list
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

#def add_student(filename, students): #add self to student list
  #  with open(filename, 'w') as file:
   #     json.dump(students, file, indent=4)
    #print("The .json file was updated with new student.")

def main():
    filename = 'student.json' #define file name
    with open('student.json') as f:
        students = json.load(f) #create class list
    
    #Print original list
    print("This is the original student list:")
    print_students(students)
    
    #Add new student
    new_student = {
        "F_Name": "Libby",
        "L_Name": "Mac",
        "Student_ID": 1171991,
        "Email": "ehmacc@example.com"
    }
    students.append(new_student)
    
    #Print updated list
    print("This is the updated student list:")
    print_students(students)
    
    # Save back to JSON file
    #add_students(filename, students)
    with open('student.json', 'w') as f:
        json.dump(students, f)
    print("The .json file was updated with new student.")

if __name__ == "__main__":
    main()