from typing import Dict
from Drone import Drone
from tools import x_y_input
from Wolverine import Wolverine
from Hunter import Hunter
from consts import DroneActions, DroneNames, ACTIONS

current_drone_id = 1
drones: Dict[int, Drone] = {
    current_drone_id: Wolverine(drone_id=current_drone_id, max_flight_speed=6, payload_weight=2),

}


def main_function():
    """
       the main app function
    """
    while True:
        try:
            action = action_user_input()
            if action == DroneActions.GOTO.value:
                drone_id = drone_id_user_input()
                x, y = x_y_input()
                drones[drone_id].goto(x, y)
            if action == DroneActions.LAND.value:
                drone_id = drone_id_user_input()
                drones[drone_id].land()
            if action == DroneActions.TAKEOFF.value:
                drone_id = drone_id_user_input()
                drones[drone_id].takeoff()
            if action == DroneActions.LIST.value:
                print_drones()
            if action == DroneActions.EXIT.value:
                for ID in drones.keys():
                    if not drones[ID].on_ground:
                        raise Exception(f"drone number {ID} need to land before ending flight")
                break
        except Exception as e:
            print(f'{e}\n')


def add_drones(drone_name: str, max_flight_speed: int, payload_weight: int = 0):
    """
       function that add drones to list

       Args: drone_name: str, max_flight_speed: int, payload_weight: int = 0
    """
    global current_drone_id
    current_drone_id += 1
    if drone_name == DroneNames.WOLVERINE.value:
        drones[current_drone_id] = Wolverine(drone_id=current_drone_id, max_flight_speed=max_flight_speed,
                                             payload_weight=payload_weight)
    elif drone_name == DroneNames.HUNTER.value:
        drones[current_drone_id] = Hunter(drone_id=current_drone_id, max_flight_speed=max_flight_speed)


def print_drones():
    """
       function that print drones list
    """
    print("Drones list:")
    for drone in drones.values():
        if isinstance(drone, Wolverine):
            print("drone_id:", drone.drone_id, ",",
                  "DRONE_NAME:", "Wolverine", ","
                                              "MAX_FLIGHT_SPEED:", drone.max_flight_speed, ","
                                                                                           "PAYLOAD_WEIGHT:",
                  drone.payload_weight)
        elif isinstance(drone, Hunter):
            print("drone_id:", drone.drone_id, ",",
                  "DRONE_NAME:", "Hunter", ","
                                           "MAX_FLIGHT_SPEED:", drone.max_flight_speed)

    print('')


def action_user_input():
    """
       function that get the user action input

       Returns: action: str
    """
    input_str = 'Enter action name:\n'
    for action in ACTIONS:
        input_str += f'{action}\n'
    action = input(input_str)
    if action not in ACTIONS:
        raise ValueError("Error: unrecognized action.")
    return action


def drone_id_user_input():
    """
        function that get the user id input

        Returns: id: int
    """
    drone_id = input('Enter drone id between 1-9:\n')
    check_drone_id_input(drone_id)
    return int(drone_id)


def check_drone_id_input(drone_id: str):
    """
       function that checks the drone id input

       Args: drone_id: str
    """
    try:
        drone_id = int(drone_id)
    except ValueError:
        raise ValueError("Error: drone_id must be integer.")
    if int(drone_id) < 0 or int(drone_id) > 9:
        raise ValueError("Error: drone_id need to be between 1-9.")
    if drone_id not in drones:
        raise AttributeError("Error: drone_id number does not exist.")


if __name__ == '__main__':
    main_function()
