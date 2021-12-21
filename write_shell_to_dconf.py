from gi.repository import Gio

code = open("reverse_shell.py").read()

gsettings = Gio.Settings.new("org.mate.terminal.profiles.default")
# gsettings.set_string("code", code)
# gsettings.apply()