import json

# Employee class
class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department
    
    def display_details(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.employee_id}, Title: {self.title}, Department: {self.department}")
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}"

# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                return
        print("Employee not found in this department.")
    
    def employees_list(self):
        for employee in self.employees:
            print(employee)

# Company class
class Company:
    def __init__(self):
        self.departments = {}
    
    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added successfully.")
        else:
            print(f"Department '{department_name}' already exists.")
    
    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed successfully.")
        else:
            print(f"Department '{department_name}' does not exist.")
    
    def show_departments(self):
        print("Departments:")
        for department_name in self.departments:
            print(department_name)
    
    def show_department_details(self, department_name):
        if department_name in self.departments:
            department = self.departments[department_name]
            print(f"Department: {department_name}")
            department.employees_list()
        else:
            print(f"Department '{department_name}' does not exist.")
    
    def save_company_data(self, filename):
        with open(filename, 'w') as file:
            data = {
                'departments': {
                    department_name: [employee.__dict__ for employee in department.employees]
                    for department_name, department in self.departments.items()
                }
            }
            json.dump(data, file)
        print("Company data saved successfully.")
    
    def load_company_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for department_name, employees in data['departments'].items():
                    department = Department(department_name)
                    for employee_data in employees:
                        employee = Employee(**employee_data)
                        department.add_employee(employee)
                    self.departments[department_name] = department
            print("Company data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

# Main function
def main():
    company = Company()
    company.load_company_data('company_data.json')

    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Department")
        print("2. Remove Department")
        print("3. Display Departments")
        print("4. Display Department Details")
        print("5. Add Employee to Department")
        print("6. Remove Employee from Department")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            department_name = input("Enter department name: ")
            company.add_department(department_name)
        elif choice == '2':
            department_name = input("Enter department name: ")
            company.remove_department(department_name)
        elif choice == '3':
            company.show_departments_departments()
        elif choice == '4':
            department_name = input("Enter department name: ")
            company.show_department_details(department_name)
        elif choice == '5':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                name = input("Enter employee name: ")
                employee_id = input("Enter employee ID: ")
                title = input("Enter employee title: ")
                employee = Employee(name, employee_id, title, department_name)
                company.departments[department_name].add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"Department '{department_name}' does not exist.")
        elif choice == '6':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                employee_id = input("Enter employee ID: ")
                company.departments[department_name].remove_employee(employee_id)
            else:
                print(f"Department '{department_name}' does not exist.")
        elif choice == '7':
            company.save_company_data('company_data.json')
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
