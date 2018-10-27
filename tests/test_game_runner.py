from api import GameRunner


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

