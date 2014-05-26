#!/usr/bin/python

DOMAIN = "sagarmatha-bluetooth"
PATH = "/usr/share/sagarmatha/locale"

import os, gettext, sys
sys.path.append('/usr/lib/chitwanix/common')
import additionalfiles

os.environ['LANG'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)

prefix = """[Desktop Entry]
Icon=bluetooth
Exec=sagarmatha-settings bluetooth
Terminal=false
Type=Application
Categories=GTK;Settings;X-Sagarmatha-NetworkSettings;HardwareSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
StartupNotify=true
X-Sagarmatha-Settings-Panel=bluetooth
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/bluetooth/sagarmatha-bluetooth-properties.desktop.in.in", prefix, _("Bluetooth"), _("Configure Bluetooth settings"), "")

