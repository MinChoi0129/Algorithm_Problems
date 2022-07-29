# main = __import__("10875")

def test():
    texts = open("E:/Downloads/tests/abc/abcd.txt", 'r')
    
    input_txt = ""
    while True:
        line = texts.readline().rstrip()
        if line == "EOF": break
        if line.startswith('TestCase'):
            print(line)
        input_txt += line
        if not line:
            answer = int(texts.readline())
        
    
    texts.close()
test()