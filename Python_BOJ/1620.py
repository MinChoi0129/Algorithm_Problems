import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemon = dict()
pokemon_l = []

for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = i
    pokemon_l.append(name)

for i in range(m):
    question = sys.stdin.readline().rstrip()
    
    if question.isdigit():
        print(pokemon_l[int(question) - 1])
    else:
        print(pokemon[question])