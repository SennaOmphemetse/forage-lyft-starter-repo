from Car import Car
from Battery.nubbin_battery import NubbinBattery
from Battery.spindler_battery import SpindlerBattery
from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        Engine = CapuletEngine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery(current_date, last_service_date)
        Car = Car(Engine, Battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery(current_date, last_service_date)
        Car = Car(Engine, Battery)
        return Car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        Engine = SternmanEngine(warning_light_is_on)
        Battery = SpindlerBattery(current_date, last_service_date)
        Car = Car(Engine, Battery)
        return Car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        Battery = NubbinBattery(current_date, last_service_date)
        car = Car(Engine, Battery)
        return Car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        Car = Car(Engine, Battery)
        return Car
