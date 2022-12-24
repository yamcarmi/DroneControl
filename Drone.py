import random as rd
from typing import List

from tools import validate_drone_input_x_y


class Drone:
    def __init__(self, drone_id: int, max_flight_speed: int):
        self.drone_id = drone_id
        self.max_flight_speed = max_flight_speed
        self.current_location = {'x': self.random_current_location(), 'y': self.random_current_location()}
        self.on_ground = True

    def get_location(self):
        """
        function that return the current location x,y

        Returns: self.current_location: Dict(str, int)
        """
        return self.current_location

    @staticmethod
    def random_current_location():
        """
        function that randomly pick numbers between 1-100, for the x,y start location

        Returns:
            number between 1-100(int)
        """
        return rd.randint(1, 100)

    def set_location(self, x, y):
        """
        function that set the current location x,y

        Args: x: int, y: int
        """
        validate_drone_input_x_y(x, y)
        self.current_location['x'] = int(x)
        self.current_location['y'] = int(y)

    def takeoff(self):
        """
        function that taking off the drone to air
        """
        if not self.on_ground:
            raise Exception("Error: cant takeoff, need to land first. ")
        print("Taking off\n")
        self.on_ground = False

    def land(self):
        """
        function that landing the drone
        """
        if self.on_ground:
            raise Exception("Error: cant land, need to takeoff first. ")
        print("Landing\n")
        self.on_ground = True

    def goto(self, x: int, y: int):
        """
        function that printing the drone path to target location

        Args: : x: int, y: int
        """
        is_positive_x = x > self.current_location['x']
        is_positive_y = y > self.current_location['y']
        self.check_goto(x, y)
        print('current location: ', self.current_location, '\ntarget location: ', {'x': x, 'y': y})
        steps_delta_x = abs(x - self.current_location['x'])
        steps_delta_y = abs(y - self.current_location['y'])
        x_reminder = steps_delta_x % self.max_flight_speed != 0
        y_reminder = steps_delta_y % self.max_flight_speed != 0
        path: List[str] = [f'({self.current_location["x"]},{self.current_location["y"]})']
        path.extend(self.calc_drone_path(steps_delta=steps_delta_x, is_positive=is_positive_x, reminder=x_reminder,
                                         target_location=x,
                                         axis='x'))
        path.extend(self.calc_drone_path(steps_delta=steps_delta_y, is_positive=is_positive_y, reminder=y_reminder,
                                         target_location=y,
                                         axis='y'))
        print('Drone path: ', path, '\n')

    def calc_drone_path(self, steps_delta: int, is_positive: bool, reminder: bool, target_location: int, axis: str):
        """
        function that printing that calculate the drone path to target location

        Args: steps_delta: int, is_positive: bool, reminder: bool, target_location: int, axis: str

        Returns: path: List(str)
        """
        path = []
        for _ in range(steps_delta // self.max_flight_speed):
            step = self.max_flight_speed if is_positive else (self.max_flight_speed * -1)
            self.current_location[axis] += step
            path.append(f'({self.current_location["x"]},{self.current_location["y"]})')
        if reminder:
            self.current_location[axis] = target_location
            path.append(f'({self.current_location["x"]},{self.current_location["y"]})')
        return path

    def check_goto(self, x: int, y: int):
        """
        function that checks the goto function

        Args: x: int, y: int
        """
        if self.on_ground:
            raise Exception("Error: need to takeoff first. ")
        if x == self.current_location['x'] and y == self.current_location['y']:
            raise Exception("Error: already in target location,choose different location. ")
