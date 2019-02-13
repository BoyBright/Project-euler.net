'''
    Smallest multiple
    Problem 5 
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
is_divisible = lambda x, y: x%y==0

in_num = input('Smallest multiple for ')
number = int(in_num)
smallest_number = 20
found = 0
while True:
    for x in range(11,number+1):
        if is_divisible(smallest_number, x):
            found = 1 
        else:
            found = 0
            break    
    if found==1:
        print('smallest_number is',smallest_number)
        break
    smallest_number += 1
