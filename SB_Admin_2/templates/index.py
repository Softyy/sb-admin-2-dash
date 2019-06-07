import dash_core_components as dcc
import dash_html_components as html

from .sidebar import render as sidebar


def render():
    return html.Div(
        id="page-top",
        style={"min-height": "100%"},
        children=[
            dcc.Location(id='url', refresh=False),
            html.Div(
                id="wrapper",
                children=[
                    # sidebar(),
                    # Content Wrapper
                    html.Div(
                        id="content-wrapper",
                        className="d-flex flex-column",
                        children=[
                            # Main Content
                            html.Div(
                                id="content"
                            )
                        ]
                    )
                ]
            )
        ]
    )
