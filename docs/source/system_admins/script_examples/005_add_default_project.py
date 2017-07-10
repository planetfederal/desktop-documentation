# Sample script for QGIS Init Script
# This script will add default project

import os
from shutil import copyfile
from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsMessageLog, QgsApplication
QgsMessageLog.logMessage("Init script: %s" % __file__, tag="Init script", level=QgsMessageLog.INFO)


settings = QSettings()
DEFAULT_PROJECT_PATH=os.path.join(QgsApplication.qgisSettingsDirPath(), "project_default.qgs")

if not os.path.exists(DEFAULT_PROJECT_PATH):
    try:
        copyfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data', 'project_default.qgs'), DEFAULT_PROJECT_PATH)
        QgsMessageLog.logMessage("Default project has been successfully installed", tag="Init script", level=QgsMessageLog.INFO)
        # Set the settings to use the default project
        settings.setValue("qgis/newProjectDefault", True)
    except Exception as ex:
        QgsMessageLog.logMessage("Error installing default project: %s" % ex, tag="Init script", level=QgsMessageLog.CRITICAL)
else:
    QgsMessageLog.logMessage("Default project was already installed",  tag="Init script", level=QgsMessageLog.INFO)

