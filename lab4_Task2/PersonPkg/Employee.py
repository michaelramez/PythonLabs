from CarPkg import Car
from Person import Person


class Employee(Person):
    def __init__(self, name, money, eid, car: Car, salary, distanceToWork):
        super().__init__(name, money)
        self.eid = eid
        self.car = car
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return  self.salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            if salary > 1000:
                self.salary = salary
            else:
                print("Salary must be 1000 or more")
        else:
            print("Salary must be integer")

    def Work(self, hours):
        if isinstance(hours, int):

            if hours == 8:
                self.mood = Employee.moods[0]
            elif hours > 8:
                self.mood = Employee.moods[1]
            else:
                self.mood = Employee.moods[2]
        else:
            print("Hours must be integer")

    def Drive(self, velocity, distance):
        self.car.Run(velocity, distance)

    def Refuel(self, gasAmmount=100):
        if isinstance(gasAmmount, int):
            self.car.fuelRate += gasAmmount
        else:
            print("Gas amount must be integer")
