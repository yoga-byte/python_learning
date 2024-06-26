dict = {
    'Jeff': 'Is afraid of clowns.',
    'David': 'Plays the piano.',
    'Json': 'Can fly an airplane.'
}

for member in dict:
    print('{}: {}'.format(member, dict[member]))

dict['Jeff'] = 'Is afraid of heights.'
dict['Jill'] = 'Can hula dance.'
print()
print()
for member, property in dict.items():
    print('{}: {}'.format(member, property))

    
