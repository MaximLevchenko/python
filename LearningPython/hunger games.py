class Person:
    population = 0

    def __init__(self, name, age, isAlive):
        self.name = name
        self.age = age
        self.isAlive = isAlive
        print('The new person: {} has been created'.format(self.name))
        Person.population += 1

    def how_many(self):
        if Person.population != 1:
            print('There are {} people'.format(Person.population))
        else:
            print('There is {} person'.format(Person.population))

    def live(self):
        print('{} has been created, the age is: {}'.format(self.name, self.age))

    def how_old(self):
        hg_age = hg_player.age
        rich_age = rich_person.age
        difference_in_age = 0
        if rich_age > hg_age:
            difference_in_age = rich_age - hg_age
            print('{}is older by {}'.format(rich_person.name, difference_in_age))

        elif rich_age == hg_age:
            difference_in_age = 0
            print('{} and {} have the same age. The difference in age is {}'.format(rich_person.name, hg_player.name,
                                                                                    difference_in_age))

        else:
            difference_in_age = hg_age - rich_age
            print('{} is older by {} years'.format(hg_player.name, difference_in_age))

    def battle(self):
        pass#TODO end this part of code

    def __del__(self):
        if Person.population > 0:
            print("{} is dying".format(self.name))
            Person.population -= 1
            if Person.population == 0:
                print('{} was the last one alive'.format(self.name))
        elif Person.population == 0:
            print('{} was the last alive'.format(self.name))
        else:
            return


class Hunger_Games_Player(Person):
    def __init__(self, name, age, ability, isAlive, strength):
        Person.__init__(self, name, age, isAlive)
        self.ability = ability
        self.strength = strength
        print('HG player {}, age: {} and the {} has been created'.format(self.name, self.age, self.ability))

    def live(self):
        Person.live(self)
        print('The ability of the HG player is: {}'.format(self.ability))


class Rich_People(Person):
    def __init__(self, name, age, ability, money, strength, isAlive):
        Person.__init__(self, name, age, isAlive)
        self.ability = ability
        self.money = money
        self.strength = strength

    def live(self):
        Person.live(self)
        print('The ability of the rich people is to: {}, he has: {}'.format(self.ability, self.money))


hg_player = Hunger_Games_Player("Pit Baker", 15, "to survive",True,100)
hg_player.live
hg_player.how_many()
rich_person = Rich_People('Gatsby', 45, 'make money', 1000000000000000,10, True)
rich_person.live()
rich_person.how_many()
print(' ')
print('Okay lets compare the age of {} and {}\n'.format(hg_player.name, rich_person.name))
Person.how_old(Person)
