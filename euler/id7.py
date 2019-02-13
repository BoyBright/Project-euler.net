'''
    10001st prime
    Problem 7 
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
'''
count = 0 
number = 2
in_find = input('prime_number position ')
find = int(in_find)
while True:
    check = 0
    for x in range(2,number+1):
        if number%x==0:
            check += 1
            if check==2:
                break

    if check == 1:
        count += 1 
    if count == find:
        print(find, 'prime number is', number)
        break
    number += 1