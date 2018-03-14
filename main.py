import json
import time
from os import listdir
from os.path import isfile, join

from plot import bokeh_draw

R05L = (25.073076, 121.216158)
N5 = ()
N7 = (25.084587, 121.232751)
N8 = ()
N9 = ()


def runtime():
    p = 'db'
    files = [f for f in listdir(p)]
    files.sort()

    for fn in files:
        with open('db/' + fn, 'r') as f:
            j = json.load(f)

            draw(j['aircraft'], fn)


def draw(aircraft, fn):
    lat = []
    lon = []
    callsign = []

    for f in aircraft:
        try:
            if f['flight'] != '' and f['lat'] != '' and f['lon'] != '':
                pass
        except KeyError:
            continue

        callsign.append(f['flight'])
        lat.append(f['lat'])
        lon.append(f['lon'])

    print(fn)
    print(lat)
    print(lon)
    print(callsign)

    bokeh_draw(lat, lon, callsign, fn)


def process(flight):
    # print(flight['aircraft'])
    print('time:', flight['now'])

    top_lats = []
    top_lons = []

    for f in flight['aircraft']:
        try:
            # if precheck(f):
            #     continue

            lat, lon = check(f)
            top_lats.append(lat)
            top_lons.append(lon)

        except KeyError:
            pass

    print(top_lats, top_lons)
    # draw(top_lats, top_lons)


if __name__ == '__main__':
    runtime()
