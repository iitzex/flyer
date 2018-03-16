import json
import math
import os
import time
from datetime import datetime
from json import JSONDecodeError
from os import listdir

from plot import bokeh_draw

S1 = (25.061006, 121.223699, 'S1', '^=')
S10 = (25.083403, 121.251938, 'S10 ', '=$')
SCALE_MAX = 500
SCALE_MIN = 50


lookup = {}
traffic = []


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


def dist(p, scale, f, fn):
    cs = f['flight']
    lat = f['lat']
    lon = f['lon']

    d = pow(10000 * (p[0] - lat), 2) + pow(10000 * (p[1] - lon), 2)
    if d < scale:
        # print(cs, d, fn, p, symbol, sep=',')
        k = cs + p[3]
        if k not in lookup:
            lookup[k] = d
            traffic.append((cs, d, fn, p[2], p[3]))
        elif d < lookup[k]:
            lookup[k] = d
            del traffic[-1]
            traffic.append((cs, d, fn, p[2], p[3]))


def checkpoint(aircraft, fn):
    for f in aircraft:
        try:
            if f['flight'] != '' and f['lat'] != '' and f['lon'] != '':
                pass
        except KeyError:
            continue

        dist(S1, SCALE_MAX, f, fn)
        dist(S10, SCALE_MAX, f, fn)


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


def draw_single(fn):
    with open('db/' + fn, 'r') as f:
        try:
            j = json.load(f)
        except JSONDecodeError:
            pass

        draw(j['aircraft'], fn)


def tstr(t):
    tstr = datetime.fromtimestamp(int(t)).strftime('%H:%M:%S')
    return tstr


def merge():
    seq = []
    for i, f in enumerate(traffic):
        # print(f[0], f[3], f[2])
        print(f)

        try:
            n = traffic[i + 1]
            if f[0] == n[0]:
                seq.append((f[0], f[3], f[2], n[3], n[2],
                            int(n[2]) - int(f[2])))

        except IndexError:
            pass

    return seq


def to_csv():
    with open('traffic.csv', 'w') as f:
        for l in merge():
            l = "{},{},{}, {}, {}, {}".format(l[0], l[1], l[3], l[5], tstr(l[2]),
                                              tstr(l[4]))
            # print(l)
            f.writelines(l + '\n')


if __name__ == '__main__':
    runtime()
    to_csv()
    # draw_single('1520921153')
