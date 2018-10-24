from api import Board


def test_empty():
    g = Board(board=[], disc_color='RED', player_id='Alice')
    assert g.rows() == 0
    assert g.columns() == 0
    assert g.free_space() == 0
    assert g.possible_moves() == []
    assert g.disc_color == 'RED'
    assert g.player_id == 'Alice'


def test_simple_board():
    b = [['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.rows() == len(b)
    assert g.columns() == len(b[0])
    assert g.free_space() == len(b) * len(b[0])
    assert g.possible_moves() == [0, 1]
    assert g.shape() == (len(b), len(b[0]))


def test_free_space():
    b = [['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.free_space() == 6
    assert g.free_space_row(0) == 2
    assert g.free_space_row(1) == 2
    assert g.free_space_row(2) == 2
    assert g.free_space_column(0) == 3
    assert g.free_space_column(1) == 3

    b = [['YELLOW', 'EMPTY'], ['YELLOW', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.free_space() == 1
    assert g.free_space_row(0) == 1
    assert g.free_space_row(1) == 0
    assert g.free_space_row(2) == 0
    assert g.free_space_column(0) == 0
    assert g.free_space_column(1) == 1

    b = [['EMPTY', 'RED'], ['EMPTY', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.free_space() == 2
    assert g.free_space_row(0) == 1
    assert g.free_space_row(1) == 1
    assert g.free_space_row(2) == 0
    assert g.free_space_column(0) == 2
    assert g.free_space_column(1) == 0

    b = [['YELLOW', 'RED'], ['YELLOW', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.free_space() == 0
    assert g.free_space_row(0) == 0
    assert g.free_space_row(1) == 0
    assert g.free_space_row(2) == 0
    assert g.free_space_column(0) == 0
    assert g.free_space_column(1) == 0


def test_possible_moves_columns():
    b = [['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.possible_moves() == [0, 1]
    assert g.free_space_column(0) == 3
    assert g.free_space_column(1) == 3
    assert g.free_space() == g.free_space_column(0) + g.free_space_column(1)
    assert g.free_space_row(0) == 2
    assert g.free_space_row(1) == 2
    assert g.free_space_row(2) == 2

    b = [['YELLOW', 'EMPTY'], ['YELLOW', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.possible_moves() == [1]
    assert g.free_space_column(0) == 0
    assert g.free_space_column(1) == 1
    assert g.free_space() == g.free_space_column(0) + g.free_space_column(1)
    assert g.free_space_row(0) == 1
    assert g.free_space_row(1) == 0
    assert g.free_space_row(2) == 0

    b = [['EMPTY', 'RED'], ['YELLOW', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.possible_moves() == [0]
    assert g.free_space_column(0) == 1
    assert g.free_space_column(1) == 0
    assert g.free_space() == g.free_space_column(0) + g.free_space_column(1)
    assert g.free_space_row(0) == 1
    assert g.free_space_row(1) == 0
    assert g.free_space_row(2) == 0

    b = [['YELLOW', 'RED'], ['YELLOW', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.possible_moves() == []
    assert g.free_space_column(0) == 0
    assert g.free_space_column(1) == 0
    assert g.free_space() == g.free_space_column(0) + g.free_space_column(1)
    assert g.free_space_row(0) == 0
    assert g.free_space_row(1) == 0
    assert g.free_space_row(2) == 0

    b = [['RED', 'RED'], ['EMPTY', 'RED'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.possible_moves() == [0, 1]
    assert g.free_space_column(0) == 2
    assert g.free_space_column(1) == 1
    assert g.free_space() == g.free_space_column(0) + g.free_space_column(1)
    assert g.free_space_row(0) == 0
    assert g.free_space_row(1) == 1
    assert g.free_space_row(2) == 2


def test_get():
    b = [['1', '2'], ['3', '4'], ['5', '6']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.get_row(0) == b[0]
    assert g.get_row(1) == b[1]
    assert g.get_row(2) == b[2]
    assert g.get_column(0) == [b[0][0], b[1][0], b[2][0]]
    assert g.get_column(1) == [b[0][1], b[1][1], b[2][1]]


def test_board_state():
    b = [['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.state() == 'EEEEEE'

    b = [['EMPTY', 'RED'], ['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')
    assert g.state() == 'EREEEE'

    b = [['EMPTY', 'RED'], ['EMPTY', 'EMPTY'], ['EMPTY', 'YELLOW']]
    g = Board(board=b, disc_color='YELLOW', player_id='Alice')
    assert g.state() == 'EREEEY'

    b = [['EMPTY', 'RED'], ['EMPTY', 'EMPTY'], ['EMPTY', 'YELLOW']]
    g = Board(board=b, disc_color='YELLOW', player_id='Alice')
    assert g.state() == 'EREEEY'

    b = [['YELLOW', 'YELLOW'], ['YELLOW', 'YELLOW'], ['YELLOW', 'YELLOW']]
    g = Board(board=b, disc_color='YELLOW', player_id='Alice')
    assert g.state() == 'YYYYYY'

    b = [['RED', 'RED'], ['RED', 'RED'], ['RED', 'RED']]
    g = Board(board=b, disc_color='YELLOW', player_id='Alice')
    assert g.state() == 'RRRRRR'


def test_board_to_str():
    b = [['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')

    assert str(g) == ''' | 0 | 1 |
 ---------
 | E | E | 
 | E | E | 
 | E | E | '''

    b = [['RED', 'YELLOW', 'EMPTY'],
         ['EMPTY', 'EMPTY', 'EMPTY'],
        ['EMPTY', 'EMPTY', 'EMPTY'],
        ['EMPTY', 'EMPTY', 'EMPTY'],
        ['EMPTY', 'EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')

    assert str(g) == ''' | 0 | 1 | 2 |
 -------------
 | R | Y | E | 
 | E | E | E | 
 | E | E | E | 
 | E | E | E | 
 | E | E | E | '''

    b = [['RED', 'YELLOW', 'EMPTY', 'EMPTY'],
         ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'],
        ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'],
        ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'],
        ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')

    assert str(g) == ''' | 0 | 1 | 2 | 3 |
 -----------------
 | R | Y | E | E | 
 | E | E | E | E | 
 | E | E | E | E | 
 | E | E | E | E | 
 | E | E | E | E | '''

    b = [['RED', 'YELLOW', 'EMPTY', 'EMPTY', 'YELLOW', 'EMPTY'],
         ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'RED', 'EMPTY']]
    g = Board(board=b, disc_color='RED', player_id='Alice')

    assert str(g) == ''' | 0 | 1 | 2 | 3 | 4 | 5 |
 -------------------------
 | R | Y | E | E | Y | E | 
 | E | E | E | E | R | E | '''
