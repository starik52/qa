class Car:

    def __init__(self, color, consumption, tank_volume, mileage = 0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False


