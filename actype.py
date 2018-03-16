import subprocess

import requests
from bs4 import BeautifulSoup


def findbyCallsign(flight):
    addr = 'https://zh-tw.flightaware.com/live/flight/'
    r = requests.get(addr+flight)

    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    actype = soup.find('meta', {'name': 'aircrafttype'})['content']
    print(actype)

    return actype


def findbyHex(hex):
    r = subprocess.check_output(['grep', hex, 'aircraftDatabase.csv'])
    t = r.decode("utf-8").split(',')[5]

    return t

if __name__ == '__main__':
    # callsign = 'EVA396'
    # findbyCallsign(callsign)

    hex = '89906d'
    t = findbyHex(hex)
    print(t)
