import html

import dash_core_components as dcc
import dash_html_components as htm


def render():
    return htm.Div(className="container-fluid", children=[
        htm.Div(
            className="text-center",
            children=[
                htm.Div(
                    className="error mx-auto",
                    **{"data-text": "404"},
                    children=404
                ),
                htm.P(
                    className="lead text-gray-800 mb-5",
                    children="Page Not Found"
                ),
                htm.P(
                    className="text-gray-500 mb-0",
                    children="It looks like you found a glitch in the matrix..."
                ),
                dcc.Link(
                    f'{html.unescape("&larr;")} Back to Dashboard', href="/")
            ]
        )
    ])
