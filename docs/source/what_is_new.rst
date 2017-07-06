What's new in 1.1.0
===================

This version contains numerous component upgrades and bug fixes. Highlights
include:

* GDAL/OGR updated to 2.2.0 (see `GDAL 2.2 changelog`_).
* pgAdmin III replaced by pgAdmin 4 (code-signed).
* QGIS updated to 2.18.10 which includes lots of new features and
  improvements (see `QGIS 2.18 visual changelog`_), including:

  * Native support for XYZ tile layers;
  * Native support for reading Map and Feature Services published by ArcGIS
    Server in Esri REST format;
  * New styling panel.
* New customization support (see :ref:`system_admin`):

  * QgsSettings support allowing to define global defaults and settings in a
    :file:`qgis_global_setting.ini` file (future QGIS 3.0 feature, currently
    available only on QGIS 2.18 for Boundless Desktop);
  * :file:`init_scripts` support for running customization scripts on QGIS
    launch.
* Several improvements in :ref:`Boundless Connect Plugin <connect_plugin>`,
  including:

  * Search for basemaps from partners providers;
  * Use Mapbox Streets basemap in QGIS default project;
  * Search and install lessons for lessons plugin.
* New :ref:`Master Password Helper <master_password_helper>` plugin (C++
  core plugin).
* New :ref:`Support Tool <support_tool_plugin>` plugin (core plugin) and
  ``createreport`` command line script (see :ref:`asking_for_support` page for
  instructions).
* New :ref:`Terrain Analysis <terrain_analysis>` plugin\*
* New :ref:`Image Discovery <image_discovery>` plugin\*
* Several improvements to :ref:`Web App Builder <web_app_builder>` plugin\*,
  including:

  * Updates WebSDK;
  * New WebSDK compiler service;
  * Enhanced support to advanced layer styling.
* Several enhancements to PKI authentication method support.
* New support for OAuth2 authentication method.
  (See :ref:`OAuth2 Plugin <oauth2>`)
* Improved symbology integration with other products from Boundless ecosystem
  using Mapbox GL Style library.
* New 'Boundless Documentation' URL link in Start menu and shortcuts on
  user's desktop
* "OpenGeo QGIS" logo replaced by the official QGIS 2.x logo

\* - Available in Boundless QGIS Plugin repository (see :ref:`qgis.plugins`).

.. Added custom OpenSSL and QtNetwork builds, and OpenSSL configuration for
   CAPI backend engine, to support Keystore plugin
.. New winhttp-head.exe sub.domain.tld utility for auto-loading missing CAs of
   endpoints in Win cert store (overcomes Qt4 flaw)

.. _QGIS 2.18 visual changelog: https://www.qgis.org/en/site/forusers/visualchangelog218/index.html
.. _GDAL 2.2 changelog: https://trac.osgeo.org/gdal/wiki/Release/2.2.0-News