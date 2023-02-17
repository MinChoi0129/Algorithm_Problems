ROOT_2 = 2 ** 0.5

class Square:
    def __init__(self, side_length: int, before_square: "Square"):
        self.side_length = side_length
        self.height = self.side_length * ROOT_2
        self.x = self.calculateX(before_square)

    def __le__(self, other: "Square"):
        return True if self.side_length <= other.side_length else False
    
    def calculateX(self, before_square: "Square"):
        if not before_square: return self.side_length / ROOT_2


        

squares: list[Square] = [None]

largest_bottom_x = None
largest_right_x = None

n = int(input())
for size in map(int, input().split()):
    squares.append(Square(size, squares[-1]))

print()
