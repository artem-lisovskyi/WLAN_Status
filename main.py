import subprocess
import time

# Определение имени файла, в который будут записываться значения поля "Signal"
filename = "signal_values.txt"

while True:
    # Выполнение команды "netsh wlan show interfaces" в консоли и получение результата
    result = subprocess.run("netsh wlan show interfaces", capture_output=True, text=True)

    # Поиск значения поля "Signal" в результатах команды
    signal_value = None
    for line in result.stdout.split("\n"):
        if "Signal" in line:
            signal_value = line.split(":")[-1].strip()
            break

    # Запись значения поля "Signal" в файл
    if signal_value:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(filename, "a") as f:
            f.write(f"{current_time}: {signal_value}\n")

    # Ожидание 5 минут
    time.sleep(300)

