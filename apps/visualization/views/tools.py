from bokeh.embed import components
from bokeh.plotting import figure


def plot_bar_chart(cols, counts):

    p = figure(plot_height=350, title="Mental Health Importance",
               toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    script, div = components(p)
    return script, div
