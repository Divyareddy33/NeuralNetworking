class Employee:
    number_of_employees = 0
    sum_of_salaries = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.number_of_employees += 1
        self.salaries_sum(self.salary)

    @staticmethod
    def salaries_sum(salary):
        Employee.sum_of_salaries += salary

    @staticmethod
    def average_salary():
        return Employee.sum_of_salaries/Employee.number_of_employees


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)


if __name__ == "__main__":
    ft_employee = FullTimeEmployee("abc", "xyz", 100000, "CS")
    employee = Employee("ab", "xy", 2000000, "CS")

    print(f'Avg Salary: {Employee.average_salary()}')
    print(f'Number of Employees: {Employee.number_of_employees}')
