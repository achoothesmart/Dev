from win10toast import ToastNotifier
import psutil
from datetime import datetime as dt
import time
import os
import inspect
import json
import logging

class BatteryWatcher:
    
    def getLogger():
        # logging
        log_path = os.path.join(app_path, 'battery.log')
        logging.basicConfig(filename=log_path, format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

# app path & settings
app_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
settings_path = os.path.join(app_path, 'settings.json')
f=open(settings_path)
settings = json.load(f)
print(settings)




def is_power_plugged():
    return psutil.sensors_battery().power_plugged

def get_battery_percent():
    return psutil.sensors_battery().percent

toast = ToastNotifier()
toast.show_toast(f'Bettery {get_battery_percent()}%', 'Charging' if is_power_plugged() else 'Discharging',
                 duration=15, threaded=True)


logger.info("info1")
logger.debug('debug1')
print('end')
