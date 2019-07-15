import os
import dash

from .templates.index import render

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T',
        'crossorigin': 'anonymous'
    },
    {
        'href': 'https://use.fontawesome.com/releases/v5.8.2/css/all.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay',
        'crossorigin': 'anonymous'
    },
    {
        'href': 'https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i',
        'rel': 'stylesheet',
    }
]

external_scripts = [
    {
        "src": "https://code.jquery.com/jquery-3.3.1.slim.min.js",
        "integrity": "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo",
        "crossorigin": "anonymous"
    },
    {
        "src": "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js",
        "integrity": "sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1",
        "crossorigin": "anonymous"
    },
    {
        "src": "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js",
        "integrity": "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM",
        "crossorigin": "anonymous"
    }
]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

app.title = "SB Admin 2 Dash"

# Sets the html template fo the dash application
file_path = os.path.dirname(os.path.realpath(__file__))
index_path = os.path.join(file_path, 'templates', 'index.html')
with open(index_path) as index_fs:
    app.index_string = index_fs.read()

app.config['suppress_callback_exceptions'] = True

app.layout = render

from SB_Admin_2.router import *

from SB_Admin_2.toggle_sidebar import *
