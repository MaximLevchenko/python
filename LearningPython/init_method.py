class Person:
    def __init__(self, name):
        self.name1 = name  # self.name1 is a link to an object name

    def sayHI(self):
        print("Hi, my name is", self.name1)


p = Person("Max")
p.sayHI()
