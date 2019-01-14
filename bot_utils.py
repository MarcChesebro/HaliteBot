import hlt

from hlt import constants

from hlt.positionals import Direction

import random


def choose_direction(game, ship):

    game_map = game.game_map

    directions = [Direction.North, Direction.South, Direction.East, Direction.West]
    direction = random.choice(directions)

    if ship.position.directional_offset(direction) == game.me.shipyard.position:
        directions.remove(direction)
        direction = random.choice(directions)

    return game_map.naive_navigate(ship, ship.position.directional_offset(direction))
