import dash_core_components as dcc
import dash_html_components as html


def render(color, src="https://source.unsplash.com/fn_BT9fwg_E/60x60", message="Hi there! I am wondering if you can help me with a problem I've been having.",name="Emily Fowle",time_since_received="58m"):
    return html.A(
              className="dropdown-item d-flex align-items-center",
              href="#",
              children=[
                  html.Div(
                  className="dropdown-list-image mr-3",
                  children=[
                    html.Img(
                      className="rounded-circle",
                      src=src,
                      alt=""
                    ),
                    html.Div(className=f'status-indicator bg-{color}')
                  ]

              ),
              html.Div(
                className="font-weight-bold",
                children=[
                  html.Div(message,className="text-truncate"),
                  html.Span(f'{name} · {time_since_received}',className="small text-gray-500")
              ])
              ]
          )
