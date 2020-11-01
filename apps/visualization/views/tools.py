from bokeh.embed import components
from bokeh.plotting import figure


def plot_bar_chart(cols, counts, title):

    p = figure(plot_height=350, title=title, toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    script, div = components(p)
    return script, div


def plot_count(cols, counts, title):
    p = figure(x_range=cols, plot_height=350, title=title,
               toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    script, div = components(p)
    return script, div
