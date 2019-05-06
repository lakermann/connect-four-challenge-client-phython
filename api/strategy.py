import random


class GameStrategy:
    def drop_disc(self, board):
        raise NotImplementedError("Please Implement this method")

    def win(self, board):
        pass

    def lose(self, board):
        pass

    def draw(self, board):
        pass


class RandomPlayerStrategy(GameStrategy):
    def drop_disc(self, board):
        p = board.possible_moves()
        return random.choice(p)

    '''
    def win(self, board):
        print('win -> %s (%s)' % (board.disc_color, board.player_id))
        print(board)

    def lose(self, board):
        print('lose -> %s (%s)' % (board.disc_color, board.player_id))
        print(board)

    def draw(self, board):
        print('draw -> %s (%s)' % (board.disc_color, board.player_id))
        print(board)
    '''