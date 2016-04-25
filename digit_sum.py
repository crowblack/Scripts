#! python3

def digit_sum(n):
    total = []
    final = 0
    for x in n:
        total.append(x)
    for y in total:
        final = final + int(y)
    return final


num = input("Enter a number: ")
print(digit_sum(num))
