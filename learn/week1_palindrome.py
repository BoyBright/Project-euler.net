def is_palindrome(data):
    temp = str(data)
    revers_data = temp[::-1]
    return True if temp == revers_data else False

def main():
    first = 999 
    max_number = 0
    while first > 100: 
        second = first
        while second > 100: 
            multiple_data = first*second
            if is_palindrome(multiple_data) and multiple_data > max_number:
                max_number = multiple_data
            second-=1    
        first-=1
    print(max_number)    
    print('END')    

if __name__ == '__main__':
    main()

