distance = input('Please tell me the distance you want to travel : ')
distance = float(distance)
if distance > 300:
    print('fly')
elif distance > 3:
    print('drive')
else:
    print('walk')
