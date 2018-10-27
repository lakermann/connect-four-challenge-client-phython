from api import GameRunner
from unittest.mock import MagicMock


def test_helper_is_finished():

    g = GameRunner(client=None, player_id='foo', strategy=None, number_of_games=0)

    game_state = {}

    assert g._is_game_finished(game_state) is False

    game_state = {'other': None}

    assert g._is_game_finished(game_state) is False

    game_state = {'finished': None}

    assert g._is_game_finished(game_state) is False

    game_state = {'finished': False}

    assert g._is_game_finished(game_state) is False

    game_state = {'finished': True}

    assert g._is_game_finished(game_state) is True


def test_helper_is_get_my_disc_color():
    g = GameRunner(client=None, player_id='foo', strategy=None, number_of_games=0)

    game_state = {}

    assert g._get_my_disc_color(game_state) is None

    game_state = {'players': None}

    assert g._get_my_disc_color(game_state) is None

    game_state = {'players': []}

    assert g._get_my_disc_color(game_state) is None

    game_state = {'players': [{'playerId': 'foo', 'disc': 'RED'}, {'playerId': 'foo2', 'disc': 'YELLOW'}]}

    assert g._get_my_disc_color(game_state) == 'RED'


def test_is_my_turn():
    g = GameRunner(client=None, player_id='foo', strategy=None, number_of_games=0)

    game_state = {}

    assert g._is_my_turn(game_state) is None

    game_state = {'currentPlayerId': 'Alice'}

    assert g._is_my_turn(game_state) is False

    game_state = {'currentPlayerId': 'foo'}

    assert g._is_my_turn(game_state) is True
