import plotly.graph_objs as go

from ..consts import COLOR


def create_line_trace(color='#4e73df'):
    x, y = get_line_data()
    return go.Scatter(
        x=x,
        y=y,
        fill='tozeroy',
        fillcolor=f'rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.05)',
        line=dict(
            color=(color),
            width=4,
            shape='spline',
            smoothing=1.3)
    )


def create_line_figure():
    return go.Figure(data=[create_line_trace()],
                     layout=go.Layout(
        yaxis=go.layout.YAxis(
            fixedrange=True,
            tickprefix="$"
        ),
        xaxis=go.layout.XAxis(
            fixedrange=True
        ),
        margin=go.layout.Margin(
            l=50,
            r=20,
            b=40,
            t=0,
            pad=4
        )
    ))


def get_line_data():
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
         'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y = [10000*((x+1)//2) - 5000*(x//2) for x in range(12)]
    return x, y


def create_bar_figure():
    values, labels = get_bar_data()
    return go.Figure(
        data=[
            go.Pie(
                values=values,
                labels=labels,
                hole=0.8,
                marker=go.pie.Marker(
                    colors=[
                        COLOR['success'],
                        COLOR['primary'],
                        COLOR['info']
                    ],
                    line=go.pie.marker.Line(
                        width=3,
                        color="#FFFFFF"
                    )
                ),
                textinfo='none',
                hoverinfo='label+value',
            )
        ],
        layout=go.Layout(
            legend=go.layout.Legend(
                yanchor="bottom",
                xanchor="center",
                orientation="h"
            ),
            margin=go.layout.Margin(
                l=40,
                r=20,
                b=40,
                t=0,
                pad=4
            )
        )
    )


def get_bar_data():
    values = [30, 55, 15]
    labels = ["Social", "Direct", "Referral"]
    return values, labels
