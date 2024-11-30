import random
import string

def random_letter_generator():
    while True:
        yield random.choice(string.ascii_letters)

generator = random_letter_generator()

for _ in range(10):
    print(next(generator))
