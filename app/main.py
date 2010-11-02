"""Database Toolkit UI

This module contains the UI elements of the database toolkit platform. 

This module should not be run directly; instead, individual scripts, when run,
should run the launch_wizard function.

"""

from dbtk.app.app import App


def launch_app(lists):
    """Launches the application GUI."""
    print "Launching Database Toolkit..."                    
    
    app = App(lists)
    app.MainLoop()
