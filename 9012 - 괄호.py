import sys as s
t = int(s.stdin.readline().rstrip())

def vps(string):
    calc = 0
    for ch in string:
        if ch == "(":
            calc += 1 
        else:
            calc -= 1
        if calc < 0:
            return "NO"
    if calc == 0:
        return "YES"
    else:
        return "NO"

bracket = []
for i in range(t):
    bracket.append(s.stdin.readline().rstrip())
    print(vps(bracket[i]))