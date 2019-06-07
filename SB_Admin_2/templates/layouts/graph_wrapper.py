import dash_core_components as dcc
import dash_html_components as html


def render(title="Earnings Overview", xl_size=8, lg_size=7, dropdown_id="dropdownMenuLink", graph=dcc.Graph()):
    return html.Div(
        className=f'col-xl-{xl_size} col-lg-{lg_size}',
        children=html.Div(
            className='card shadow mb-4',

            children=[
                # Card Header - Dropdown
                html.Div(
                  className="card-header py-3 d-flex flex-row align-items-center justify-content-between",
                    children=[
                        html.H6(
                            title, className="m-0 font-weight-bold text-primary"),
                        html.Div(
                            className="dropdown no-arrow",
                            children=[html.A(
                                className="dropdown-toggle",
                                href="#",
                                role="button",
                                id=dropdown_id,
                                **{"data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                                children=html.I(
                                    className="fas fa-ellipsis-v fa-sm fa-fw text-gray-400")
                            ),
                                html.Div(
                                className="dropdown-menu dropdown-menu-right shadow animated--fade-in",
                                **{"aria-labelledby": dropdown_id},
                                children=[
                                    html.Div("Dropdown Header:",
                                             className="dropdown-header"),
                                    html.A("Action", className="dropdown-item"),
                                    html.A("Another action",
                                           className="dropdown-item"),
                                    html.Div(className="dropdown-divider"),
                                    html.A("Something else here",
                                           className="dropdown-item")
                                ]
                            )

                            ],

                        )
                    ]
                ),
                # Card Body
                html.Div(
                    className="card-body",
                    children=graph
                )
            ]
        )
    )
