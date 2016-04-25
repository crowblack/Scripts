#! python3
def factorial(x):
    hold = []
    result = 1
    for i in range(1,x+1):
        hold.append(i)
    for j in hold:
        result = result * j
    return result


num = input("Enter a number: ")
print(factorial(int(num)))
