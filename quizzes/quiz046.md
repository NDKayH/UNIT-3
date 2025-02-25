# Quiz 046


## Paper Solution
![IMG_4792](https://github.com/user-attachments/assets/d8017e10-6cad-4ceb-abfe-8978b0f86216)


## Code
```.py

class Citizen:
    def __init__(self, name: str, city: str, status: str):
        self.name = name
        self.city = city
        self.status = status

    def getName(self) -> str:
        return self.name

    def getCity(self) -> str:
        return self.city

    def getStatus(self) -> str:
        return self.status

class Employee(Citizen): # integrated
    def __init__(self, name: str, city: str, status: str, annualSalary: float):
        super().__init__(name, city, status) 
        self.annualSalary = annualSalary

    def getAnnualSalary(self) -> float:
        return self.annualSalary

class PartTimeEmployee(Employee):
    def __init__(self, name: str, city: str, status: str,
                 annualSalary: float, fraction: float, unionMember: bool):
        super().__init__(name, city, status, annualSalary)
        self.fraction = fraction
        self.unionMember = unionMember

    def getFraction(self) -> float:
        return self.fraction

    def isUnionMember(self) -> bool:
        return self.unionMember

# Example
if __name__ == "__main__":

    citizen = Citizen("Alice", "Wonderland", "Visitor")
    print(f"Citizen: {citizen.getName()}, {citizen.getCity()}, {citizen.getStatus()}")

    employee = Employee("Bob", "Metropolis", "Employee", 60000.0)
    print(f"Employee: {employee.getName()}, {employee.getCity()}, {employee.getStatus()}, "
          f"Salary: {employee.getAnnualSalary()}")

    part_time = PartTimeEmployee("Charlie", "Gotham", "Part-Time", 40000.0, 0.5, True)
    print(f"Part-Time Employee: {part_time.getName()}, {part_time.getCity()}, {part_time.getStatus()}, "
          f"Salary: {part_time.getAnnualSalary()}, Fraction: {part_time.getFraction()}, "
          f"Union Member: {part_time.isUnionMember()}")

```

## Proof of work
![image](https://github.com/user-attachments/assets/54d92539-e7f9-49c9-8a47-67a162020c4f)

