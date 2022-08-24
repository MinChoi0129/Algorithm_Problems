class Piece:
    def __init__(self, piece):
        self.piece = piece
        
    def isPerfectPiece(self):
        is_all_same, same_type = True, self.piece[0][0]
        for line in self.piece:
            for element in line:
                if element != same_type: return False
        return is_all_same

    def getFourPieces(self):
        size = len(self.piece)
        left_up_piece, right_up_piece, left_down_piece, right_down_piece = [], [], [], []
        
        for row in range(size // 2):
            left_up_piece.append([self.piece[row][i] for i in range(size // 2)])
            right_up_piece.append([self.piece[row][i] for i in range(size // 2, size)])
            
        for row in range(size // 2, size):
            left_down_piece.append([self.piece[row][i] for i in range(size // 2)])
            right_down_piece.append([self.piece[row][i] for i in range(size // 2, size)])
        
        # return Piece Objects
        return [Piece(left_up_piece), Piece(left_down_piece), Piece(right_up_piece), Piece(right_down_piece)] 
        
    def getTypeOfPerfectPiece(self):
        if self.isPerfectPiece(): return 'white' if int(self.piece[0][0]) == 0 else 'blue'
        else: raise Exception('완벽한 조각이 아닙니다.')

n = int(input())
box = [Piece([input().split() for _ in range(n)])]
perfect_piece_counter = {'white' : 0, 'blue' : 0}
            
while box:
    piece = box.pop()
    try: perfect_piece_counter[piece.getTypeOfPerfectPiece()] += 1
    except:
        for new_piece in piece.getFourPieces():
            box.append(new_piece)
        

print(perfect_piece_counter['white'], perfect_piece_counter['blue'], sep = '\n')