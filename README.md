import Adafruit_DHT

# DHT22 센서에 연결된 GPIO 핀 번호
sensor_pin = 4
sensor_type = Adafruit_DHT.DHT22

# 온습도 측정 함수
def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

# 메인 코드
if __name__ == '__main__':
    temperature, humidity = read_temperature_humidity()
    if temperature is not None and humidity is not None:
        print(f'Temperature: {temperature:.2f}°C')
        print(f'Humidity: {humidity:.2f}%')
    else:
        print('Failed to retrieve data from the sensor.')  
