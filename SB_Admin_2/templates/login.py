import dash_core_components as dcc
import dash_html_components as html

from .layouts.entry_wrapper import render as entry_wrapper


def render():
    return entry_wrapper(html.Div(
        className="row",
        children=[
            html.Div(
                className="col-lg-6 d-none d-lg-block bg-login-image"),
            html.Div(
                className="col-lg-6",
                children=html.Div(
                    className="p-5",
                    children=[
                        html.Div(
                            html.H1("Welcome Back!",
                                    className="h4 text-gray-900 mb-4"),
                            className="text-center"
                        ),
                        html.Form(
                            className="user",
                            children=[
                                html.Div(
                                    className="form-group",
                                    children=dcc.Input(type="email", className="form-control form-control-user", id="exampleInputEmail",  placeholder="Enter Email Address...",
                                                       # **{"aria-describedby": "emailHelp"}
                                                       )
                                ),
                                html.Div(
                                    className="form-group",
                                    children=dcc.Input(
                                        type="password", className="form-control form-control-user", id="exampleInputPassword", placeholder="Password")
                                ),
                                html.Div(
                                    className="form-group",
                                    children=html.Div(
                                        className="custom-control custom-checkbox small",
                                        children=dcc.Checklist(
                                            id="customCheck",
                                            options=[{'label': 'Remember Me',
                                                     'value': 'remember-me'}],
                                            values=[],
                                            #inputClassName="custom-control-input",
                                            #labelClassName="custom-control-label"
                                        )
                                    )
                                ),
                                dcc.Link(
                                    "Login", href="/", className="btn btn-primary btn-user btn-block"),
                                html.Hr(),
                                dcc.Link(
                                    className="btn btn-google btn-user btn-block",
                                    href="/",
                                    children=[
                                        html.I(
                                            className="fab fa-google fa-fw"),
                                        "Login with Google"
                                    ]
                                ),
                                dcc.Link(
                                    className="btn btn-facebook btn-user btn-block",
                                    href="/",
                                    children=[
                                        html.I(
                                            className="fab fa-facebook-f fa-fw"),
                                        "Login with Facebook"
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            dcc.Link(
                                "Forgot Password?", href="/forgot-password", className="small"),
                            className="text-center"
                        ),
                        html.Div(
                            dcc.Link(
                                "Create an Account!", href="/register", className="small"),
                            className="text-center"
                        ),
                    ]
                )
            )
        ]
    )
    )
