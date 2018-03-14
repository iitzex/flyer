import json
import time

import requests

def save():
    # addr = 'http://192.168.0.11:8080/data/aircraft.json'
    addr = 'http://127.0.0.1:8080/data/aircraft.json'
    r = requests.get(addr)
    c = r.json()
    t = str(int(c['now']))
    print(t)

    with open('db/' + t, 'w') as f:
        f.writelines(r.text)


if __name__ == '__main__':
    while(True):
        save()
        time.sleep(1)

