f = open("glass.csv", "r")
g = open("glass.txt", "w")

f.readline()

while True:
    line = f.readline()
    if not line:
        break
    
    g.write("[" + line + "],\\" + "\n")


f.close()
g.close()