import time
from opensky_api import OpenSkyApi
from flightaware import findtype

def m2ft(altitude):
    if altitude:
        altitude = round(float(altitude) * 3.2808399, 1)
    return altitude

def precheck(ac):
    if ac.latitude is None or ac.latitude > 28 or ac.latitude < 18:
        return False
    if ac.longitude is None or ac.longitude > 129 or ac.longitude < 114:
        return False
    if ac.callsign.strip() == '':
        return False

    return True

def main():
    api = OpenSkyApi()
    s = api.get_states()

    flights = []
    for ac in s.states:
        status = None
        ac.geo_altitude = m2ft(ac.geo_altitude)

        if not precheck(ac):
            continue

        print(ac)
        # print(ac.callsign)
        # print(ac.callsign, findtype(ac.callsign.strip()))

if __name__ == '__main__':
    while True:
        main()
        print('-------------------')
        time.sleep(5)
        
    
