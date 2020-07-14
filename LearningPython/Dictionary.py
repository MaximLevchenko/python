ab = {"Max": "Cool guy",
      "Anton": 'Asshole',
      'Artem': 'Not bad not good'

      }
print('Who is Max?', ab['Max'])  # We are adressing to the value of the key 'Max'. The output will be 'Cool guy'
print('Who is Anton?', ab['Anton'])  # We are adressing to the value of the key 'Anton'. The output will be 'Asshole'
print('There are ', len(ab), 'people in the statistic')
print("I want to delete Artem")
del ab['Artem']
for key, value in ab.items():  # We are making a loop through all positions of the list 'ab' and printing all ab params through method 'format'
    print('Person is :{}, I identify him as {}'.format(key, value))
print('There are ', len(ab), 'people in the statistic')

ab['Guido'] = 'Stranger'
ab['Edgar'] = 'He is pretty hot'
ab['Maya'] = 'Stranger'

if 'Guido' in ab:
    print("The status of Guido in my eyes is: ", ab['Guido'])
print('There are ', len(ab), 'people in the statistic')
for key, value in ab.items():
    print('Person is :{}, I identify him as: {}'.format(key, value))
