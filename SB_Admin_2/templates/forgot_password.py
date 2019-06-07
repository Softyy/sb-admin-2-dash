import dash_core_components as dcc
import dash_html_components as html


def render():
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
                        children=html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="col-lg-6 d-none d-lg-block bg-password-image"),
                                html.Div(
                                    className="col-lg-6",
                                    children=html.Div(
                                        className="p-5",
                                        children=[
                                            html.Div(

                                                className="text-center",
                                                children=[
                                                    html.H1("Forgot Your Password?",
                                                            className="h4 text-gray-900 mb-4"),
                                                    html.P(
                                                        "We get it, stuff happens. Just enter your email address below and we'll send you a link to reset your password!", className="mb-4")
                                                ]
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
                                                    dcc.Link(
                                                        "Reset Password", className="btn btn-primary btn-user btn-block", href="/login")
                                                ]
                                            ),

                                            html.Div(
                                                dcc.Link(
                                                    "Create an Account!", href="/register", className="small"),
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
                )
            )
        ),
    ])
