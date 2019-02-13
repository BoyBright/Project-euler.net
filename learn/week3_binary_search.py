'''
    Find a number 
'''
from random import randint

data = [x for x in range(101)]
answer = randint(0, 100)
while True:
    guess_number = input("Enter a number : ")
    x = int(guess_number)

    if x==answer:
        print("=== Correct Answer ===")
        break
    else:
        print("Too High" if x>answer else "Too Low") 
print("GAME OVER !!!")