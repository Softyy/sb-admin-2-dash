import dash_core_components as dcc
import dash_html_components as html

from .layouts.a_i import render as a_i
from .layouts.a_i_span import render as a_i_span

def render():
    return html.Div(className="container-fluid", children=[

        # Page Heading
        html.H1("Buttons", className="h3 mb-4 text-gray-800"),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-lg-6",
                    children=[
                        #circle buttons
                        html.Div(
                            className="card shadow mb-4",
                            children=[
                                html.Div(
                                    html.H6("Circle Buttons",className="m-0 font-weight-bold text-primary"),
                                    className="card-header py-3"
                                ),
                                html.Div(
                                    className="card-body",
                                    children=[
                                        html.P("Use Font Awesome Icons (included with this theme package) along with the circle buttons as shown in the examples below!"),
                                        # Circle Buttons (Default)
                                        html.Div(
                                            html.Code(".btn-circle"),
                                            className="mb-2"
                                        ),
                                        a_i('facebook-f','primary'),
                                        a_i('check','success'),
                                        a_i('info-circle','info'),
                                        a_i('exclamation-triangle','warning'),
                                        a_i('trash','danger'),
                                        html.Div(
                                            html.Code(".btn-circle .btn-sm"),
                                            className="mt-4 mb-2"
                                        ),
                                        a_i('facebook-f','primary','sm'),
                                        a_i('check','success','sm'),
                                        a_i('info-circle','info','sm'),
                                        a_i('exclamation-triangle','warning','sm'),
                                        a_i('trash','danger','sm'),
                                         html.Div(
                                            html.Code(".btn-circle .btn-lg"),
                                            className="mt-4 mb-2"
                                        ),
                                        a_i('facebook-f','primary','lg'),
                                        a_i('check','success','lg'),
                                        a_i('info-circle','info','lg'),
                                        a_i('exclamation-triangle','warning','lg'),
                                        a_i('trash','danger','lg'),
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="card shadow mb-4",
                            children=[
                                html.Div(
                                    html.H6("Brand Buttons",className="m-0 font-weight-bold text-primary"),
                                    className="card-header py-3"
                                ),
                                html.Div(
                                    className="card-body",
                                    children=[
                                        html.P("Google and Facebook buttons are available featuring each company's respective brand color. They are used on the user login and registration pages."),
                                        html.P(["You can create more custom buttons by adding a new color variable in the ",html.Code("_variables.scss")," file and then using the Bootstrap button variant mixin to create a new style, as demonstrated in the ",html.Code("_buttons.scss")," file."]),
                                    html.A(
                                        [html.I(className="fab fa-google fa-fw"), ".btn-google"],
                                        className="btn btn-google btn-block",
                                        href="#"
                                    ),
                                    html.A(
                                        [html.I(className="fab fa-facebook fa-fw"), ".btn-facebook"],
                                        className="btn btn-facebook btn-block",
                                        href="#"
                                    )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="col-lg-6",
                    children=[
                        html.Div(
                            className="card shadow mb-4",
                            children=[
                                html.Div(
                                    html.H6("Split Buttons with Icon",className="m-0 font-weight-bold text-primary"),
                                    className="card-header py-3"
                                ),
                                html.Div(
                                    className="card-body",
                                    children=[
                                        html.P(["Works with any button colors, just use the ",html.Code(".btn-icon-split"), " class and the markup in the examples below. The examples below also use the ",html.Code(".text-white-50")," helper class on the icons for additional styling, but it is not required."]),
                                        a_i_span('flag','primary','Split Button Primary'),
                                        html.Div(className="my-2"),
                                        a_i_span('check','success','Split Button Success'),
                                        html.Div(className="my-2"),
                                        a_i_span('info-circle','info','Split Button Info'),
                                        html.Div(className="my-2"),
                                        a_i_span('exclamation-triangle','warning','Split Button Warning'),
                                        html.Div(className="my-2"),
                                        a_i_span('trash','danger','Split Button Danger'),
                                        html.Div(className="my-2"),
                                        a_i_span('arrow-right','secondary','Split Button Secondary'),
                                        html.Div(className="my-2"),
                                        a_i_span('arrow-right','light','Split Button Primary'),
                                        html.Div(className="mb-4"),
                                        html.P("Also works with small and large button classes!"),
                                        a_i_span('flag','primary','Split Button Small',"sm"),
                                        html.Div(className="my-2"),
                                        a_i_span('flag','primary','Split Button Large',"lg"),
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ])
