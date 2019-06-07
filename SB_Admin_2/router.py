
from dash.dependencies import Input, Output

from . import app

from .templates.layouts.content_wrapper import render as content_wrapper
from .templates.layouts.entry_wrapper import render as entry_wrapper

from .templates.sidebar import render as sidebar

from .templates.dashboard import render as dashboard

from .templates.cards import render as cards
from .templates.buttons import render as buttons

from .templates.color_utilities import render as color_utilities
from .templates.border_utilities import render as border_utilities
from .templates.animation_utilities import render as animation_utilities
from .templates.other_utilities import render as other_utilities

from .templates.login import render as login
from .templates.register import render as register
from .templates.forgot_password import render as forgot_password

from .templates.blank import render as blank

from .templates.charts import render as charts
from .templates.tables import render as tables

from .templates._404 import render as _404


urls = [
    ('/', dashboard),
    ('/dashboard', dashboard),
    ('/buttons', buttons),
    ('/cards', cards),
    ('/utilities-color', color_utilities),
    ('/utilities-border', border_utilities),
    ('/utilities-animation', animation_utilities),
    ('/utilities-other', other_utilities),
    ('/charts', charts),
    ('/tables', tables),
    ('/blank', blank),
    ('/404', _404)
]

page_urls = [
    ('/login', login),
    ('/register', register),
    ('/forgot-password', forgot_password),
]

routes = {route: layout for route, layout in urls}
pages = {route: layout for route, layout in page_urls}

SIDEBAR = sidebar()


@app.callback(Output('wrapper', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    # this check should be replaced with a user authenticated check
    # otherwise the first 404 makes no sense.
    if pathname in routes:
        page_content = routes.get(pathname, _404)()
        return [SIDEBAR, content_wrapper(page_content)]
    elif pathname in pages:
        page_content = pages.get(pathname, _404)()
        return page_content
    else:
        return entry_wrapper(_404())
