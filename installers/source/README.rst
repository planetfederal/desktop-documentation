.. |minorversion| replace:: 2.0

Boundless Desktop |version|
===========================

Boundless Desktop is the commercially-supported version of the open source QGIS project and GIS toolkit, providing the ability to manage, analyze, and disseminate your geospatial data under open standards without sacrificing the security of an Enterprise solution.
Powered by proven open source projects with premier support, Boundless Desktop gives you the control and tools to unlock your location-based data for maximum bottom-line impact.

.. only:: win

   .. include:: /win/supported_components.rst

.. only:: osx

   .. include:: /osx/supported_components.rst


For convenience, outside the supported scope of Boundless Desktop, the following components are provided:

.. only:: win

   .. include:: /win/additional_components.rst

.. only:: osx

   .. include:: /osx/additional_components.rst


To support the core components functionality and ensure compatibility with not-so-open tools, the core components are bundled with the following proprietary drivers

.. only:: win

   .. include:: /win/proprietary_components.rst

.. only:: osx

   .. include:: /osx/proprietary_components.rst

Boundless Desktop was built upon the remaining open source dependencies:

   .. only:: win

      .. include:: /win/dependencies.rst

   .. only:: osx

      .. include:: /osx/dependencies.rst


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

Copyright (C) 2009-2019 Boundless
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

.. * PgAdmin official documentation:

..   http://www.pgadmin.org/docs

* GDAL/OGR official documentation:

  http://www.gdal.org

* Qt Designer Manual:

  http://doc.qt.io/qt-5/qtdesigner-manual.html
