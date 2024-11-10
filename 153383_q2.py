class Student:
    def initialize_student(self, full_name, student_id):
        "Let start by initializing  the student's basic information."""
        self.full_name = full_name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignment names and their corresponding grades

    def assignment_submition(self, assignment_name, grade):
        "then let store the assignment with its associated grade for each the student we have."
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade '{grade}' has been added for {self.full_name}.")

    def display_my_grade(self):
        if self.assignments:
            print(f"\nGrades for {self.full_name}:")
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print(f"{self.full_name} has no assignments or grades yet.")


class Instructor:
    def my_function(self, name, course_name):
        "Initialization of details of the instructor plus the course they give."
        self.course_name = course_name
        self.name = name
        self.students = []  # List to track all students enrolled in the course

    def student_enrollement (self, student):
        "we add now a student to the instructor's course."
        self.students.append(student)
        print(f"Student {student.full_name} (ID: {student.student_id}) has been successfully enrolled in the course '{self.course_name}'.")

    def assignment_grade(self, student, assignment_name, grade):
        "Assign a grade to a student for a specific assignment."
        if student in self.students:
            student.assignment_submition(assignment_name, grade)
        else:
            print(f"Error: Student {student.full_name} is not enrolled in this course.")

    def display_all_grades(self):
        "display of the list of all students with their specific grades"
        if self.students:
            print(f"\nCourse: {self.course_name}")
            for student in self.students:
                student.display_my_grade()
        else:
            print("No students have been enrolled in the course yet.")


# Interactive code for managing course enrollment and grading
def unit_management():
    "management of course, students enrollement, and grades assignment."
    # Sample Instructor
    
    course_name = input("Enter the name of the course : ")
    instructor_name = input("Enter the  name of your (Instructor): ")
    
    # Initialize instructor with the entered details
    instructor = Instructor()
    instructor.my_function(instructor_name, course_name)
    
    while True:
        print("\nOnline Course Management System")
        print("1. Enroll a student")
        print("2. Assign grade to a student")
        print("3. View all students' grades")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Enroll a new student
            student_name = input("\nEnter the student's name: ")
            student_id = input("Enter the student's ID: ")
            
            # Initialize student with their details
            student = Student()
            student.initialize_student(student_name, student_id)
            instructor.student_enrollement (student)
        
        elif choice == '2':
            if not instructor.students:
                print("There are no students enrolled in the course.")
                continue
            
            # Select a student to assign a grade
            print("\nSelect a student to assign a grade:")
            for idx, student in enumerate(instructor.students, 1):
                print(f"{idx}. {student.full_name} (ID: {student.student_id})")
            
            student_choice = int(input("Enter the number of the student: "))
            if 1 <= student_choice <= len(instructor.students):
                selected_student = instructor.students[student_choice - 1]
                
                # Collect assignment details from the instructor
                assignment_name = input(f"\nEnter the assignment name for {selected_student.full_name}: ")
                grade = input("Enter the grade for this assignment: ")
                
                # Assign the grade to the selected student
                instructor.assignment_grade(selected_student, assignment_name, grade)
            else:
                print("Invalid selection, please try again.")
        
        elif choice == '3':
            # Display all students and their grades
            instructor.display_all_grades()
        
        elif choice == '4':
            print("Exiting the course management system.")
            break
        
        else:
            print("Invalid choice. Please try again.")


# Start the interactive course management system
unit_management()
