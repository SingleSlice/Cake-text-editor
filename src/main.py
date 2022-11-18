import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

import MainWindow

app = Adw.Application(application_id = "io.singleslice.github")

def on_activate(app):
    win = MainWindow.MainWindow(application = app)
    win.present()

app.connect('activate', on_activate)
app.run()