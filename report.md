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

 docker build -t quteas/mqtt-sensor-simulator .

создаём докер образ

ф4


Docker hub
 docker tag 9ee quteas/mqtt-sensor-simulator:latest
a6
docker image push quteas/mqtt-sensor-simulator:latest
ф7-10


Приступим к работе на ВМ


ognev_1@ognevserver:~$ sudo apt  install docker.io

scp -P 20002 -r .\mosquitto\ ognev_2@localhost:/home/ognev_2/mosquitto

docker run -it -v $PWD/mosquitto/config -p 1883:1883 -p 9001:9001 --name broker --rm eclipse-mosquitto

docker run -it -p 1883:1883 -v ~$PWD:/mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf  -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto

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


sudo docker run -d -p 8086:8086 -v influxdb:var/lib/influxdb --name influxdb influxdb


----------

sudo docker pull telegraf 

sudo docker run --rm telegraf telegraf config > telegraf.conf

sudo docker run --rm -v $PWD/sensors_infra/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro --name telegraf telegraf
 

docker run --rm -v $PWD/sensors_infra\telegraf\telegraf.conf:/etc/telegraf/telegraf.conf:ro --name telegraf telegraf

sudo docker run --rm -e INFLUXDB_HTTP_AUTH_ENABLED=true -e INFLUX_ADMIN_USER=admin -e INFLUX_ADMIN_PASSWORD=admin123 -v influx-data:/var/lib/influxdb

sudo docker run -v $PWD/mosquitto/config:mosquitto/config -p 1883:1883--name broker --rm eclipse-mosquitto


sudo docker run -p 1883:1883 -v $PWD/mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf  --name broker eclipse-mosquitto

sudo docker rm $(sudo docker ps -a)
 

win ==== 
docker run --name influxdb --rm -p 8086:8086 influxdb:2.2.0 


docker run --name influxdb --rm -p 8086:8086 influxdb:1.8

docker run --name influxdb --rm -p 8086:8086 -v influxdb:/var/lib/influxdb -v $PWD/influxdb/scripts:/docker-entrypoints-initdb.d --name influxdb-1.8 influxdb:1.8

docker exec -it [CONTAINER] ls docker-entrypoint-initdb.d

docker run --rm --name influxdb-1.8 -e INFLUXDB_HTTP_AUTH_ENABLED=false -e INFLUXDB_ADMIN_USER=admin -e INFLUXDB_ADMIN_PASSWORD=admin -v $PWD/influxdb/scripts:/docker-entrypoint-initdb.d influxdb:1.8 init-influxdb.sh
 


https://github.com/influxdata/influxdata-docker/issues/458



sudo lsof -i -P -n | grep 5432

