def is_prime(num):
    for i in range(2,num):
       if num % i == 0:
           return False
    return True

def find_all_prime(start,end):
    all_prime_numbers = []
    for i in range(start, end +1):
        if is_prime(i):
            all_prime_numbers.append(i)
    return all_prime_numbers

print('your prime number is :',find_all_prime(5,100))