zoo = ('elephant', 'giraffe', 'deer')
print('The amount of animals in the zoo is: ', len(zoo))

new_zoo = ("monkey", 'camel', zoo)
print('The amount of cages is: ', len(new_zoo))
print("all animals in the new zoo are:", end=' ')
for i in new_zoo:
    print(i, end=", ")
print('\n')
print('all new animals from the old zoo are:', new_zoo[2])
print('the last animal from the old zoo is:', new_zoo[2][2])
print('the amount of all animals is :', len(new_zoo) - 1 + \
      len(new_zoo[2]))
singleton=(2,) #Creating the tuple with only 1 variable

