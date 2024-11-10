class Employee:
  def my_function(self, name, employee_id, salary):
    "Initialization of the the employees with their names, employee_id, and salary."
    self.employee_id = employee_id
     self.name = name
    self.salary = salary

  def display_details(self):
    "now let display the details of employees"
    print(f"employee full Name: {self.name}")
    print(f"Employee ID_number: {self.employee_id}")
    print(f" fixe Salary: ${self.salary:.2f}")

  def update_salary(self, new_salary):
    "now let have the salary of the employee updated."
    self.salary = new_salary
    print(f"hey! the salary of mr,miss {self.name} has been succesfully updated to ${self.salary:.2f}.")

class Department:
  def my_function(self, department_name):
    "Initialization of the department with the name and an empty list of employees."
    self.department_name = department_name
    self.employees = [] # List to store employees in the department

  def add_employee(self, employee):
    "code allowing to add employees department."""
    self.employees.append(employee)
    print(f"Hey, the employee {employee.name} has been succesfully added to the {self.department_name} department.")

  def calculate_total_salary(self):
    "display and calculation of the total salary expenditure for a specific department."
    total_salary = sum(employee.salary for employee in self.employees)
    print(f"\nThe total salary expenditure for the {self.department_name} department is: ${total_salary:.2f}")

  def all_employees_displayed(self):
    " code to display all employees of a specific department."""
    if self.employees:
      print(f"\nthe employees in the {self.department_name} department:")
      for employee in self.employees:
        employee.display_details()
    else:
      print(f"sorry, there is no employees in the {self.department_name} department.")

# Interactive part to manage department and employees
def my_depart_management_syst():
  # Get the department name from the user
  department_name = input("kindly enter the department name: ")
   
  # Initialize the department
  department = Department(department_name)

  while True:
    print("\nDepartment Management System")
    print("1. kindly Add a new employee")
    print("2. kindly display total salary expenditure")
    print("3. kindly display all employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      # Collect employee details and add them to the department
      name = input("let enter the employee's name: ")
      employee_id = input("now let enter the employee's ID: ")
      salary = float(input("now kindly let add the employee's salary: "))

      # Create a new employee instance
      employee = Employee(name, employee_id, salary)
      department.add_employee(employee)

    elif choice == '2':
      # Display the total salary expenditure for the department
      department.calculate_total_salary()

    elif choice == '3':
      # Display all employees in the department
      department.all_employees_displayed()

    elif choice == '4':
      print("excellent!!! let exit the department management system.")
      break

    else:
      print("sorry, this choice is not valid. Try again later.")

# Start the interactive department management system
my_depart_management_syst()
