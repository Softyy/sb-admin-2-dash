import dash_core_components as dcc
import dash_html_components as html


def render():
    return html.Div(className="container", children=[

        # Outer Row
        html.Div(
            className="card o-hidden border-0 shadow-lg my-5",
            children=html.Div(
                className="card-body p-0",
                # Nested Row within Card Body
                children=html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="col-lg-5 d-none d-lg-block bg-register-image"),
                        html.Div(
                            className="col-lg-7",
                            children=html.Div(
                                className="p-5",
                                children=[
                                    html.Div(
                                        html.H1("Create an Account!",
                                                className="h4 text-gray-900 mb-4"),
                                        className="text-center"
                                    ),
                                    html.Form(
                                        className="user",
                                        children=[
                                            html.Div(
                                                className="form-group row",
                                                children=[
                                                    html.Div(
                                                        className="col-sm-6 mb-3 mb-sm-0",
                                                        children=dcc.Input(
                                                            type="text", className="form-control form-control-user", id="exampleFirstName",  placeholder="First Name")
                                                    ),
                                                    html.Div(
                                                        className="col-sm-6",
                                                        children=dcc.Input(
                                                            type="text", className="form-control form-control-user", id="exampleLastName",  placeholder="Last Name")
                                                    ),

                                                ]
                                            ),
                                            html.Div(
                                                className="form-group",
                                                children=dcc.Input(
                                                    type="email", className="form-control form-control-user", id="exampleInputEmail", placeholder="Email Address")
                                            ),
                                            html.Div(
                                                className="form-group row",
                                                children=[
                                                    html.Div(
                                                        className="col-sm-6 mb-3 mb-sm-0",
                                                        children=dcc.Input(
                                                            type="password", className="form-control form-control-user", id="exampleInputPassword",  placeholder="Password")
                                                    ),
                                                    html.Div(
                                                        className="col-sm-6",
                                                        children=dcc.Input(
                                                            type="password", className="form-control form-control-user", id="exampleRepeatPassword",  placeholder="Repeat Password")
                                                    ),
                                                ]
                                            ),
                                            dcc.Link(
                                                "Register Account", href="/login", className="btn btn-primary btn-user btn-block"),
                                            html.Hr(),
                                            dcc.Link(
                                                className="btn btn-google btn-user btn-block",
                                                href="/",
                                                children=[
                                                    html.I(
                                                        className="fab fa-google fa-fw"),
                                                    "Register with Google"
                                                ]
                                            ),
                                            dcc.Link(
                                                className="btn btn-facebook btn-user btn-block",
                                                href="/",
                                                children=[
                                                    html.I(
                                                        className="fab fa-facebook-f fa-fw"),
                                                    "Register with Facebook"
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
                                            "Already have an account? Login!", href="/login", className="small"),
                                        className="text-center"
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )

        ),
    ])
