import os
dir = '\\\\smr00-nas\\hide\\'
asd = ''

with open(f'{dir}users.txt', 'r', encoding='UTF-16') as users:
    with open(f'{dir}new_users.csv', 'w', encoding='UTF-16') as new_users:
        all_users = users.readlines()
        for i in all_users:
            # print(i.split('  '))
            trololo = i.split('  ')
            for t in trololo:
                if t != '':
                    new_users.write(f'{t}\t')
    #     n = len(i)
    #
    #
    #

