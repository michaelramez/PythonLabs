class Car:
    def __init__(self, name: str, velocity: int, fuelRate=100):
        self.name = name
        self.velocity = velocity
        self.fuelRate = fuelRate

    @property
    def velocity(self):
        return self.velocity

    @velocity.setter
    def velocity(self, velocity: int):
        if isinstance(velocity, int):
            if 0 <= velocity <= 200:
                self.velocity = velocity
            else:
                print("Velocity must be between 0 and 200")
        else:
            print("Health rate must be integer")

    @property
    def fuelRate(self):
        return self.fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelRate: int):
        if isinstance(fuelRate, int):
            if 0 <= fuelRate <= 100:
                self.fuelRate = fuelRate
            else:
                print("Fuel rate must be between 0 and 100")
        else:
            print("Fuel rate must be integer")

    def Run(self, velocity: int, distance: int):
        if not isinstance(velocity, int):
            print("Velocity must be integer")
        if not isinstance(distance, int):
            print("Distance must be integer")

        self.velocity = velocity
        if distance < self.fuelRate:  # 10% fuelRate --> 10km distance
            self.fuelRate -= 0.01 * distance * self.fuelRate
            remDistance = 0
        else:
            self.fuelRate = 0
            remDistance = distance - self.fuelRate

        self.Stop(remDistance)

    def Stop(self, remDistance: int):
        self.velocity = 0
        if remDistance == 0:
            print("You reached your destination")
        else:
            print("Remaining Distance ", remDistance, "km")
