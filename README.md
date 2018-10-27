# Connect Four Challenge Python Client ![Build Status](https://travis-ci.org/lakermann/connect-four-challenge-client-python.svg)
This is a Python client for the [connect four challenge server](https://github.com/lakermann/connect-four-challenge-server).
This client allows you to easily develop a bot for the connect four challenge.

To run the client you need Python 3.x and the library [requests](http://docs.python-requests.org/).

> pip install requests


## Getting started

Clone this repository and start the [run_game.py](run_game.py) script:

``` python

NUMBER_OF_GAMES = 1_000
SERVER_URL = "http://localhost:8080"


def main():
    logging.getLogger().setLevel(logging.INFO)
    executor = ThreadPoolExecutor(max_workers=2)

    client = ConnectFourClient(SERVER_URL)

    strategy = RandomPlayerStrategy()

    future1 = executor.submit(
        GameRunner(client=client, player_id='Alice', strategy=strategy, number_of_games=NUMBER_OF_GAMES).run)
    future2 = executor.submit(
        GameRunner(client=client, player_id='Bob', strategy=strategy, number_of_games=NUMBER_OF_GAMES).run)

    while not future1.done() and not future2.done():
        time.sleep(1)

    logging.info('Done!')


if __name__ == '__main__':
    main()

```

## Implement your own bot

To implement your own bot you need to provide an implementation of the
[GameStrategy](api/strategy.py) class:

``` python

class GameStrategy:
    def drop_disc(self, board):
        raise NotImplementedError("Please Implement this method")

    def win(self, board):
        pass

    def loose(self, board):
        pass

    def draw(self, board):
        pass


class MyStrategy(GameStrategy):
    def drop_disc(self, board):
        return random.choice([0,1,2,3,4,5,6])
```