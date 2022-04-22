from abc import ABC, abstractmethod
import datetime
import math
import random

ACCELERATE = 20  # Accelerate processes in k times


class Device(ABC):
    def __init__(self, device_type: str, device_name: str):
        self.__device_type = device_type
        self.__device_name = device_name

    @property
    def device_name(self):
        return self.__device_name

    @device_name.getter
    def device_name(self):
        return self.__device_name

    @property
    def device_type(self):
        return self.__device_type

    @device_type.getter
    def device_type(self):
        return self.__device_type

    @abstractmethod
    def simulate_process(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class Sensor(Device, ABC):
    def __init__(self, sensor_type: str, sensor_name: str):
        super(Sensor, self).__init__(device_type="sensor", device_name=sensor_name)
        self.__value: float = 0.0
        self.__sensor_type: str = sensor_type

    @property
    def value(self):
        return self.__value

    @value.getter
    def value(self):
        self.simulate_process()
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def sensor_type(self):
        return self.__sensor_type

    @sensor_type.getter
    def sensor_type(self):
        return self.__sensor_type

    def get_data(self):
        # return {
        #     "device_type": self.device_type,
        #     "sensor_type": self.sensor_type,
        #     "name": self.device_name,
        #     "value": self.value
        # }
        return self.value

    def __str__(self):
        return str(self.get_data())


class TemperatureSensor(Sensor):
    def __init__(self, sensor_name: str):
        super().__init__(sensor_type="temperature_sensor",
                         sensor_name=sensor_name)

    def simulate_process(self):
        time_stamp = datetime.datetime.time(datetime.datetime.now())
        time_sec = 24 * time_stamp.hour + 60 * time_stamp.minute + time_stamp.second
        time_sec *= ACCELERATE
        self.value = 4 * math.cos(time_sec * math.pi / 10000) - 10


class PressureSensor(Sensor):
    def __init__(self, sensor_name: str):
        super().__init__(sensor_type="pressure_sensor",
                         sensor_name=sensor_name)

    def simulate_process(self):
        time_stamp = datetime.datetime.time(datetime.datetime.now())
        time_sec = 24 * time_stamp.hour + 60 * time_stamp.minute + time_stamp.second
        time_sec *= ACCELERATE
        self.value = math.sin(time_sec * math.pi / 10000) \
                     - 10 * math.cos(time_sec * math.pi / 10000) \
                     + 10 * math.cos(3 * time_sec * math.pi / 10000)


class LightSensor(Sensor):
    def __init__(self, sensor_name: str):
        super().__init__(sensor_type="light_sensor",
                         sensor_name=sensor_name)

    def simulate_process(self):
        time_stamp = datetime.datetime.time(datetime.datetime.now())
        time_sec = 24 * time_stamp.hour + 60 * time_stamp.minute + time_stamp.second
        time_sec *= ACCELERATE
        self.value = math.sin(time_sec * math.pi / 20000)


class AccelerometerSensor(Sensor):
    def __init__(self, sensor_name: str):
        super().__init__(sensor_type="accelerometer_sensor",
                         sensor_name=sensor_name)

    def simulate_process(self):
        self.value = random.random() if random.random() > 0.5 else 0


sensors_dict = {
    "temperature_sensor": TemperatureSensor,
    "pressure_sensor": PressureSensor,
    "light_sensor": LightSensor,
    "accelerometer_sensor": AccelerometerSensor
}
