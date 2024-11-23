import requests
from sqlparse.engine.grouping import group
from urllib3 import request
'''
response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.content)
print(type(response.content))
print(type(requests.Response()))

payload = dict(key1 = 'group', key2 = 'S20112')
response = requests.post('https://httpbin.org/post', payload)
if(response.status_code == 200):
    print(response.status_code)
    print(response.content)
    print(response.text)
'''


class Car:
    pass
class BMW(Car):
    pass
class Animal:
    pass

print(issubclass(BMW, Car))
print(issubclass(Animal, Car))
bmw = BMW()
animal = Animal
print(isinstance(bmw, BMW))
print(isinstance(bmw, Car))
print(isinstance(animal, Animal))
print(isinstance(animal, Car))



