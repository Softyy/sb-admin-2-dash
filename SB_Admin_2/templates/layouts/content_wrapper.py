import dash_core_components as dcc
import dash_html_components as html

from ..topbar import render as topbar

TOPBAR = topbar()


def render(content):
    return html.Div(
        id="content-wrapper",
        className="d-flex flex-column",
        children=html.Div(
            [TOPBAR, content],
            id="content"
        )
    )
