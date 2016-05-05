#! python3

def median(seq):
    seq = sorted(seq)
    if len(seq) % 2 == 0:
        num_a = seq[int((len(seq)/2)-1)]
        print(num_a)
        num_b = seq[int(len(seq)/2)]
        print(num_b)
        return (num_a + num_b) / 2.0

    else:
        i = int(len(seq)/2)
        return seq[i]


seq = [4,5,5,4]
print(median(seq))
        

    
