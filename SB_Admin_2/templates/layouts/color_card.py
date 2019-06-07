import dash_core_components as dcc
import dash_html_components as html


def render(title, color, color_code):
    return html.Div(
        className="col-lg-6 mb-4",
        children=html.Div(
            className=f'card bg-{color} text-white shadow',
            children=html.Div([
                title,
                html.Div(color_code, className="text-white-50 small")
            ],
                className="card-body"

            )
        )
    )
