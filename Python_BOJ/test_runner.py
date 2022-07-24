main = __import__("1195")

def test():
    for i in range(3):
        for j in range(10):
            if i == j == 0: continue
            if i*j >= 16: break
            print("* TEST " + str(i) + str(j))
            problem_f = open("E:/Downloads/tests/tests/kickdown/tests/" + str(i) + str(j), 'r')
            answer_f = open("E:/Downloads/tests/tests/kickdown/tests/" + str(i) + str(j) + '.a', 'r')
            
            inputs = problem_f.readlines()
            answer = int(answer_f.readline().rstrip())
            
            line_a, line_b = list(inputs[0].rstrip()), list(inputs[1].rstrip())
            
            my_answer = main.main((line_a, line_b))
            if my_answer != answer: print("FAILED", my_answer, answer)
            else: print("OK")
            
            problem_f.close()
            answer_f.close()

test()