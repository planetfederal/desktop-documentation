# Sample script for QGIS Init Script
# This script will install the HelloWorld plugin into user space (if not yet installed)
# The plugin will also be enabled.

import os
import zipfile

from qgis.PyQt.QtCore import QSettings
from qgis.utils import home_plugin_path, loadPlugin, startPlugin, plugins
from qgis.core import QgsMessageLog
QgsMessageLog.logMessage("Init script: %s" % __file__, tag="Init script", level=QgsMessageLog.INFO)

if "HelloWorld" not in plugins:
    # Installing
    zip_ref = zipfile.ZipFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data', 'helloworld.zip'), 'r')
    zip_ref.extractall(home_plugin_path)
    zip_ref.close()
    loadPlugin('HelloWorld')
    startPlugin('HelloWorld')
    QgsMessageLog.logMessage("Plugin HelloWorld has been successfully installed", tag="Init script", level=QgsMessageLog.INFO)
else:
    QgsMessageLog.logMessage("Plugin HelloWorld has been already installed", tag="Init script", level=QgsMessageLog.INFO)

