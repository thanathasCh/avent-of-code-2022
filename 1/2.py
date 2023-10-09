with open('input.txt', 'r') as f:
    data = f.read()

lst_clr = []

curr_value = 0
for txt in data.split('\n'):
    if txt == '':
        lst_clr.append(curr_value)
        curr_value = 0
    else:
        curr_value += int(txt)

print(sum(sorted(lst_clr, reverse=True)[:3]))
