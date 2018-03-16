import json

import numpy
import pandas as pd
from bokeh.io import export_png, output_file, show
from bokeh.models import (Circle, ColumnDataSource, GMapOptions, GMapPlot,
                          LabelSet, Range1d)


def bokeh_draw(lat, lon, callsign, t):
    m = GMapOptions(lat=25.084, lng=121.23, map_type="roadmap", zoom=14)
    plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=m)
    plot.title.text = t
    plot.api_key = "AIzaSyCa4x7OjPPqH9Jt9_EFHbISoUZo6cRIo7Q "

    source = ColumnDataSource(
        data=dict(
            lat=lat,
            lon=lon,
            callsign=callsign,
        ))

    circle = Circle(
        x='lon',
        y='lat',
        size=4,
        fill_color="red",
        fill_alpha=0.8,
        line_color=None)
    plot.add_glyph(source, circle)

    labels = LabelSet(
        x='lon',
        y='lat',
        text='callsign',
        text_font_size='8pt',
        level='glyph',
        x_offset=1,
        y_offset=1,
        source=source,
        render_mode='canvas')
    plot.add_layout(labels)

    export_png(plot, filename='screenshots/' + t + '.png')

