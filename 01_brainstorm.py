import random

categories = ['Food', 'City', 'Country', 'Drinks']
answers = []

print('Your category is', categories[random.randrange(4)])
print('List 10 things in this category.')

for i in range(10):
	answers.append(input())

print()
print('Your answers are:')
[print(i) for i in answers]