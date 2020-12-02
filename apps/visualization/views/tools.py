import numpy as np
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.plotting import figure


def plot_bar_chart(cols, counts, title):
    p = figure(plot_height=350, title=title, toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9, line_color='white')

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


def plot_hexbin(x, y, title):
    p = figure(title=title, match_aspect=True, plot_height=370,
               tools="wheel_zoom,reset", background_fill_color='white')
    p.grid.visible = False

    r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

    p.circle(x, y, color="red", size=5)

    p.add_tools(HoverTool(
        tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
        mode="mouse", point_policy="follow_mouse", renderers=[r]
    ))
    script, div = components(p)
    return script, div


def plot_hist(df, title):
    p = df.plot_bokeh(
        kind="hist",
        bins=np.arange(-20, 120, 10),
        vertical_xlabel=False,
        xlabel="Age",
        normed=1000,
        hovertool=False,
        title=title,
        show_figure=False)
    p.axis.major_label_text_font_size = '12pt'
    p.xaxis.axis_label_text_font_size = "12pt"
    script, div = components(p)
    return script, div


def plot_stacked_bar(cols, classes, data, title):
    colors = ["maroon", "salmon"]

    p = figure(x_range=cols, plot_height=350, title=title,
               toolbar_location=None, tools="")

    p.vbar_stack(classes, x='labels', width=0.9, color=colors, source=data,
                 legend_label=classes)

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
    script, div = components(p)
    return script, div


def plot_line(x, y):
    p = figure(plot_width=600, plot_height=350)
    p.line(x, y, line_width=2)
    script, div = components(p)
    return script, div
