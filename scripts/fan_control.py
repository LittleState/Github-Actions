import RPi.GPIO as GPIO
import subprocess
import time

FAN_PIN = 14
PWM_FREQ = 25
INTERVAL = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)

current_duty = 0


def get_temp():
    try:
        r = subprocess.run(
            ['vcgencmd', 'measure_temp'],
            capture_output=True, text=True, timeout=3,
        )
        return float(r.stdout.replace('temp=', '').replace("'C\n", ''))
    except Exception:
        return None


def target_duty(temp, current):
    """根据当前状态和温度计算目标占空比，带迟滞避免频繁切换"""
    if current == 0:
        if temp >= 46:
            return 40
    elif current == 40:
        if temp < 43:
            return 0
        elif temp >= 51:
            return 75
    elif current == 75:
        if temp < 48:
            return 40
        elif temp >= 56:
            return 100
    elif current == 100:
        if temp < 53:
            return 75
    return current


try:
    while True:
        temp = get_temp()
        if temp is None:
            time.sleep(INTERVAL)
            continue

        duty = target_duty(temp, current_duty)
        if duty != current_duty:
            current_duty = duty
            fan.ChangeDutyCycle(duty)
            print(f"{temp}°C -> fan {duty}%")

        time.sleep(INTERVAL)

except KeyboardInterrupt:
    pass
finally:
    fan.stop()
    GPIO.cleanup()
