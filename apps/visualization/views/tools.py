import math

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


def plot_count(cols, counts, title, fill_color):
    p = figure(x_range=cols, plot_height=350, title=title,
               toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9, fill_color=fill_color)
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
        bins=np.arange(0, 10),
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
    p.line(x, y, line_width=2, line_alpha=0.8)
    script, div = components(p)
    return script, div


def box_plot(yy, g):
    lists = ['Did not go to school', 'Primary school', 'Secondary school', 'Vocational training diloma']
    import pandas as pd
    df = pd.DataFrame(dict(score=yy, group=g))

    # find the quartiles and IQR for each category
    groups = df.groupby('group')
    q1 = groups.quantile(q=0.25)
    q2 = groups.quantile(q=0.5)
    q3 = groups.quantile(q=0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    lower = q1 - 1.5 * iqr

    # find the outliers for each category
    def outliers(group):
        cat = group.name
        return group[(group.score > upper.loc[cat]['score']) | (group.score < lower.loc[cat]['score'])]['score']

    out = groups.apply(outliers).dropna()

    # prepare outlier data for plotting, we need coordinates for every outlier.
    if not out.empty:
        outx = []
        outy = []
        for keys in out.index:
            outx.append(keys[0])
            outy.append(out.loc[keys[0]].loc[keys[1]])

    p = figure(tools="", background_fill_color="white", x_range=lists, toolbar_location=None,
               plot_height=540)

    # if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
    qmin = groups.quantile(q=0.00)
    qmax = groups.quantile(q=1.00)
    upper.score = [min([x, y]) for (x, y) in zip(list(qmax.loc[:, 'score']), upper.score)]
    lower.score = [max([x, y]) for (x, y) in zip(list(qmin.loc[:, 'score']), lower.score)]

    # stems
    p.segment(lists, upper.score, lists, q3.score, line_color="black")
    p.segment(lists, lower.score, lists, q1.score, line_color="black")

    # boxes
    p.vbar(lists, 0.7, q2.score, q3.score, fill_color="#E08E79", line_color="black")
    p.vbar(lists, 0.7, q1.score, q2.score, fill_color="#3B8686", line_color="black")

    # whiskers (almost-0 height rects simpler than segments)
    p.rect(lists, lower.score, 0.2, 0.01, line_color="black")
    p.rect(lists, upper.score, 0.2, 0.01, line_color="black")

    # outliers
    # if not out.empty:
    #     p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6)

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = "white"
    p.grid.grid_line_width = 2
    p.xaxis.major_label_text_font_size = "16px"
    p.xaxis.major_label_orientation = math.pi/2

    # or alternatively:
    p.xaxis.major_label_orientation = "vertical"
    script, div = components(p)
    return script, div
