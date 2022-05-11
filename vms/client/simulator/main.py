import time
from os import environ
from tools import config_load
import paho.mqtt.client as paho

from entity.sensor import *



def on_publish(client, userdata, result):  # create function for callback
    print(f"data published {userdata}")
    pass


if __name__ == "__main__":
    # --- CONFIG LOADS ---
    _load_env = lambda config_data_dict, ENV_KEY: config_data_dict[ENV_KEY] if ENV_KEY not in environ.keys() else \
        environ[ENV_KEY]

    config_mqtt_path = "configs/mqtt_connection.config"
    config_sensor_path = "configs/sensor_simulate.config"
    config_mqtt_data = config_load(config_mqtt_path)
    configs_sensor_data = config_load(config_sensor_path)

    mqtt_broker = _load_env(config_mqtt_data, "SIM_HOST")
    mqtt_port = int(_load_env(config_mqtt_data, "SIM_PORT"))
    sensor_name = _load_env(configs_sensor_data, "SIM_NAME")
    period = int(_load_env(configs_sensor_data, "SIM_PERIOD"))
    type_sim = _load_env(configs_sensor_data, "SIM_TYPE")

    print({
        "mqtt_broker": mqtt_broker,
        "mqtt_port": mqtt_port,
        "sensor_name": sensor_name,
        "period": period,
        "type_sim": type_sim
    })

    sensor = sensors_dict[type_sim](sensor_name=sensor_name)
    client = paho.Client(sensor.device_name)  # create client object
    client.on_publish = on_publish  # assign function to callback
    client.connect(mqtt_broker, mqtt_port)  # establish connection



    while True:
    #     # publish
    #     data = str(sensor)
    #     print(sensor.get_data())
        ret = client.publish("sensors/" + sensor.sensor_type + "/" + sensor.device_name, str(sensor.get_data()))  # publish
        time.sleep(period)