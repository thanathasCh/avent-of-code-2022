from helper import getData

data = getData()
'''
A = Rock
B = Paper
C = Scissors

Rock 1
Paper 2
Scissors 3

X lost = 0
Y draw = 3
Z win = 6
'''

score = 0
scoring = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
table = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1,
}

for turn in data:
    enemy, you = turn.split()
    score += scoring[you]
    score += table[turn]

print(score)