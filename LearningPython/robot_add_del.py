class Robot:
    population = 0

    def __init__(self, name, age):
        '''This method is called every time when the class object is realised cause it is marked by __init__'''

        self.name = name
        self.age_of_the_robot = age
        print('(Initialization of {}, he is {} years old '.format(self.name, self.age_of_the_robot))
        Robot.population += 1

    def __del__(self):
        '''This method is invoked when the class object is destroyed'''
        print('The robot with the name {} and age  is destroyed'.format(self.name, self.age_of_the_robot))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last robot alive".format(self.name))
        else:
            print('There are {} robots left'.format(Robot.population))

    def sayHi(self):
        '''Then we enter this method cause we realise this in the class object realisation'''
        print('Hi, my name is {}'.format(self.name))

    def howManyRobots(self):
        '''Same with this one, it is entered in the sequence described in the method realisation'''
        print("We have {} robots".format(Robot.population))


robot1 = Robot("MaxGoodRobot", 17)
robot1.sayHi()
robot1.howManyRobots()
robot2 = Robot("NataliBestRobot", 17)
robot2.sayHi()
robot2.howManyRobots()

print('\nHere robots can continue their job.\n')

print('Robots ended their job, lest delete them\n')
del robot1
del robot2

Robot.howManyRobots(Robot)
