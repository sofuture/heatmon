import time
from w1thermsensor import W1ThermSensor, Sensor
from w1thermsensor.errors import SensorNotReadyError, NoSensorFoundError
from prometheus_client import start_http_server
from prometheus_client import Gauge

g = Gauge("heatmon_temperature_c", "sensor temperature", ["sensor"])
therms = {
    "031397941c75": "office_out",
    "030397942af7": "office_return",
    "030594970240": "upstairs_return",
    "030697940cde": "upstairs_out",
    "0305949769c1": "main_return",
    "031397945533": "main_out",
}

if __name__ == "__main__":
  start_http_server(8000)
  print("Prometheus metrics available on port 8000 /metrics")
  sensors = {}

  while True:
    print("checking temps")
    for id, sensor_id in therms.items():
        try:
            sensors[id] = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id=id)
        except NoSensorFoundError:
            print("unable to initialize sensor:{}:{}".format(id, sensor_id))
            continue

        sensor = sensors[id]
        try:
            temp = sensor.get_temperature()
            g.labels(sensor=sensor_id).set(temp)
            print("sensor:{}:{} temp:{}".format(id,sensor_id,temp))
        except SensorNotReadyError:
            print("failed to get temp for sensor:{}:{}".format(id, sensor_id))
    time.sleep(5)


