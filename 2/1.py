from helper import getData

data = getData()

'''
A = Rock
B = Paper
C = Scissors

X = Rock 1
Y = Paper 2
Z = Scissors 3

lost = 0
draw = 3
win = 6

A Y -> 6 + 2 = 8
B X -> 0 + 1 = 1
C Z -> 3 + 3 = 6
= 15
'''

score = 0
scoring = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
table = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}

for turn in data:
    enemy, you = turn.split()
    score += scoring[you]
    score += table[turn]

print(score)