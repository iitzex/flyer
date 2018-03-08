import requests
from bs4 import BeautifulSoup

def findtype(flight):
    addr = 'https://zh-tw.flightaware.com/live/flight/'
    r = requests.get(addr+flight)

    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    actype = soup.find('meta', {'name': 'aircrafttype'})['content']
    print(actype)

    return actype

if __name__ == '__main__':
    callsign = 'EVA396'
    findtype(callsign)