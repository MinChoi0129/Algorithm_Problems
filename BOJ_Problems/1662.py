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


def findPairBracketIndex(s: str, start_idx: int):
    stack = []
    for i in range(start_idx, len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            stack.pop()
            if not stack:
                return i

def recur(s: str):
    try:
        if not s: return 0
        int(s)
        return len(s)
    
    except:
        for i in range(len(s)):
            element = s[i]
            if element == '(':
                idx = findPairBracketIndex(s, i)
                new_s = len(s[:i-1]) + recur(s[i+1:idx]) * int(s[i-1]) + len(s[idx+1:])
                return new_s

statement = input()              
while '(' in statement:
    statement = recur(statement)
print(len(statement))