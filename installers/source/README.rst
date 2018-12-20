.. |minorversion| replace:: 1.1

Boundless Desktop |version|
===========================

Boundless Desktop is a full-featured, professional desktop GIS that supports the management, analysis, visualization and dissemination of your geospatial data.
Powered by QGIS, a proven open source geospatial software, Desktop combines innovative open source projects with premier support, certiication and security, giving you the control and tools to unlock your location-based data for maximum bottom-line impact. The current version (|release|) includes:

.. only:: win

   .. include:: /win/supported_components.rst

.. only:: osx

   .. include:: /osx/supported_components.rst

For convenience, outside the supported scope of Boundless Desktop, the following components are provided:

.. only:: win

   .. include:: /win/additional_components.rst

.. only:: osx

   .. include:: /osx/additional_components.rst

Python interpreter
------------------

A full Python interpreter install is embedded within Desktop. Desktop does not use any Python interpreter or modules that you have installed on your system.

To manage packages available to the embedded Python install, open the included Command Shell application (as an administrator) and use ``pip``:

::

        pip --help

See ``pip`` docs for more details:

https://pip.pypa.io/en/stable/

The ``IPython`` and ``Jupyter`` packages are installed (see **Known Issues** on Windows). This allows for easy installation of the **IPyConsole** plugin for QGIS, an excellent additional console to QGIS's embedded Python console.

http://plugins.qgis.org/plugins/IPyConsole/

System requirements
-------------------

Boundless Desktop has the following minimum and recommended system requirements:

.. only:: win

   .. include:: /win/system_requirements.rst

.. only:: osx

   .. include:: /osx/system_requirements.rst

Install
-------

There are 64-bit installers available for both Windows and Mac OS X in:

https://connect.boundlessgeo.com/Downloads

.. only:: win

   .. include:: /win/install_uninstall.rst

.. only:: osx

   .. include:: /osx/install_uninstall.rst

License
-------

Copyright (C) 2009-2018 Boundless
http://boundlessgeo.com/

For more details, please consult the Boundless End User License Agreement (EULA) during installation. You can review the EULA and individual licenses for components of Desktop in the Licenses folder located within the installation folder.

Known issues
------------

.. only:: win

   .. include:: /win/known_issues.rst

.. only:: osx

   .. include:: /osx/known_issues.rst

Changelog
---------

.. only:: win

   .. include:: /win/version_changelog.rst

.. only:: osx

   .. include:: /osx/version_changelog.rst

Online resources
----------------

* Boundless Desktop Documentation:

  https://connect.boundlessgeo.com/docs/desktop/|release|/index.html

* Boundless Connect:

  https://connect.boundlessgeo.com

* Boundless Spatial website:

  http://boundlessgeo.com

* QGIS official documentation:

  http://www.qgis.org/en/docs

* PgAdmin official documentation:

  http://www.pgadmin.org/docs

* GDAL/OGR official documentation:

  http://www.gdal.org

* Qt Designer Manual:

  http://doc.qt.io/qt-5/qtdesigner-manual.html

Proprietary software
--------------------

Proprietary software, included with Desktop, has its provenance from the
following sources.

* MrSID raster and LiDAR decompression driver support for GDAL/OGR

  - (LizardTech Computer Software License)

  - https://www.lizardtech.com/gis-tools/server-development-kit

* ECW, ECWP and JPEG2000 driver support for GDAL

  - (ERDAS ECW/JP2 Desktop Read-Only Redistributable SDK License)

  - http://www.hexagongeospatial.com/products/provider-suite/erdas-ecw-jp2-sdk

.. only:: win

   .. include:: /win/proprietary_components.rst

.. only:: osx

   .. include:: /osx/proprietary_components.rst
