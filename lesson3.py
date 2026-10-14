# data_types = ['myktarova', 18, True,33.44,False,33,'myk']
# data_types.append('aelita')
# data_types.insert(0,'iphone')
# data_types.remove(23)
# del data_types[0]
# data_types[-2] = 'dean w.'
# data_type_1 = [1,2,3,4,5,6,7]
# data_type_2 = ['J.sean', 'florida','50 cent''kesha']
# data_type_2.append(data_type_1.pop(4))

flags = {
    'ru': {'red blue', 'white'},
    'kg': {"red yellow", 'red'},
    'ua': {"red blue", 'red', 'blue'},
    'uk': {"yellow", "blue"},
    'kz': {'blue yellow', 'blue'}
}

flags['us'] = {'red', 'white', 'blue'}
flags['tr'] = {'red', 'white'}
flags['jp'] = {'red', 'white'}

colors = input('Введите цвет флага: ')

for k, v in flags.items():
    if colors in v:
        print(k)

data_tuple = ('h', 6.13, 'C', ['e', 'T'], True, 'k', 'e', '3', 'e', 1, ('g', 'x'), False)

letters = []
numbers = []

for i in data_tuple:

    if type(i) == str:
        if i.isdigit():
            numbers.append(int(i))
        else:
            letters.append(i)

    elif type(i) == list:
        for j in i:
            letters.append(j)

    elif type(i) == tuple:
        for j in i:
            letters.append(j)

    elif type(i) == bool:
        letters.append(i)

    else:
        numbers.append(i)


numbers.remove(6.13)

numbers.insert(2, 2)

numbers.sort(reverse=True)

letters = letters[::-1]

for i in range(len(letters)):
    if type(letters[i]) == str:
        letters[i] = letters[i].swapcase()

print(letters)
print(numbers)


