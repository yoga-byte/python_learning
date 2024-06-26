print('Program 1 ')
print()
with open('/Users/yogeshdwivedi/projects/python_learning/files.txt', 'w') as file:
    file.write('This is line  one.\n')
    file.write('This is line two.\n')
    file.write('Finally, we are on the third and last line of the file.')

with open('/Users/yogeshdwivedi/projects/python_learning/files.txt', 'r+') as file:
    i = 1
    for line in file:
        print('{}: {}'.format(i, line.rstrip()))
        i += 1
        
print()
print('_'*50)
print()
print('Program 2')

with open('/Users/yogeshdwivedi/projects/python_learning/animals.txt', 'w') as file:
    for animal in ['man', 'bear', 'pig', 'cow', 'duck', 'horse', 'dog']:
        file.write('{}\n'.format(animal))

with open('/Users/yogeshdwivedi/projects/python_learning/animals-sorted.txt', 'w') as file_two:
    with open('/Users/yogeshdwivedi/projects/python_learning/animals.txt') as file:
        list = []
        for line in file:
            list.append(line)
        list.sort()
        for animal in list:
            file_two.write('{}'.format(animal))

print()
print('file without sorting is:')
with open('/Users/yogeshdwivedi/projects/python_learning/animals.txt') as file:
    print(file.read())
print()
print('file after sorting is ')
with open('/Users/yogeshdwivedi/projects/python_learning/animals-sorted.txt') as file:
    print(file.read())

    
            
