to_do_list = []
get_input = input('Enter the to do list : ')

while get_input != '':
    to_do_list.append(get_input)
    get_input = input('Enter the to do list : ')

print()
print('Here is your to do list:')
print('_'* 30)

for i in to_do_list:
    print(i)

    
