import json
import onewire
import time
import ds18x20
import machine


pico_id = machine.unique_id()

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)


pin = config_data.get("pin")
interval = config_data.get("interval")

ds_pin = machine.Pin(pin)

ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(interval)

    
    for rom in roms:
        temp = ds_sensor.read_temp(rom)


        print("Pico ID:", pico_id)
        print("ROM-adresser:", roms)
        print("Aktuell ROM-adress:", rom)
        print("Temperatur (C)", temp)

        print(f"{pico_id.hex()} {rom.hex()} {temp:.2f}")






