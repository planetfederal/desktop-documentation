#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2017 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0+ license.
#
"""
Dump QGIS 2 or 3 Q[gs]Settings object to .ini file.
Useful for Windows and macOS versions that do not store settings in INI format.
Resultant file can be used to help populate a qgis_global_settings.ini file.
Author: Larry Shaffer
Email: lshaffer (at) boundlessgeo (dot) com

"""

import os
import datetime

# Are we running inside of QGIS's Python console editor?
try:
    iface
    if not isinstance(iface, qgis._gui.QgisInterface):
        raise NameError
except NameError:
    print("Run script from within Python Console's editor inside a running QGIS instance")
    raise

try:
    from qgis.core import Qgis as QGis
    QGIS_APP_NAME = 'QGIS3'
except ImportError:
    from qgis.core import QGis
    QGIS_APP_NAME = 'QGIS2'

try:
    from qgis.PyQt.QtCore import QStandardPaths
    QT5 = True
except ImportError:
    from qgis.PyQt.QtGui import QDesktopServices
    QT5 = False

try:
    # Are we in QGIS >= 2.99 or Boundless Desktop's 2.18.10+?
    from qgis.core import QgsSettings
    HAS_QGSSETTINGS = True
except ImportError:
    HAS_QGSSETTINGS = False

from qgis.PyQt.QtCore import QSettings, QDir


def main():
    datestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if QT5:
        ini_out_dir = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
    else:
        ini_out_dir = QDesktopServices.storageLocation(QDesktopServices.DesktopLocation)
    ini_name = 'org.qgis.{0}-settings_{1}.ini'.format(QGIS_APP_NAME, datestamp)
    ini_out = QDir(ini_out_dir).absoluteFilePath(ini_name)

    if not os.path.exists(ini_out_dir):
        print('INI output directory does not exist: {0}'.format(ini_out_dir))
        return

    if not os.access(ini_out_dir, os.W_OK | os.X_OK):
        print('INI output directory is not writeable: {0}'.format(ini_out_dir))
        return

    # QGIS settings
    if HAS_QGSSETTINGS:
        qgis_settings = QgsSettings()
    else:
        qgis_settings = QSettings()

    # Output INI settings
    ini_settings = QSettings(ini_out, QSettings.IniFormat)

    qgis_keys = qgis_settings.allKeys()
    for k in qgis_keys:
        ini_settings.setValue(k, qgis_settings.value(k))

    ini_settings.sync()

    print("Settings output to: {0}".format(QDir.toNativeSeparators(ini_out)))


main()
