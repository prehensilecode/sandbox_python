#!/usr/bin/env python3
# https://stackoverflow.com/a/34918369/299952

from bokeh.palettes import HighContrast3
from bokeh.plotting import figure, show
from bokeh.io import export_png, export_svg

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

p = figure(x_range=fruits, height=250, title="Fruit Counts by Year",
           toolbar_location=None, tools="hover", tooltips="$name @fruits: @$name")

p.vbar_stack(years, x='fruits', width=0.9, color=HighContrast3, source=data,
             legend_label=years)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = "black"
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
export_png(p, filename='plot.png')

export_svg(p, filename='plot.svg')
