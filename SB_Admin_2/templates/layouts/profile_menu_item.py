import dash_core_components as dcc
import dash_html_components as html


def render(icon, name):
    return html.A(
            className=f'dropdown-item',
            href="#",
            children=[
              html.I(className=f'fas fa-{icon} fa-sm fa-fw mr-2 text-gray-400'),
              name
            ]
          )
