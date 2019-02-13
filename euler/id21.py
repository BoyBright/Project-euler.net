'''
    Amicable numbers
    Problem 21 
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
'''

def is_amicable(number):
    sum_ = 0
    for i in range(1,number):
        if number%i==0:
            sum_ += i 
    return sum_        


def main():
    result = []
    sum_of_all = 0
    for i in range(2,10000):
        # i = 220
        # sum1 = 284
        # sum2 = 220
        sum1 = is_amicable(i)   
        sum2 = is_amicable(sum1)

        if sum2==i and i!=sum1:
            result.append(i)
    print(result)
    print(sum(result))

if __name__ == '__main__':
    main()

