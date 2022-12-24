from enum import Enum


class DroneActions(Enum):
    TAKEOFF = "takeoff"
    GOTO = "goto"
    LAND = "land"
    LIST = "list"
    EXIT = "exit"


ACTIONS = [item.value for item in DroneActions]


class DroneNames(Enum):
    WOLVERINE = "Wolverine"
    HUNTER = "Hunter"
