import requests
from bs4 import BeautifulSoup

f = open("C:\\Users\\leemi\\Desktop\\민재\\백준\\Unsolved.txt", encoding='utf-8', mode = 'r')
g = open("C:\\Users\\leemi\\Desktop\\민재\\백준\\Unsolved-edit.txt", encoding='utf-8', mode = 'w')
wrongProblems = f.read().split("\n")
for i in range(len(wrongProblems)):
    wrongProblems[i] = int(wrongProblems[i])
wrongProblems.sort()

for i in range(len(wrongProblems)):
    num = str(wrongProblems[i])
    base = 'https://www.acmicpc.net/problem/'
    url = base + num
    response = requests.get(url)

    if response.status_code == 200:
        problem_title = str(BeautifulSoup(response.text, 'html.parser').select('#problem_title'))
        problem_title = problem_title[problem_title.index('>') + 1 : problem_title.index('</')]
        g.write(num + ' - ' + problem_title + '\n')

    else:
        print(response.status_code)