class Robot:
    population = 0

    def __init__(self, name, age, strength, isAlive):
        '''This method is called every time when the class object is realised cause it is marked by __init__'''

        self.name = name
        self.age_of_the_robot = age
        self.strength = strength
        self.isAlive = isAlive
        print('(Initialization of {}, he is {} years old and has his strength is: {} '.format(self.name,
                                                                                              self.age_of_the_robot,
                                                                                              self.strength))
        Robot.population += 1

    def __del__(self):
        '''This method is invoked when the class class reference is destroyed'''

        if Robot.population == 0:  # Here we check whether the population of robots is 0 or not, is it is - we shut
            # down this if else block
            return
        elif not self.isAlive:  # Here we check whether the robot is dead, if it is -  we enter this code block
            print("\n{} is already dead, there is no point in killing it again\n".format(self.name))
            return
        else:
            print('The robot with the name {},strength: {} and age {} is destroyed'.format(self.name, self.strength,
                                                                                           self.age_of_the_robot))
            Robot.population -= 1
            print('There are {} robots left'.format(Robot.population))
            if Robot.population == 0:
                print("{} was the last robot alive".format(self.name))
            elif self.isAlive == False:
                print('robot is already dead')

    def sayHi(self):
        '''Then we enter this method cause we realise this in the class object realisation'''
        print('Hi, my name is {}'.format(self.name))
    
    def howManyRobots(self):
        '''Same with this one, it is entered in the sequence described in the method realisation'''
        print("We have {} robots".format(Robot.population))

    def compare(self):

        if robot1.strength > robot2.strength:
            winner = robot1
            winner_name = robot1.name
            loser = robot2
            loser_name = robot2.name
            difference_in_strength = robot1.strength - robot2.strength
            print(
                "In the battle between {} and {}. {} was the winner with with the difference of strength: {}. The {} "
                "is now dead".format(
                    robot1.name, robot2.name, winner_name, difference_in_strength, loser_name))
            loser.__del__()
            loser.isAlive = False


        else:
            winner = robot2
            winner_name = robot2.name
            loser = robot1
            loser_name = robot1.name
            difference_in_strength = robot2.strength - robot1.strength
            print(
                "In the battle between {} and {}. {} was the winner with with the difference of strength: {}. The {} "
                "is now dead".format(
                    robot1.name, robot2.name, winner_name, difference_in_strength, loser_name))
            loser.__del__()
            loser.isAlive = False


robot1 = Robot("MaxGoodRobot", 17, 70, True)
robot1.sayHi()
robot1.howManyRobots()
robot2 = Robot("NataliBestRobot", 17, 50, True)
robot2.sayHi()
robot2.howManyRobots()
robot3 = Robot("NiceRobot", 15, 24, True)
robot3.sayHi()
robot3.howManyRobots()

Robot.compare(Robot)

print('Robots ended their job, let`s delete them\n')

