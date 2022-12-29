def findPairBracketIndex(s: list, start_idx: int):
    stack_count = 0
    for i in range(start_idx, len(s)):
        if s[i] == '(': stack_count += 1
        elif s[i] == ')': stack_count -= 1            
        if stack_count == 0: return i
    
def getLengthOfSubstring(s: list):
    if '(' not in s: return len(s)
    try:
        result, i, last_i = 0, 0, len(s) - 1
        while i <= last_i:
            if s[i] == '(':
                pair_bracket_index = findPairBracketIndex(s, i)
                result += int(s[i-1]) * getLengthOfSubstring(s[i+1: pair_bracket_index])
                i = pair_bracket_index
            elif s[i] != ')' and s[i+1] != '(': result += 1
            i += 1
    except: result += 1
    return result

print(getLengthOfSubstring(list(input())))