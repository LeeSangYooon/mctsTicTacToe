from Game import Game

NONE = 0
X = 1
O = 2
int_to_char = {NONE:'.', X:'X', O:'O'}
check_list = [[[0, 0], [0, 1], [0, 2]],
              [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[2, 0], [1, 1], [0, 2]]]

# 틱택토는 게임
class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = X
        self.move_number = 0

    def set_color(self, position, color):
        self.board[position[1]][position[0]] = color

    def get_color(self, position):
        return self.board[position[1]][position[0]]

    def result(self):
        for check in check_list:
            first = self.get_color(check[0])
            if first != NONE and all([self.get_color(pos) == first for pos in check]):
                self.end = True
                return first
        if self.move_number == 9:
            self.end = True
            return 0
        return None

    def move(self, position):
        self.set_color(position, self.turn)
        self.turn = 3 - self. turn
        self.move_number += 1
        return self.result()
    def get_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                move = (i, j)
                if self.get_color(move) == NONE:
                    moves.append(move)
        return moves
    def show(self):
        for line in self.board.__reversed__():
            print(''.join([int_to_char[cell] for cell in line]))
        print()

