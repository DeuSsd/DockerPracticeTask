sudo docker ps
sudo usermod -aG docker ognev_1
id
docker run hello-woeld
docker ps -a
docker rm b7e
docker images ls -a
docker -v 

```python
    class TemperatureSensor(Sensor):
    def __init__(self, sensor_name: str):
        super().__init__(sensor_type="temperature_sensor",
                         sensor_name=sensor_name)

    def simulate_process(self):
        time_stamp = datetime.datetime.time(datetime.datetime.now())
        time_sec = 24 * time_stamp.hour + 60 * time_stamp.minute + time_stamp.second
        self.value = 4 * math.cos(time_sec * math.pi / 10000) - 10
```

фт1

Проверяем данные


a2 

Запускаем MQTT docker для проверки работы скрипта генерации данных

а3
a5

docker build -t simulator .

создаём докер образ

ф4


Docker hub

a6
docker image push quteas/mqtt-sensor-simulator:latest
ф7-10


Приступим к работе на ВМ


ognev_1@ognevserver:~$ sudo apt  install docker.io

scp -P 20002 -r .\mosquitto\ ognev_2@localhost:/home/ognev_2/mosquitto

docker run -it -v $PWD/mosquitto/config -p 1883:1883 -p 9001:9001 --name broker --rm eclipse-mosquitto

docker run -it -p 1883:1883 -p 9001:9001 -v ~/tmp/config:/mosquitto/config -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto

sudo apt update -y && sudo apt install mosquitto mosquitto-clients -y


a11

тест

 mosquitto_pub -h 192.168.6.1 -t /hello -m “hello”
 mosquitto_sub -h 192.168.7.1 -t /hello


ф-12-13

слева логи, справа докер


машина 1

sudo apt  install docker-compose

а14







sudo docker pull quteas/mqtt-sensor-simulator


a15





docker-compose --env-file .\variables.env up -d --no-deps --build

docker-compose --env-file .\variables.env up

a16
17
18

 scp -P 20001 -r .\mqtt_sensor_simulate ognev_1@localhost:/home/ognev_1/mqtt_sensor_simulate


f19

sudo docker-compose --env-file .\variables.env up -d --no-deps --build

 21
 $ mosquitto_sub -h 192.168.7.1 -F '\e[92m%t \e[96m%p\e[0m' -q 2 -t '#'
22