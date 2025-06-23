from typing import List


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


class Employee(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__salary = 20000

    def get_salary(self) -> int:
        return self.__salary


class Parent(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__children: List[Person] = []

    def add_child(self, child: Person) -> None:
        self.__children.append(child)

    def get_children(self) -> List[Person]:
        return self.__children


class Citizen(Employee, Parent):
    def __init__(self, name: str, age: int):
        Employee.__init__(self, name, age)
        Parent.__init__(self, name, age)

    def get_info(self) -> str:
        return f"Name: {self.get_name()}, Age: {self.get_age()}, Salary: {self.get_salary()}"


# Використання:
my_citizen = Citizen("John Doe", 30)
my_citizen.add_child(Person("Child 1", 5))

print(my_citizen.get_info())

for child in my_citizen.get_children():
    print(f"Child Name: {child.get_name()}, Age: {child.get_age()}")
