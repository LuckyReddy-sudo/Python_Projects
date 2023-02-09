import random

# for i in range(3):
#     print(random.random())
#     print(random.randint(1, 20))
#
# members = ['John', 'Lucky', 'Sandeep', 'Jaggu']
# print(random.choice(members))


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())
