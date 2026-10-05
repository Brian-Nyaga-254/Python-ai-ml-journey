class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"{self.name} has {self.salary}  from {self.department}"

    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        salary = int(input("Enter your salary: "))
        department = input("Enter your department: ")
        return cls(name, salary, department)
        
def main():
    employee =Employee.get()
    print(employee)

if __name__ == "__main__":
    main()
