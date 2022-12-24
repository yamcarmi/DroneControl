from Drone import Drone


class Wolverine(Drone):
    def __init__(self, drone_id, max_flight_speed, payload_weight):
        super().__init__(drone_id, max_flight_speed)
        self.payload_weight = payload_weight
        self.calc_speed_by_weight()

    def calc_speed_by_weight(self):
        """
            function that calculate the speed by weight
        """
        self.max_flight_speed = round(self.max_flight_speed * (1 / self.payload_weight))
        if self.max_flight_speed < 1:
            self.max_flight_speed = 1
