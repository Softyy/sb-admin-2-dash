import dash_core_components as dcc
import dash_html_components as html


def render(icon, color, text,size=None):
    return html.A(
            className=f'btn btn-{color} btn-icon-split {"btn-%s" % size if size else ""}',
            href="#",
            children=[
              html.Span(
                html.I(className=f'fas fa-{icon}'),
                className=f'icon {"text-white-50" if color != "light" else "text-gray-600"}'
              ),
            html.Span(text,className="text")
            ]
          )
