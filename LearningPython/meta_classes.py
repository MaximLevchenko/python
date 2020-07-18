from abc import *


class SchoolMember(metaclass=ABCMeta):  # Like abstract classes in Java
    """Represents every school member."""

    def __init__(self, name,
                 age):  # This method is called when the first SchoolMember class reference has been defined
        # (it can be called through subclasses)
        self.name = name
        self.age = age
        print('SchoolMember: {0} has been created)'.format(self.name))

    @abstractmethod
    def tell(self):
        print("The name is: {}, the age is: {}".format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age,
                 salary):  # This method is called when the first Teacher class reference has been defined
        SchoolMember.__init__(self, name, age)  # Here we address the super class

        self.salary = salary
        print('Teacher: {} has been created'.format(self.name))

    def tell(self):
        SchoolMember.tell(
            self)  # Here we address super class`s method tell and with 'end' link it with teacher`s method tell
        print('The salary is: {}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age,
                 marks):  # This method is called when the first Student class reference has been defined
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Student {} has been created'.format(self.name))

    def tell(self):
        SchoolMember.tell(
            self)  # Here we address super class`s method tell and with 'end' link it with student`s method tell
        print('Marks are: {}'.format(self.marks))


t = Teacher('Mrs Tatyana', 56, 20000)
s = Student('Max', 17, 1000000)
# t.tell()
# s.tell()
members = [t, s]  # We can do the same with directly invoking the method through the class reference
# or creating a list and making it in a for loop
for member in members:
    member.tell()
