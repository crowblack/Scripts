#! python3

def digit_sum(n):
    final = 0
    for y in n:
        final = final + int(y)
    return final


num = input("Enter a number: ")
print(digit_sum(num))
