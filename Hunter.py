from Drone import Drone


class Hunter(Drone):
    def __init__(self, drone_id, max_flight_speed):
        super().__init__(drone_id, max_flight_speed)
