import dash_core_components as dcc
import dash_html_components as html


def render(title="Summary Card", display_value="100", icon="fa-dollar-sign", color="success", progress_bar=False):

    content = [html.Div(
        className=f'col {"" if progress_bar else "mr-2"}',
        children=[
            html.Div(
                title, className=f'text-xs font-weight-bold text-{color} text-uppercase mb-1'),
            html.Div(
                str(display_value) + "%" if progress_bar else display_value, className="h5 mb-0 font-weight-bold text-gray-800")
        ]
    )]

    if progress_bar:
        content.append(html.Div(
            className="col",
            children=html.Div(
                className="progress progress-sm mr-2",
                children=html.Div(
                    className="progress-bar bg-info",
                    role="progressbar",
                    style={"width": f'{int(display_value)}%'},
                    **{"aria-valuenow": display_value, "aria-valuemin": "0", "aria-valuemax": "100"}
                )
            )
        ),)

    content.append(
        html.Div(
            className="col-auto",
            children=html.I(
                className=f'fas {icon} fa-2x text-gray-300')
        ))

    return html.Div(
        className="col-xl-3 col-md-6 mb-4",
        children=html.Div(
            className=f'card border-left-{color} shadow h-100 py-2',
            children=html.Div(
                className="card-body",
                children=html.Div(
                    className="row no-gutters align-items-center",
                    children=content
                )
            )
        )
    )
