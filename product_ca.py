#! python3

def product(seq):
    total = 1
    for x in seq:
        total *= x
        
    return total



seq = [4,5,5]
print(product(seq))
