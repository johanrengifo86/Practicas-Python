a = [1061691248, 10545899, 34553167]

new_list = []
for num in a:
    new_list.append('{:,}'.format(num))

print(new_list)

