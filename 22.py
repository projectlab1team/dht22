import Adafruit_DHT

# DHT22 ������ ����� GPIO �� ��ȣ
sensor_pin = 4
sensor_type = Adafruit_DHT.DHT22

# �½��� ���� �Լ�
def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

# ���� �ڵ�
if __name__ == '__main__':
    temperature, humidity = read_temperature_humidity()
    if temperature is not None and humidity is not None:
        print(f'Temperature: {temperature:.2f}��C')
        print(f'Humidity: {humidity:.2f}%')
    else:
        print('Failed to retrieve data from the sensor.')