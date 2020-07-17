class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       # print("School member {} has been created".format(self.name))

    def tell(self):
        print('Name is: {}, age is: {}'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Teacher {} has been created".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Student {} has been created'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))


teacher = Teacher('Mrs Belkina', 76, 15000)
student = Student('Natali Poda', 17, 170)

print()

members = [teacher, student]
for member in members:
    member.tell()
