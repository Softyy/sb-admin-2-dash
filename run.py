from SB_Admin_2 import app

from SB_Admin_2.router import *

from SB_Admin_2.toggle_sidebar import *

if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
