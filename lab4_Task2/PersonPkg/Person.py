class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.mood = None
        self.healthRate = None

    @property
    def money(self):
        return self.money

    @money.setter
    def money(self, money):
        if isinstance(money, int):
            if money >= 0:
                self.money = money
            else:
                print("The value of money can't be negative")

        else:
            print("Money must be integer")

    @property
    def healthRate(self):
        return self.healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if isinstance(healthRate, int):
            if 0 <= healthRate <= 100:
                self.healthRate = healthRate
            else:
                print("Health rate must be between 0 and 100")
        else:
            print("Health rate must be integer")

    def Sleep(self, cls, hours):
        if isinstance(hours, int):
            if hours == 7:
                self.mood = cls.moods[0]

            elif hours > 7:
                self.mood = cls.moods[1]

            else:
                self.mood = cls.moods[2]
        else:
            print("Hours must be integer")

    def Eat(self, meals):
        if isinstance(meals, int):
            if meals == 3:
                self.healthRate = 100
            elif meals == 2:
                self.healthRate = 75
            elif meals == 1:
                self.healthRate = 0
            else:
                print("Number of meals must be 1, 2 or 3")
        else:
            print("Meals must be integer")

    def Buy(self, items):
        self.money -= items * 10
