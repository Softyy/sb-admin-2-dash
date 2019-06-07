from dash.dependencies import Input, Output, State

from . import app

from.consts import SIDEBAR_ID, SIDEBAR_TOGGLE_ID, SIDEBAR_TOP_TOGGLE_ID


@app.callback(
    Output(SIDEBAR_ID, 'className'),
    [Input(SIDEBAR_TOGGLE_ID, 'n_clicks'),
     Input(SIDEBAR_TOP_TOGGLE_ID, 'n_clicks')],
    [State(SIDEBAR_ID, 'className')]
)
def toggle_sidebar(s_click, t_click, className):
    if (s_click is not None or t_click is not None):
        if "toggled" not in className:
            className += " toggled"
        else:
            className = className.replace(" toggled", "")
    return className
