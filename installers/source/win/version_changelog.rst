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
* Added custom OpenSSL and QtNetwork builds, and OpenSSL configuration for
  CAPI backend engine, to support Keystore plugin
* New 'Boundless Desktop Documentation' URL link in Start menu and shortcuts on
  user's desktop
* New winhttp-head.exe sub.domain.tld utility for auto-loading missing CAs of
  endpoints in Win cert store (overcomes Qt4 flaw)
* OpenGeo QGIS logo dropped in favor of the official QGIS 2.x logo

**Quality Assurance**

* In-house testing suite, covering Windows 10 and Windows 7 with latest updates


**Version 1.0.1**

**Fixed**

* Fixed QGIS project file icons and assignment of Desktop QGIS for launching project files.
* Various installer fixes.

**Added**

* Ability to pin Desktop apps launched from .bat wrapper scripts (right-click on shortcuts and choose Pin to Start or Taskbar). Wrappers are launched with nircmd.exe executable.
* Included SciPy Python package: https://www.scipy.org/scipylib/index.html
* Included 'requests' and 'future' Python packages.
* Upgraded 'setuptools' Python package.

**Quality Assurance**

* Additional in-house testing suite, covering numerous Desktop/Win upgrade paths.
