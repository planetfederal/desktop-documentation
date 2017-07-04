What's new in 1.1.0
===================

This version contains numerous component upgrades and bug fixes. Highlights
include:

* QGIS updated to 2.18.10 which includes lots of new features and
  improvements (see `QGIS 2.18 visual changelog`_)
* New init_scripts support for running customization scripts on QGIS launch
  (see :ref:`system_admin`)
* GDAL/OGR updated to 2.2.0 (see `GDAL 2.2 changelog`_)
* pgAdmin III replaced by pgAdmin 4 (code-signed)
* Updated Boundless Connect plugin
* New Master Password Helper (C++ core plugin)
* New OAuth2 authentication method (C++ core plugin)
* New Reporting Tool plugin and createreport command line script
* New 'Boundless Documentation' URL link in Start menu and shortcuts on
  user's desktop
* OpenGeo QGIS logo dropped in favor of the official QGIS 2.x logo
* Numerous bug fixes

.. QgsSettings (a QGIS 3.0 feature) backported to 2.18 Boundless release
   branch
.. New qgis_global_setting.ini customization file, with Boundless plugins and
   plugin repo enabled by default
.. Added custom OpenSSL and QtNetwork builds, and OpenSSL configuration for
   CAPI backend engine, to support Keystore plugin
.. New winhttp-head.exe sub.domain.tld utility for auto-loading missing CAs of
   endpoints in Win cert store (overcomes Qt4 flaw)

.. _QGIS 2.18 visual changelog: https://www.qgis.org/en/site/forusers/visualchangelog218/index.html
.. _GDAL 2.2 changelog: https://trac.osgeo.org/gdal/wiki/Release/2.2.0-News