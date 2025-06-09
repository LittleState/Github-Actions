import RPi.GPIO as GPIO
import time
import os

# 设置GPIO模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)  # 假设风扇连接到GPIO14

# 设置PWM
fan = GPIO.PWM(14, 25)  # GPIO18, 频率为25Hz
fan.start(0)  # 初始占空比（风扇停止）

def get_cpu_temperature():
    """获取CPU温度"""
    res = os.popen('vcgencmd measure_temp').readline()
    temp_str = res.replace("temp=", "").replace("'C\n", "")
    return float(temp_str)

try:
    while True:
        temp = get_cpu_temperature()
        print(f"Current Temperature: {temp} 'C")

        # 根据温度调整风扇占空比
        if temp < 55:
            duty_cycle = 10  # 停止转动
        elif 55 <= temp < 65:
            duty_cycle = 20  # 中速
        elif 65 <= temp < 75:
            duty_cycle = 50  # 高速
        else:
            duty_cycle = 100  # 全速

        fan.ChangeDutyCycle(duty_cycle)
        print(f"Fan duty cycle set to: {duty_cycle}%")
        time.sleep(5)

except KeyboardInterrupt:
    pass

finally:
    fan.stop()
    GPIO.cleanup()
