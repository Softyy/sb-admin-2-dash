import warnings

import dash_core_components as dcc
import dash_html_components as html

COLOR_ORDER = [
    'danger',
    'warning',
    'primary',
    'info',
    'success'
]


def render(project_name, percentage_done):
    if (percentage_done > 100):
        warnings.warn(
            "Project bar was passed a percentage larger than 100", UserWarning)
        percentage_done = 100

    color = COLOR_ORDER[percentage_done//20 - 1]

    return html.Div([
        html.H4(
            className="small font-weight-bold",
            children=[
                project_name,
                html.Span(
                    str(percentage_done) +
                    "%" if percentage_done < 100 else "Completed!",
                    className="float-right")
            ]
        ),
        html.Div(
            className="progress mb-4",
            children=html.Div(
                className=f'progress-bar bg-{color}',
                role="progressbar",
                style={"width": f'{percentage_done}%'},
                **{"aria-valuenow": str(percentage_done), "aria-valuemin": "0", "aria-valuemax": "100"}
            )
        )
    ])
