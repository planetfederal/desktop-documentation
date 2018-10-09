What is new in |version|
========================

1.1.1 Release
-------------

In Boundless Desktop 1.1.1 patch release, Boundless Desktop team focused mainly on bug fixing.
Nevertheless, there were some upgrades and new features as well:

* **QGIS** updated to 2.18.14.
* Activated QGIS Oracle data provider.
* Activated QGIS's QSpatialite (Qt) database driver.
* **GDAL/OGR** updated to :gdal_release:`2.2.2` (see also GDAL :gdal_release:`2.2.1` changelog).
* New OGR plugin for OGDI format.
* New OGR plugin for Oracle geospatial databases.
* New GDAL/OGR plugin for PDF format.
* **GRASS** updated to :grass_release:`7.2.2`.
* **Python** updated to 2.7.14 (Mac only).
* **PgAdmin 4** updated to :pgadmin_release:`2.0 <2_0>` (see also `:pgadmin_release:`1.6 <1_6>` release notes).
* **SAGA GIS** updated to LTS version
* New offline Desktop documentation included in installer.
* Support for TLS v1.2 in custom OpenSSL setup.
* Improvements to :ref:`Image Discovery <image_discovery>` plugin UI [#0]_.
* Several improvements to :ref:`Boundless Connect <connect_plugin>` search.

1.1.0 Release
-------------

This Boundless Desktop 1.1.0 release contains numerous component upgrades and bug fixes. The highlights
include:

* **GDAL/OGR** updated to :gdal_release:`2.2.0`.
* **pgAdmin III** replaced by **pgAdmin 4** :pgadmin_release:`1.5 <1_5>` (code-signed).
* **QGIS** updated to :qgis_changelogs:`2.18.10 <218>` which includes lots of new features and
  improvements (see also QGIS :qgis_changelogs:`2.16 <216>`), including:

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
* New :ref:`Terrain Analysis <terrain_analysis>` plugin [#0]_.
* New :ref:`Image Discovery <image_discovery>` plugin [#0]_.
* Several improvements to :ref:`Web App Builder <web_app_builder>` plugin [#0]_,
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
  user's desktop.
* "OpenGeo QGIS" logo replaced by the official QGIS 2.x logo.

For a complete list of new features, fixes, and known issues, please consult each platform README files:

* :download:`Windows <_static/README_win.txt>`
* :download:`Mac OSX <_static/README_osx.txt>`

.. rubric:: Footnotes

.. [#0] Available for installation in Boundless QGIS Plugin repository (see :ref:`qgis.plugins`).
