**Version 1.1.1**

**Fixed**

* TODO

**Added**

* QGIS updated to 2.18.13
* GDAL/OGR updated to 2.2.2
* GRASS updated to 7.2.2
* Python updated to 2.7.14
* PgAdmin 4 updated to v2.0
* New offline Desktop documentation included in installer

**Quality Assurance**

* In-house testing suite, covering Mac OS X 10.9 and macOS 10.12 and 10.13 with latest updates

**Version 1.1.0**

**Fixed**

* SAGA "slope, aspect, curvature" returns wrong output
* Crash when zooming a reprojected PostGIS layer
* Degradation of rendering performances in MSSQL provider
* Encoding problems with Processing toolbox
* Python filter expression don't work on "value relation"
* DB Manager: previewing layers in Virtual layers section remove them from the Layers panel
* Intersection causes crash with specific inputs
* Crashes when switching to some UTM CRSs with certain data
* Errors while trying run IPython and Jupyter consoles in Windows.

**Added**

* QGIS updated to 2.18.10
* QgsSettings (a QGIS 3.0 feature) backported to 2.18 Boundless release
  branch
* New qgis_global_setting.ini customization file, with Boundless plugins and
  plugin repo enabled by default
* New init_scripts support for running customization scripts on QGIS launch
* pgAdmin3 replaced by pgAdmin4 (code-signed)
* New Master Password Helper (C++ core plugin)
* New OAuth2 authentication method plugin
* New Reporting Tool plugin and createreport command line script
* GDAL/OGR updated to 2.2.0
* Updated license files for included third-party software
* New 'Boundless Documentation' URL link in Start menu and shortcuts on
  user's desktop
* OpenGeo QGIS logo dropped in favor of the official QGIS 2.x logo

**Quality Assurance**

* In-house testing suite, covering Mac OS X 10.9 and macOS 10.12 with latest updates

**Version 1.0.1**

**Fixed**

* Fixed QGIS crash on macOS after 10.12.4 update (Qt's Phonon Python binding removed)
* Fixed referenced macOS system Python library paths
* Removed deprecated CFBundleSignature key/value from Qt Designer's Info.plist
* Fixed help menu linking for Qt Designer help in Qt Assistant

**Added**

* Included SciPy Python package: https://www.scipy.org/scipylib/index.html

**Quality Assurance**

* Additional in-house testing suite, covering numerous Desktop/macOS upgrade paths
