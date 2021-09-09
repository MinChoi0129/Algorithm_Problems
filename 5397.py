# 시간 초과 해결 필요, 1339도 풀자!
t = int(input())

class Cursor:
    
    def __init__(self, orders):
        self.index = 0
        self.orders = orders
        self.password = []

    def Move_or_Erase(self, cmd):
        if cmd == "<":
            if self.index > 0:
                self.index -= 1
        elif cmd == ">":
            if self.index != len(self.password):
                self.index += 1
        elif cmd == "-":
            if self.index != 0:
                self.password.pop(self.index -1)
                self.index -= 1
        else:
            self.password.insert(self.index, cmd)
            self.index += 1

    def getPassword(self):
        return ''.join(self.password)

for _ in range(t):
    typing = Cursor(input())
    for cmd in typing.orders:
        typing.Move_or_Erase(cmd)
    print(typing.getPassword())