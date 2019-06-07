import dash_core_components as dcc
import dash_html_components as html

from .layouts.alert_item import render as alert_item
from .layouts.message_item import render as message_item
from .layouts.profile_menu_item import render as profile_menu_item


def render():
    return html.Nav(
        className="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow",
        children=[
            html.Button(
                id="sidebarToggleTop",
                className="btn btn-link d-md-none rounded-circle mr-3",
                children=html.I(className="fa fa-bars")
            ),
            html.Form(
                className="d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search",
                children=html.Div(
                    className="input-group",
                    children=[
                        dcc.Input(
                            type="text",
                            className="form-control bg-light border-0 small",
                            placeholder="Search for...",
                            # **{"aria-label":"Search","aria-describedby":"basic-addon2"}
                        ),
                        html.Div(
                            className="input-group-append",
                            children=html.Button(
                                type="button",
                                className="btn btn-primary",
                                children=html.I(className="fas fa-search fa-sm")
                            )
                        )
                    ]
                )
            ),
            # Topbar Navbar
            html.Ul(
                className="navbar-nav ml-auto",
                children=[
                    # Nav Item - Search Dropdown (Visible Only XS)
                    html.Li(
                        className="nav-item dropdown no-arrow d-sm-none",
                        children=[
                            html.A(
                                className="nav-link dropdown-toggle",
                                href="#",
                                id="searchDropdown",
                                role="button",
                                **{"data-toggle":"dropdown", "aria-haspopup":"true","aria-expanded":"false"},
                                children=html.I(className="fas fa-search fa-fw")
                            ),
                            # Dropdown - Messages
                            html.Div(
                                className="dropdown-menu dropdown-menu-right p-3 shadow animated--grow-in",
                                **{"aria-labelledby":"searchDropdown"},
                                children=html.Form(
                                    className="form-inline mr-auto w-100 navbar-search",
                                    children=html.Div(
                                        className="input-group",
                                        children=[
                                            dcc.Input(
                                                type="text",
                                                className="form-control bg-light border-0 small",
                                                placeholder="Search for..."
                                            ),
                                            html.Div(
                                                className="input-group-append",
                                                children=html.Button(
                                                    type="button",
                                                    className="btn btn-primary",
                                                    children=html.I(className="fas fa-search fa-sm")
                                                )
                                            )
                                        ]
                                    )
                                )
                            )
                        ]
                    ),
                    # Nav Item - Alerts
                    html.Li(
                        className="nav-item dropdown no-arrow mx-1",
                        children=[
                            html.A(
                                className="nav-link dropdown-toggle",
                                href="#",
                                id="alertsDropdown",
                                role="button",
                                **{"data-toggle":"dropdown", "aria-haspopup":"true", "aria-expanded":"false"},
                                children=[
                                    html.I(className="fas fa-bell fa-fw"),
                                    #Counter - Alerts
                                    html.Span("3+",className="badge badge-danger badge-counter")
                                ]
                            ),
                            # Dropdown Alerts
                            html.Div(
                                className="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in",
                                **{"aria-labelledby":"alertsDropdown"},
                                children=[
                                    html.H6("Alerts Center",className="dropdown-header"),
                                    alert_item("file-alt",'primary',"December 12, 2019","A new monthly report is ready to download!"),
                                    alert_item("donate",'success',"December 7, 2019","$290.29 has been deposited into your account!"),
                                    alert_item("exclamation-triangle",'warning',"December 2, 2019","Spending Alert: We've noticed unusually high spending for your account."),
                                    html.A(
                                        className="dropdown-item text-center small text-gray-500",
                                        href="#",
                                        children="Show All Alerts"
                                    )
                                ]
                            )
                        ]
                    ),
                    # Nav Item - Messages
                    html.Li(
                        className="nav-item dropdown no-arrow mx-1",
                        children=[
                            html.A(
                                className="nav-link dropdown-toggle",
                                href="#",
                                id="messagesDropdown",
                                role="button",
                                **{"data-toggle":"dropdown", "aria-haspopup":"true", "aria-expanded":"false"},
                                children=[
                                    html.I(className="fas fa-envelope fa-fw"),
                                    #Counter - Messages
                                    html.Span("7",className="badge badge-danger badge-counter")
                                ]
                            ),
                            # Dropdown - Messages
                            html.Div(
                                className="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in",
                                **{"aria-labelledby":"messagesDropdown"},
                                children=[
                                    html.H6("Message Center",className="dropdown-header"),
                                    message_item("success","https://source.unsplash.com/fn_BT9fwg_E/60x60","Hi there! I am wondering if you can help me with a problem I've been having.","Emily Fowler","58m"),
                                    message_item("success","https://source.unsplash.com/AU4VPcFN4LE/60x60","I have the photos that you ordered last month, how would you like them sent to you?","Jae Chun","1d"),
                                    message_item("warning","https://source.unsplash.com/CS2uCrpNzJY/60x60","Last month's report looks great, I am very happy with the progress so far, keep up the good work!","Morgan Alvarez","2d"),
                                    message_item("success","https://source.unsplash.com/Mv9hjnEUHR4/60x60","Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren't good...","Chicken the Dog","2w"),
                                    html.A(
                                        className="dropdown-item text-center small text-gray-500",
                                        href="#",
                                        children="Read More Messages"
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div(className="topbar-divider d-none d-sm-block"),
                    # Nav Item - User Information
                    html.Li(
                        className="nav-item dropdown no-arrow",
                        children=[
                            html.A(
                                className="nav-link dropdown-toggle",
                                href="#",
                                id="userDropdown",
                                role="button",
                                **{"data-toggle":"dropdown", "aria-haspopup":"true","aria-expanded":"false"},
                                children=[
                                    html.Span("Valerie Luna",className="mr-2 d-none d-lg-inline text-gray-600 small"),
                                    html.Img(className="img-profile rounded-circle",src="https://source.unsplash.com/QAB-WJcbgJk/60x60")
                                ]
                            ),
                            # Dropdown - User Information
                            html.Div(
                                className="dropdown-menu dropdown-menu-right shadow animated--grow-in",
                                **{"aria-labelledby":"userDropdown"},
                                children=[
                                    profile_menu_item("user","Profile"),
                                    profile_menu_item("cogs","Settings"),
                                    profile_menu_item("list","Activity Log"),
                                    html.Div(className="dropdown-divider"),
                                    profile_menu_item("sign-out-alt","Logout"),
                                ]
                            )
                        ]
                    )
                ]
            )
        ])
