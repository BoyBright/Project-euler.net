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

