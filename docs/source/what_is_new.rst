What is new in |version|
========================

2.0.0 Release
-------------

The Boundless Desktop 2.0.0 release contains numerous component upgrades, new
functionality, and bug fixes. The highlights include:

* QGIS updated to |qgis_version|
* GDAL/OGR updated to |gdal_version|
* GRASS updated to |grass_version|
* Python is now |python_version|
* Qt Designer updated to |qt_design_version|
* New installers both for Mac and Windows, which will allow partial package updates

.. * PgAdmin 4 updated to|pgadmin_version|

QGIS 3.4 receives a major update from its LTR predecessor (2.18). QGIS 3.4 is
based on Qt 5 and Python 3 and adds many new features. Some examples are:

* Support for user profiles
* Unified data source manager dialog
* Improved support for Geopackage, which is now the default format on
  processing tools
* Multiple map views
* 3D surface and layer rendering, with animations
* Support for running processes as background tasks, allowing the user to
  keep using QGIS interface while the job is running
* Improved layout creation including reports
* Master password integration with win, mac and linux keychains
* Locator bar for quick access to tools and commands
* Improved consistency to the user interface
* Tens of new expression functions, including array functions
* Improved expressions editor with auto-completion and error highlighting
* New units for symbols and layouts, including pixels and inches
* Point cluster renderer
* Easy styling of discrete rasters
* Note tool is replaced by a much improved and functional vertex tool
* Auxiliary storage support, which allows, for example, saving custom label
  positions on the project)
* Several Improvements to the feature forms and widgets, including drill-down
  (cascading) forms (aka domains and sub-domains in forms)
* Several new processing algorithms, and performance improvements to existing ones.
* Improved processing modeler window
* New Geonode data provider
* Opening of vector and raster stored on HTTP(S), FTP, or cloud services
* Save and load QGIS projects in PostgreSQL database
* Support for mesh layers (GRIB, XMDF, Netcdf)
* Automatically set default style for layers from ArcGIS Feature Server layers
* OpenCL based acceleration
* Polished browser panel interface and experience
* GPS tracking improvements
* Processing “Edit in place” mode
* Store processing models inside project
* OAuth2 authentication method plugin
* ESRI Token Authentication support
* Support for encrypted zips in the Plugin Manager¶

For a full list of new features check the visual changelogs for versions :qgis_changelogs:`3.0 <30>`, :qgis_changelogs:`3.2 <32>`, and :qgis_changelogs:`3.4 <34>`.

There were also some removals for this version:

* Standalone QGIS browser application has been deprecated
* Connect plugin will not be shipped in this release
* Boundless OAuth2 and Master Password plugins, has its functionality was integrated into
  QGIS 3 core
* Orfeo toolbox processing provider no longer ships with QGIS
* PgAdmin 4 was temporarily removed from installer

For a complete list of new features, fixes, and known issues, please consult each platform README files:

* :download:`Windows <_static/README_win.txt>`
* :download:`Mac OSX <_static/README_osx.txt>`


.. |qgis_version| replace:: 3.4
.. |qt_design_version| replace:: ?5.9?
.. |pgadmin_version| replace:: ?v3.?
.. |gdal_version| replace:: 2.3
.. |grass_version| replace:: 7.4
.. |saga_version| replace:: 2.3
.. |python_version| replace:: 3.6
.. |otb_version| replace:: 5.0
.. |mrsid_drv_version| replace:: ?9.5?
.. |ecw_version| replace:: ?5.6?
.. |filegdb_version| replace:: ?1.5.1?
.. |oracle_version| replace:: 12.2
