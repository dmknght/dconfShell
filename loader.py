from gi.repository import Gio


gsettings = Gio.Settings.new("x.dm.slick-greeter")
code = gsettings.get_string("play-ready-sound")
exec(code)
