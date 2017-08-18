from collections import namedtuple
from operator import attrgetter


Character = namedtuple(
    'Character',
    'first_name last_name birthdate stats',
)

Stats = namedtuple(
    'Stats',
    'strength agility intelligence',
)

chars = [
    Character('Kahit', 'Sino', '1990/1/1', Stats(10.0, 10.0, 10.0)),
    Character('Policorpio', 'Alipucay', '1972/2/14', Stats(8.5, 11.2, 14.0)),
    Character('Mary Jane', 'Moon', '1985/4/20', Stats(4.20, 4.20, 4.20)),
]

def sort_by_age(chars):
    """Sort the characters by exact age (i.e. youngest to oldest).
    """

    return sorted(chars, key=attrgetter('birthdate'), reverse=True)

def sort_by_stat(chars, stat):
    """Sort the characters by the given stat from lowest to highest.
    """

    specific_stat = 'stats.{}'.format(stat)

    return sorted(chars, key=attrgetter(specific_stat))


def sort_by_name(chars):
    """Sort the characters by last name, then by first name.
    """

    return sorted(chars, key=attrgetter('last_name', 'first_name'))


print('---------------------')
print('Sorting by Age')
print('---------------------')
print(sort_by_age(chars))
print()

print('---------------------')
print('Sorting by Name')
print('---------------------')
print(sort_by_name(chars))
print()

print('---------------------')
print('Sorting by Intelligence')
print('---------------------')
print(sort_by_stat(chars, 'intelligence'))
print()

print('---------------------')
print('Sorting by Strength')
print('---------------------')
print(sort_by_stat(chars, 'strength'))
print()

print('---------------------')
print('Sorting by Agility')
print('---------------------')
print(sort_by_stat(chars, 'agility'))
print()
