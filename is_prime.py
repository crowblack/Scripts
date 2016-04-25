#! python3

def is_prime(x):
    if x < 2:
        return False
    for n in range(2,x):
        if x%n == 0 :
            return False
    return True

num = input("Enter a number to check: ")
print(is_prime(int(num)))
        
