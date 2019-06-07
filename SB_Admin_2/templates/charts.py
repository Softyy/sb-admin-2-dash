import dash_core_components as dcc
import dash_html_components as html


def render():
    return html.Div(className="container-fluid", children=[

        # Page Heading
        html.Div(
            html.H1("Charts", className="h3 mb-0 text-gray-800"),
            className="d-sm-flex align-items-center justify-content-between mb-4"
        ),
    ])
