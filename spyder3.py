f = open("fruits.txt", "r")
g = open("fruits for X.txt", "w")
g.write("X = [\\\n")

h = open("fruits for Y.txt", "w")
h.write("Y = [")

f.readline()
while True:
    line = f.readline()
    if not line:
        g.write("]")
        h.write("]")
        break
    
    tmp = line.split()
    print(tmp)
    h.write(str(tmp[0]) + ", ")
    g.write("[" + str(float(tmp[2])) + ', ' + str(float(tmp[3])) + ', ' + str(float(tmp[4])) + ', ' + \
        str(float(tmp[5])) +"], \\" +"\n")
    

f.close()
g.close()