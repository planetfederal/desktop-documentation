# Sample script for QGIS Init Script
# This script will add a demo WMS endpoint


from qgis.PyQt.QtCore import QSettings
from qgis.utils import home_plugin_path, loadPlugin, startPlugin, plugins
from qgis.core import QgsMessageLog
QgsMessageLog.logMessage("Init script: %s" % __file__, tag="Init script", level=QgsMessageLog.INFO)

WMS_URL="http://demo.boundlessgeo.com/geoserver/wms"
WMS_NAME="Boundlessgeo Geoserver Demo"

settings = QSettings()

if "Qgis/WMS/%s/authcfg" % WMS_NAME not in settings.allKeys():
    settings.setValue("Qgis/WMS/%s/authcfg" % WMS_NAME, "")
    settings.setValue("Qgis/WMS/%s/username" % WMS_NAME, "")
    settings.setValue("Qgis/WMS/%s/password" % WMS_NAME, "")
    settings.setValue("Qgis/connections-wms/%s/dpiMode" % WMS_NAME, 7)
    settings.setValue("Qgis/connections-wms/%s/ignoreAxisOrientation" % WMS_NAME, False)
    settings.setValue("Qgis/connections-wms/%s/ignoreGetFeatureInfoURI" % WMS_NAME, False)
    settings.setValue("Qgis/connections-wms/%s/ignoreGetMapURI" % WMS_NAME, False)
    settings.setValue("Qgis/connections-wms/%s/invertAxisOrientation" % WMS_NAME, False)
    settings.setValue("Qgis/connections-wms/%s/referer" % WMS_NAME, "")
    settings.setValue("Qgis/connections-wms/%s/smoothPixmapTransform" % WMS_NAME, "")
    settings.setValue("Qgis/connections-wms/%s/url" % WMS_NAME, WMS_URL)
    QgsMessageLog.logMessage("WMS %s has been successfully installed" % WMS_NAME, tag="Init script", level=QgsMessageLog.INFO)
else:
    QgsMessageLog.logMessage("WMS %s was already installed" % WMS_NAME,  tag="Init script", level=QgsMessageLog.INFO)

