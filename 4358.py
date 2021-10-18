import sys
input = lambda : sys.stdin.readline().rstrip()

trees = dict()
count = 0

while True:
    get_tree = input()
    if not get_tree:
        break
    
    if get_tree in trees:
        trees[get_tree] += 1
    else:
        trees[get_tree] = 1
        
    count += 1

for tree_name in sorted(trees.keys()):
    print("%s %.4f" % (tree_name, trees[tree_name] / count *100))