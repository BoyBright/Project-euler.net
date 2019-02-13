'''
    Lattice paths
    Problem 15 
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
'''
x = input('Enter grid scale: ')
num = int(x)+1
a = [ [0]*num for _ in range(num) ]
value = []
for row in range(num):
    for col in range(num):            
        if row==0:
            a[0][col] = 1
        elif col==0:
            a[row][0] = 1
        else:     
            a[row][col] = a[row-1][col] + a[row][col-1]

print(a[num-1][num-1])
