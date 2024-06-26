cost = input('Enter the cost of the server per hour: ')
cost = float(cost)
print('cost to operate the server per day: {}'.format(cost*24))
print()
print('cost to operate the server per month: {}'.format(cost*24*30))


print()
print()
print('-'*40)
print('Second Program')
print('cost to operate 20 server per day: {}'.format(cost*24*20))
print('cost to operate 20 server per month: {}'.format(cost*30*24*20))
print('number of days that can be operated with 918 dollars: {}'.format(918/(cost*24)))
