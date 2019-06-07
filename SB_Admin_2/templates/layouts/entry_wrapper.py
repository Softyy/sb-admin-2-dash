import dash_core_components as dcc
import dash_html_components as html


def render(content):
    return html.Div(className="container", children=[

        # Outer Row
        html.Div(
            className="row justify-content-center",
            children=html.Div(
                className="col-xl-10 col-lg-12 col-md-9",
                children=html.Div(
                    className="card o-hidden border-0 shadow-lg my-5",
                    children=html.Div(
                        className="card-body p-0",
                        # Nested Row within Card Body
                        children=content))
            )
        )
    ])
