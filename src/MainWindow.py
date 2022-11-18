import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title("Peak notes")
        self.set_default_size(600, 400)

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

        self.button = Gtk.Button(label="Save")
        self.button.connect("clicked", self.save_button)
        self.header.pack_start(self.button)

        self.save_dialog = Gtk.FileChooserNative.new(title = "Open Text File",
        parent = self, action=Gtk.FileChooserAction.SAVE)
        self.save_dialog.connect("response", self.save_response)

        self.big_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.big_box.set_margin_top(10)
        self.big_box.set_margin_bottom(10)
        self.big_box.set_margin_start(10)
        self.set_child(self.big_box)

        self.textScroll = Gtk.ScrolledWindow()
        self.textScroll.set_hexpand(True)
        self.textScroll.set_vexpand(True)
        self.big_box.append(self.textScroll)

        self.tView = Gtk.TextView()
        self.tView.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textScroll.set_child(self.tView)

    def save_button(self, button):
        self.save_dialog.show()

    def save_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            self.file = dialog.get_file()
            self.filename = self.file.get_path()
            self.startIter, self.endIter = self.tView.get_buffer().get_bounds()
            print("text = " + self.tView.get_buffer().get_text(self.startIter,self.endIter,False))
            print(self.filename)

            self.savefile = open(self.file.get_path(), 'a')
            self.savefile.write(self.tView.get_buffer().get_text(self.startIter,self.endIter,False))
            self.savefile.close()