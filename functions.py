# Print the story

string = "Once upon a time there was a {}. He was {}, {}"

print(string.format('______', '_______', '________'))

def fill_the_string(name, adjective, verb):
    print(string.format(name, adjective, verb))

name = input('Enter the name in the story: ')
adjective = input('Enter the adjective: ')
verb = input('Enter the verb: ')

fill_the_string(name, adjective, verb)
