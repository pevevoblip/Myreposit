from human import Human

class Student():
    pass
    def __init__(self, name: str = 'Defult student name'):
        super().__init__(name)

    def __str__(self):
        return f'Student name: {self.Name}'
               f'Greeting: {self.greeting}'
               f'Greeting: {self.greeting}'