'''
from collections.abc import Iterable

from sqlparse.sql import Where


'''
students = ["Student1", "Student2", "Student3", "Student4"]
'''
for item in students:
    print(item)
i=0
while i < len(students):
    print(students[i])
    i += 1
    '''
'''
iter_students = iter(students)
while True:
    try:
        print(next(iter_students))
    except StopIteration:
        break
print('Hello world 2')
'''

from counter import Counter

counter = Counter(0,20)
while True:
    try:
        print(next(counter))
    except StopIteration:
        break
print('HI')