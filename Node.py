from math import sqrt, log

ROOT2 = sqrt(2)
class Node:
    def __init__(self, parent, game):
        self.parent = parent
        self.game = game
        self.win = 0
        self.n = 0
        self.is_leaf_node = True
        self.children = []
        self.movements = []
        self.move = None
    def uct(self, t):
        return self.win / self.n + ROOT2 *  sqrt(log(t) / self.n)
