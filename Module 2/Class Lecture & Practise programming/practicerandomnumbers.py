import random

print('Random number in the range 2 to 3:', random.random())
print('Random number in the range 1 to 20:', random.random() * 100)
print('Select 4 random numbers: ')
# Chooses 6 non-repeating numbers in the range 1 to 50

print('Your random numbers are: ', random.sample(range(1, 51),4))