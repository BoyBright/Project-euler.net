'''
    Hash Function
'''

# battery = {
#     'A': '5V',
#     'AA': '4.5V',
#     'AAA': '3.5V'
#     }
# x = input('Enter a battery type : ')
# print(battery.get(x, '0V'))

voted = dict()
for i in range(4):
    voter = input('Type your name: ')
    if voted.get(voter):
        print('Get out of here')
    else:
        voted[voter] = 1
        print('Thank for vote!!')