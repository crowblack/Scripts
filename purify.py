#! python3

def purify(dump):
    result = []
    for x in dump:
        if x % 2 == 0:
            result.append(x)

    return result
    
