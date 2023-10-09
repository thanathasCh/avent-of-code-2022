def getData(txt='input.txt'):
    with open(txt, 'r') as f:
        return f.read().split('\n')