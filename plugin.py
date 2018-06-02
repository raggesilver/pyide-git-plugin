
import git, os

from gi.repository import GObject, GLib, Gtk

class Plugin(GObject.GObject):

    def __init__(self, *args, **kwargs):

        GObject.GObject.__init__(self)

        if 'applicationWindow' in kwargs:
            self.applicationWindow = kwargs['applicationWindow']

    def do_activate(self):

        self.applicationWindow.headerBar.pack_end(Gtk.Button('Git'))
        self.applicationWindow.headerBar.show_all()

    def say_ok(self, *args):
        print("I'm ok")