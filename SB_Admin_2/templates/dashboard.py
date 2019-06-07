import dash_core_components as dcc
import dash_html_components as html

from .layouts.info_card import render as info_card
from .layouts.graph_wrapper import render as graph_wrapper
from .layouts.project_bar import render as project_bar
from .layouts.color_card import render as color_card

from ..data_retrievers.dummy import create_bar_figure, create_line_figure
from ..consts import COLOR, DUMMY_PROJECTS


def render():
    return html.Div(className="container-fluid", children=[

        # Page Heading
        html.Div([
            html.H1("Dashboard", className="h3 mb-0 text-gray-800"),
            html.A([html.I(className="fas fa-download fa-sm text-white-50"), "Generate Report"],
                   className="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm", href="#")
        ],
            className="d-sm-flex align-items-center justify-content-between mb-4"
        ),

        # Content Row
        html.Div(className="row", children=[
            info_card("Earnings (Monthly)", "$40,000",
                      "fa-calendar", "primary"),

            info_card("Earnings (Annual)", "$215,000",
                      "fa-dollar-sign", "success"),

            info_card("Tasks", display_value=50, icon="fa-clipboard-list",
                      color="info", progress_bar=True),

            info_card("Pending Requests", display_value=18, icon="fa-comments",
                      color="warning"),

        ]),

        html.Div(className="row", children=[
            graph_wrapper("Earnings Overview", 8, 7, "lineGraphDropdownMenuLink",
                          dcc.Graph(figure=create_line_figure(),
                                    config={'displayModeBar': False})),
            graph_wrapper("Revenue Sources", 4, 5, 'pieChartDropdownMenuLink',
                          dcc.Graph(figure=create_bar_figure(),
                                    config={'displayModeBar': False}))

        ]),

        html.Div(className="row", children=[
            # Content Column
            html.Div(
                className="col-lg-6 mb-4",

                children=[
                    # Project Card Example
                    html.Div(
                        className="card shadow mb-4",
                        children=[
                            html.Div(
                                className="card-header py-3",
                                children=html.H6(
                                    "Projects", className="m-0 font-weight-bold text-primary")
                            ),
                            html.Div(
                                className="card-body",
                                children=[project_bar(p[0], p[1])
                                          for p in DUMMY_PROJECTS]
                            )
                        ]
                    ),

                    # Color System

                    html.Div(
                        className="row",
                        children=[color_card(color, color, COLOR[color])
                                  for color in COLOR]
                    )
                ]
            ),
            html.Div(
                className="col-lg-6 mb-4",
                children=[
                    # Illustrations
                    html.Div(
                        className="card shadow mb-4",
                        children=[
                          html.Div(
                              className="card-header py-3",
                              children=html.H6(
                                  "Illustrations", className="m-0 font-weight-bold text-primary")
                          ),
                            html.Div(
                              className="card-body",
                              children=[
                                  html.Div(
                                      className="text-center",
                                      children=html.Img(
                                        className="img-fluid px-3 px-sm-4 mt-3 mb-4",
                                        style={"width": "25rem"},
                                        src="/assets/img/undraw_posting_photo.svg"
                                      )
                                  ),
                                  html.P([
                                      "Add some quality, svg illustrations to your project courtesy of ",
                                      html.A(
                                          "unDraw", target="_blank", rel="nofollow", href="https://undraw.co/"),
                                      " a constantly updated collection of beautiful svg images that you can use completely free and without attribution!"]),
                                  html.A("Browse Illustrations on unDraw", target="_blank",
                                         rel="nofollow", href="https://undraw.co/")
                              ]
                          )
                        ]
                    ),

                    # Approach
                    html.Div(
                        className="card shadow mb-4",
                        children=[
                            html.Div(
                                className="card-header py-3",
                                children=html.H6(
                                  "Development Approach", className="m-0 font-weight-bold text-primary")
                            ),
                            html.Div(
                                className="card-body",
                                children=[
                                    html.P("SB Admin 2 makes extensive use of Bootstrap 4 utility classes in order to reduce CSS bloat and poor page performance. Custom CSS classes are used to create custom components and custom utility classes."),
                                    html.P(
                                        "Before working with this theme, you should become familiar with the Bootstrap framework, especially the utility classes.", className="mb-0")
                                ]
                            )
                        ]
                    )
                ]
            )
        ])
    ])
