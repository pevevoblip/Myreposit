class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, distance):
        if self.speed > 0:
            time = distance / self.speed
            return f"Час для подолання {distance} км: {time:.2f} год."

    def __str__(self):
        return f"Транспортний засіб зі швидкістю {self.speed} км/год."

class Car(Transport):
    def __init__(self, speed, fuel_type):
        super().__init__(speed)
        self.fuel_type = fuel_type

    def __str__(self):
        return f"Автомобіль ({self.fuel_type}) зі швидкістю {self.speed} км/год."


if __name__ == "__main__":
    car = Car(120, "бензин")

    print(car)
    print(car.move(1000))
