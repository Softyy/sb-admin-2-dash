import dash_core_components as dcc
import dash_html_components as html


def render(icon, color, size=None):
    return html.A(
            html.I(className=f'{"fas" if icon not in ["facebook-f"] else "fab"} fa-{icon}'),
            className=f'btn btn-{color} btn-circle {"btn-%s" % size if size else ""} mr-1',
            href="#"
          )
