with open('input.txt', 'r') as f:
    data = f.read()


max_value = 0
curr_value = 0

for txt in data.split('\n'):
    if txt == '':
        max_value = max(max_value, curr_value)
        curr_value = 0
    else:
        curr_value += int(txt)

print(max_value)