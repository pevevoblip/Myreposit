from ur3.person import Person


class Car:
    def __init__ (self, brand: str = 'testBrand' ):
        self.Brand = brand
        self.Driver: Person = None
        self.Passengers: list = list()

    def add_passenger(self, passenger: Person):
        if(isinstance(passenger, Person)
            and self.Passengers is not None):
            self.Passengers.append(passenger)


    def add_driver(self, driver: Person):
        if (isinstance(driver, Person)
            and self.Driver is None):
            self.Driver = driver

    def __str__(self):
        passengersStr = ''
        for item in self.Passengers:
            passengersStr += str(item)
        return (f'Driver:\n{self.Driver}\n'
                f'Passenger:\n{passengersStr}')

