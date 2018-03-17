import csv
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


d = {}
with open('aircraft_db.csv') as f:
    reader = csv.reader(f)
    d = dict((rows[0], rows[2]) for rows in reader)


def findbyHex(hex):
    return (d[hex]).upper()


if __name__ == '__main__':
    hex = '89906d'
    t = findbyHex(hex)
    print(t)
