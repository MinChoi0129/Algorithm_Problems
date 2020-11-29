def print_ans(seq_num):
    sequence = [1, 1, 2]
    if seq_num in [0, 1, 2]:
        print(sequence[seq_num])
    else:
        for _ in range(seq_num - 2):
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
        print(sequence[-1])
    
T = int(input())
for _ in range(T):
    print_ans(int(input()))