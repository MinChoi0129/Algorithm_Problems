from math import log2, floor

def isExpressiveTree(txt):
    txt_len = len(txt)
    mid_idx = txt_len // 2
    
    if txt_len == 1 or '1' not in txt or '0' not in txt: return True
    elif txt[mid_idx] == '0': return False
    else: return isExpressiveTree(txt[:mid_idx]) and isExpressiveTree(txt[mid_idx + 1:])

def solution(dec_numbers):
    answer = []
    for dec_number in dec_numbers:
        bin_number = bin(dec_number)[2:]
        min_length = 2 ** (floor(log2(len(bin_number))) + 1) - 1
        binary_searching_txt = bin_number.zfill(min_length)
        answer.append(1 if isExpressiveTree(binary_searching_txt) else 0)
        
    return answer