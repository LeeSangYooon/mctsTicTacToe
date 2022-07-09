#MCTS
from Node import Node
from random import choice
from copy import deepcopy
from Game import Game

class AI:
    def __init__(self, game):
        self.game = game
        self.root_node = Node(None, game=self.game)
        self.root_node.n = 1
        self.visits = 1000
        self.simulations = 1
        pass

    def selection(self):
        node = self.root_node
        while not node.is_leaf_node :
            # UCT 함수값이 가장 큰 자식 노드를 찾는다
            max_value, max_index = -1000, -1
            for i in range(len(node.children)):

                value = node.children[i].uct(node.n)
                if value > max_value:
                    max_value = value
                    max_index = i

            node = node.children[max_index]  # 자식 노드로 내려감
        return node

    def expansion(self, node):
        if node.game.end:
            self.back_propagation(node, node.game.result())
            return
        moves : list = node.game.get_moves()
        candidates = []
        for move in moves:
            if not move in node.movements:
                candidates.append(move)

        if candidates == []:
            node.game.show()

        choice_move = choice(candidates)


        new_game : Game = deepcopy(node.game)
        result = new_game.move(choice_move)

        new_node = Node(node, new_game)
        new_node.move = choice_move
        node.children.append(new_node)
        node.movements.append(choice_move)

        if len(moves) == len(node.movements):
            node.is_leaf_node = False
        if new_node.game.end:
            self.back_propagation(new_node, result)
            return
        self.simulation(new_node)

    def simulation(self, node):
        for i in range(self.simulations):
            simulation_game : Game = deepcopy(node.game)
            result = None
            while not simulation_game.end:
                result = simulation_game.move(choice(simulation_game.get_moves()))

            self.back_propagation(node, result)
        pass

    def back_propagation(self, last_node, result):
        node = last_node
        while True:  # Root Node 가 아닐때
            node.n += 1
            opposite_turn = 3 - node.game.turn

            if opposite_turn == result :  # 해당 노드가 이겼다면
                node.win += 1
            if result == 0:
                node.win += 0.5
            if node.parent is None:
                break
            node = node.parent # 역전파
        pass
    def next_movement(self):
        for i in range(self.visits):
            leaf_node = self.selection()
            self.expansion(leaf_node) # back_propagation 까지 수행
        m = 0
        best_child =None
        for child in self.root_node.children:
            if child.n > m:
                m = child.n
                best_child = child
        print(best_child.win / best_child.n)

        return best_child.move