#! python3

def remove_duplicates(seq):
    final_val = []
    for i in seq:
        if i not in final_val:
            final_val.append(i)

    return final_val


seq = [1,1,2,2,3,4,1,3,7]
out = remove_duplicates(seq)
for i in out:
    print(i)
