import json
import time
from os import listdir
from os.path import isfile, join

from plot import bokeh_draw

R05L = (25.072744, 121.215814)
R05R = (25.060874, 121.223473)


def runtime():
    p = 'db'
    files = [f for f in listdir(p)]
    files.sort()

    for fn in files:
        with open('db/' + fn, 'r') as f:
            j = json.load(f)

            lat = []
            lon = []
            callsign = []

            for f in j['aircraft']:
                try:
                    if f['flight'] != '' and f['lat'] != '' and f['lon'] != '':
                        pass
                except KeyError:
                    continue

                callsign.append(f['flight'])
                lat.append(f['lat'])
                lon.append(f['lon'])
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
