#! python3

def count(sequence,item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
    return total


seq = ['a','b','a','a']
mask = 'a'

print(count(seq,mask))
