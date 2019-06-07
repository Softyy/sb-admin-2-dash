import dash_core_components as dcc
import dash_html_components as html

from ..consts import SIDEBAR_ID,SIDEBAR_TOGGLE_ID

def render():
    return html.Ul(
        id=SIDEBAR_ID,
        className="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
        children=[
            dcc.Link(
                className="sidebar-brand d-flex align-items-center justify-content-center",
                href="/",
                children=[
                    html.Div(
                        className="sidebar-brand-icon rotate-n-15",
                        children=html.I(className="fas fa-laugh-wink")
                    ),
                    html.Div(
                        className="sidebar-brand-text mx-3",
                        children=[
                            "SB Admin ",
                            html.Sup(2)
                        ]
                    )]
            ),
            # Divider
            html.Hr(className="sidebar-divider my-0"),

            # Nav Item - Dashboard
            html.Li(

                dcc.Link([
                    html.I(className="fas fa-fw fa-tachometer-alt"),
                    html.Span("Dashboard")
                ],
                    className="nav-link",
                    href="/dashboard"),
                className="nav-item active"
            ),

            # Divider
            html.Hr(className="sidebar-divider"),

            # Heading
            html.Div(
                "Interface",
                className="sidebar-heading"
            ),

            # Nav Item - Pages Collapse Menu

            html.Li([
                html.A([
                    html.I(className="fas fa-fw fa-cog"),
                    html.Span("Components")],
                    className="nav-link collapsed",
                    href="#",
                    **{"data-toggle": "collapse", "data-target": "#collapseTwo", "aria-expanded": "true", "aria-controls": "collapseTwo"}
                ),
                html.Div(
                    id="collapseTwo",
                    className="collapse",
                    **{"aria-labelledby": "headingTwo", "data-parent": "#accordionSidebar"},
                    children=html.Div([
                        html.H6("Custom Components:",
                                className="collapse-header"),
                        dcc.Link("Buttons", className="collapse-item",
                                 href="/buttons"),
                        dcc.Link("Cards", className="collapse-item",
                                 href="/cards")
                    ],
                        className="bg-white py-2 collapse-inner rounded")
                )],
                className="nav-item"
            ),

            # Nav Item - Utilities Collapse Menu

            html.Li([
                html.A([
                    html.I(className="fas fa-fw fa-wrench"),
                    html.Span("Utilities")],
                    className="nav-link collapsed",
                    href="#",
                    **{"data-toggle": "collapse", "data-target": "#collapseUtilities", "aria-expanded": "true", "aria-controls": "collapseUtilities"}
                ),
                html.Div(
                    id="collapseUtilities",
                    className="collapse",
                    **{"aria-labelledby": "headingUtilities", "data-parent": "#accordionSidebar"},
                    children=html.Div([
                        html.H6("Custom Utilities:",
                                className="collapse-header"),
                        dcc.Link("Colors", className="collapse-item",
                                 href="/utilities-color"),
                        dcc.Link("Borders", className="collapse-item",
                                 href="/utilities-border"),
                        dcc.Link("Animations", className="collapse-item",
                                 href="/utilities-animation"),
                        dcc.Link("Other", className="collapse-item",
                                 href="/utilities-other")
                    ],
                        className="bg-white py-2 collapse-inner rounded")
                )],
                className="nav-item"
            ),

            # Divider
            html.Hr(className="sidebar-divider"),

            # Heading
            html.Div(
                "Addons",
                className="sidebar-heading"
            ),

            # Nav Item - Pages Collapse Menu
            html.Li([
                html.A([
                    html.I(className="fas fa-fw fa-folder"),
                    html.Span("Pages")],
                    className="nav-link collapsed",
                    href="#",
                    **{"data-toggle": "collapse", "data-target": "#collapsePages", "aria-expanded": "true", "aria-controls": "collapsePages"}
                ),
                html.Div(
                    id="collapsePages",
                    className="collapse",
                    **{"aria-labelledby": "headingPages", "data-parent": "#accordionSidebar"},
                    children=html.Div([
                        html.H6("Login Screens:",
                                className="collapse-header"),
                        dcc.Link("Login", className="collapse-item",
                                 href="/login"),
                        dcc.Link("Register", className="collapse-item",
                                 href="/register"),
                        dcc.Link("Forgot Password", className="collapse-item",
                                 href="/forgot-password"),
                        html.Div(className="collapse-divider"),
                        html.H6("Other Pages:",
                                className="collapse-header"),
                        dcc.Link("404 Page", className="collapse-item",
                                 href="/404"),
                        dcc.Link("Blank Page", className="collapse-item",
                                 href="/blank"),
                    ],
                        className="bg-white py-2 collapse-inner rounded")
                )],
                className="nav-item"
            ),

            # Nav Item - Charts

            html.Li(
                dcc.Link([
                    html.I(className="fas fa-fw fa-chart-area"),
                    html.Span("Charts")],
                    className="nav-link",
                    href="/charts"
                ), className="nav-item"),

            # Nav Item - Tables
            html.Li(
                dcc.Link([
                    html.I(className="fas fa-fw fa-table"),
                    html.Span("Tables")],
                    className="nav-link",
                    href="/tables"
                ), className="nav-item"),

            # Divider
            html.Hr(className="sidebar-divider"),

            # Sidebar Toggler (Sidebar)
            html.Div(
                html.Button(id=SIDEBAR_TOGGLE_ID,
                            className="rounded-circle border-0"),
                className="text-center d-none d-md-inline")
        ])
