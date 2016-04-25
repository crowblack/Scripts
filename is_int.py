#! python3

def is_int(x):
    if x % 1 == 0:
        print('True')
    else:
        print('False')

n = input("Enter a number: ")
is_int(float(n))
          
