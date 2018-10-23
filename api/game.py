import time


class GameRunner:

    POLLING_IN_SEC = 0

    def __init__(self, client, player_id, strategy, number_of_games):
        self._client = client
        self._player_id = player_id
        self._strategy = strategy
        self._number_of_games = number_of_games

    def run(self):

        win = 0
        draw = 0

        try:

            for i in range(self._number_of_games):

                join_state = self._client.join(player_id=self._player_id)

                # join a game
                while True:
                    if 'gameId' in join_state:
                        break

                    join_state = self._client.join(player_id=self._player_id)
                    time.sleep(self.POLLING_IN_SEC)

                game_id = join_state['gameId']

                # play a game
                game_state = self._client.game_state(game_id=game_id)
                disc_color = self._get_my_disc_color(game_state=game_state)

                while self._is_game_finished(game_state) is False:

                    game_state = self._client.game_state(game_id=game_id)

                    board = Board(board=game_state['board'], disc_color=disc_color, player_id=self._player_id)

                    if self._is_my_turn(game_state=game_state):
                        column = self._strategy.drop_disc(board=board)
                        self._client.drop_disc(game_id=game_id, player_id=self._player_id, column=column)
                    else:
                        time.sleep(self.POLLING_IN_SEC)


                # game finished
                board = Board(board=game_state['board'], disc_color=disc_color, player_id=self._player_id)

                winner = game_state['winner']

                if winner is None:
                    self._strategy.draw(board)
                    draw += 1

                if winner == self._player_id:
                    self._strategy.win(board)
                    win += 1
                else:
                    self._strategy.loose(board)

            print('games %i, win %i, draw %i, player %s' % (self._number_of_games, win, draw, self._player_id))

        except Exception as e:
            print(e)

    def _is_game_finished(self, game_state):
        return game_state['finished'] is True

    def _get_my_disc_color(self, game_state):
        players = game_state['players']

        for p in players:
            if p['playerId'] == self._player_id:
                return p['disc']

    def _is_my_turn(self, game_state):
        return game_state['currentPlayerId'] == self._player_id


class Board:
    BOARD_RED = 'RED'
    BOARD_YELLOW = 'YELLOW'
    BOARD_EMPTY = 'EMPTY'

    def __init__(self, board, disc_color, player_id):
        self.board = board
        self.disc_color = disc_color
        self.player_id = player_id

    def columns(self):
        if len(self.board) == 0:
            return 0

        return len(self.board[0])

    def rows(self):
        return len(self.board)

    def get_column(self, n):
        columns = []
        for row in self.board:
            columns.append(row[n])

        return columns

    def free_space_column(self, n):
        column = self.get_column(n)
        free_space = 0
        for c in column:
            if c == 'EMPTY':
                free_space += 1

        return free_space

    def free_space_row(self, n):
        row = self.get_row(n)
        free_space = 0
        for r in row:
            if r == 'EMPTY':
                free_space += 1

        return free_space

    def get_row(self, n):
        return self.board[n]

    def possible_columns(self):
        c = self.columns()
        out = []
        for i in range(c):
            if self.free_space_column(i) > 0:
                out.append(i)
        return out

    def state(self):

        items = [item for sublist in self.board for item in sublist]
        out = []

        for i in items:

            if i == self.BOARD_EMPTY:
                out.append(' ')
            elif i == self.BOARD_RED:
                out.append('R')
            else:
                out.append('Y')
        return ''.join(out)

    def __str__(self):
        board = self.state()
        c = self.columns()
        out = ' | 0 | 1 | 2 | 3 | 4 | 5 | 6 |\n'
        out += ' -----------------------------\n'
        for i in range(len(board)):
            if i == 0:
                out += ' | ' + board[i]
            elif i % c == 0:
                out += ' | ' + '\n'
                out += ' | ' + board[i]

            else:
                out += ' | ' + board[i]

        out += ' | '
        return out
