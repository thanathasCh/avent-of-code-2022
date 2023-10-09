from helper import getData

data = getData('input2.txt')

'''
24 items per sack
2 parts
find the duplicate value
convert to somewhat ascii
sum them together
'''


def to_ord(letter):
    if ord(letter) in range(65, 92):
        return ord(letter) - 38  # uppercase 65 - 27 = 38
    else:
        return ord(letter) - 96  # lower case 97 - 1 = 96


result = 0

for i in data:
    half = len(i) // 2
    m = {x: '' for x in i[:half]}
    second = i[half:]

    for j in second:
        if m.get(j) is not None:
            result += to_ord(j)
            break

print(result)