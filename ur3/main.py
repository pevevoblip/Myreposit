from ur3.car import Car
from ur3.person import Person

bmw = Car('BMW X5')
bmw.add_driver(Person('Kapitanskiy'))
bmw.add_driver(Person('Muchortowa'))
bmw.add_passenger(Person('Polischtschuk'))
bmw.add_passenger(Person('Oborskiy'))
bmw.add_passenger(Person('Andrienko'))
bmw.add_passenger(Person('Kiselow'))
print(bmw)

