from AI import AI
from TicTacToe import TicTacToe


game = TicTacToe()

def play_alone():
    while True:
        game.show()
        pos = list(map(int, input("move: ").split()))
        result = game.move(pos)
        if result:
            game.show()
            print(('X' if result == 1 else 'O') + ' won')
            break

def play_with_AI():

    while True:
        ai = AI(game=game)
        result = game.move(ai.next_movement())
        game.show()
        if result is not None:
            if result == 1:
                print ('X WON')
            elif result == 2:
                print('O WON')
            else:
                print('DRAWN')
            break

play_with_AI()
