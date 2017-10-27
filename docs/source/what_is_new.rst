What is new in |version|
========================

1.1.0 Release
-------------

This Boundless Desktop 1.1.0 release contains numerous component upgrades and bug fixes. The highlights
include:

* **GDAL/OGR** updated to `2.2.0 <GDAL 2.2.0_>`_.
* **pgAdmin III** replaced by **pgAdmin 4 1.5** (code-signed).
* **QGIS** updated to `2.18.10 <QGIS 2.18 visual changelog_>`_ which includes lots of new features and
  improvements (see also QGIS `2.16 <QGIS 2.16 visual changelog_>`_), including:

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

\(*) - Available in Boundless QGIS Plugin repository (see :ref:`qgis.plugins`).

1.1.1 Release
-------------

In Boundless Desktop 1.1.1 patch release, Boundless Desktop team focused mainly on bug fixing.
Nevertheless, there were some upgrades and new features as well:

* **QGIS** updated to 2.18.13.
* Activated QGIS Oracle data provider.
* Activated QGIS's QSpatialite (Qt) database driver.
* **GDAL/OGR** updated to `2.2.2 <GDAL 2.2.2_>`_ (see also GDAL `2.2.1 <GDAL 2.2.1_>`_ changelog).
* New OGR plugin for OGDI format.
* New OGR plugin for Oracle geospatial databases.
* New GDAL/OGR plugin for PDF format.
* **GRASS** updated to `7.2.2 <GRASS GIS 7.2.2_>`_ changelog.
* **Python** updated to 2.7.14 (Mac only).
* **PgAdmin 4** updated to `2.0 <PgAdmin 4 2.0_>`_ (see also `1.6 <PgAdmin 4 1.6_>`_ release notes).
* New offline Desktop documentation included in installer.
* Support for TLS v1.2 in custom OpenSSL setup.
* Improvements to :ref:`Image Discovery <image_discovery>` plugin UI [#0]_.
* Several improvements to :ref:`Boundless Connect <connect_plugin>` search.

For a complete list of new features and fixes, please consult the README file
provided with Boundless Desktop installer.

.. rubric:: Footnotes

.. [#0] Available for installation in Boundless QGIS Plugin repository (see :ref:`qgis.plugins`).

.. _QGIS 2.16 visual changelog: https://www.qgis.org/en/site/forusers/visualchangelog216/index.html
.. _QGIS 2.18 visual changelog: https://www.qgis.org/en/site/forusers/visualchangelog218/index.html
.. _GDAL 2.2.0: https://trac.osgeo.org/gdal/wiki/Release/2.2.0-News
.. _GDAL 2.2.1: https://trac.osgeo.org/gdal/wiki/Release/2.2.1-News
.. _GDAL 2.2.2: https://trac.osgeo.org/gdal/wiki/Release/2.2.2-News
.. _GRASS GIS 7.2.2: https://trac.osgeo.org/grass/wiki/Release/7.2.2-News#Overviewofchanges
.. _PgAdmin 4 2.0: https://www.pgadmin.org/docs/pgadmin4/dev/release_notes_2_0.html
.. _PgAdmin 4 1.6: https://www.pgadmin.org/docs/pgadmin4/dev/release_notes_1_6.html