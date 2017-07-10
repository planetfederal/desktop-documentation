# Sample script for QGIS Init Script
# This script will check for a setting value to determine
# if it needs to be run.
# When run, it will set the setting value and log a line.


from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsMessageLog
QgsMessageLog.logMessage("Init script: %s" % __file__, tag="Init script", level=QgsMessageLog.INFO)

if not QSettings().value("InitScript/RunOnceHasRun"):
    QgsMessageLog.logMessage("Setting 'InitScript/RunOnceHasRun' to 'true'", tag="Init script", level=QgsMessageLog.INFO)
    QSettings().setValue("InitScript/MyTestSetting", True)
else:
    QgsMessageLog.logMessage("'InitScript/MyTestSetting' already set to '%s'" % QSettings().value("InitScript/MyTestSetting"), tag="Init script", level=QgsMessageLog.INFO)

