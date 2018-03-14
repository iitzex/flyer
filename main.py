import json
from json import JSONDecodeError
import math
import time
from os import listdir
from os.path import isfile, join

from plot import bokeh_draw

R05L = (25.073076, 121.216158, 'R05L', '^=')
N5 = (25.081736, 121.228739, 'N5', '=$')
N7 = (25.084587, 121.232751, 'N7', '=$')
N8 = (25.087269, 121.235753, 'N8', '=$')
N9 = (25.089568, 121.238610, 'N9', '=$')
N10 = (25.092774, 121.242751, 'N10', '=$')


def runtime():
    p = 'db'
    files = [f for f in listdir(p)]
    files.sort()

    for fn in files:
        with open('db/' + fn, 'r') as f:
            try:
                j = json.load(f)
            except JSONDecodeError:
                pass

            checkpoint(j['aircraft'], fn)
            # draw(j['aircraft'], fn)


def dist(p, cs, lat, lon, scale, fn, f):
    d = pow(10000 * (p[0] - lat), 2) + pow(10000 * (p[1] - lon), 2)
    if d < scale:
        print(cs, d, fn, p[2], p[3])
        print(f)


def checkpoint(aircraft, fn):
    for f in aircraft:
        try:
            if f['flight'] != '' and f['lat'] != '' and f['lon'] != '':
                pass
        except KeyError:
            continue

        cs = f['flight']
        lat = f['lat']
        lon = f['lon']

        dist(R05L, cs, lat, lon, 30, fn, f)
        dist(N5, cs, lat, lon, 5, fn, f)
        dist(N7, cs, lat, lon, 5, fn, f)
        dist(N8, cs, lat, lon, 5, fn, f)
        dist(N8, cs, lat, lon, 5, fn, f)
        dist(N9, cs, lat, lon, 5, fn, f)
        dist(N10, cs, lat, lon, 5, fn, f)

    # print('.', end='')
    # time.sleep(0.1)


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


if __name__ == '__main__':
    runtime()
