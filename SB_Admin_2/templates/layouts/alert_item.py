import dash_core_components as dcc
import dash_html_components as html


def render(icon, color, date="December 12, 2019", message="A new monthly report is ready to download!"):
    return html.A(
              className="dropdown-item d-flex align-items-center",
              href="#",
              children=[
                  html.Div(
                  className="mr-3",
                  children=html.Div(
                      className=f'icon-circle bg-{color}',
                      children=html.I(className=f'fas fa-{icon} text-white')
                  )
              ),
              html.Div([
                  html.Div(date,className="small text-gray-500"),
                  html.Span(message,className="font-weight-bold")
              ])
              ]
          )
