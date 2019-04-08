.. _what_is_boundless_desktop:

What is Boundless Desktop?
==========================

Boundless Desktop is the commercially-supported version of the open source QGIS
project and GIS toolkit, providing the ability to manage, analyze, and
disseminate your geospatial data under open standards without sacrificing the
security of an Enterprise solution. Powered by proven open source projects with
premier support, Boundless Desktop gives you the control and tools to unlock
your location-based data for maximum bottom-line impact.

Components
----------

Core components
...............

Boundless Desktop |version| is composed of the following core components:

* :program:`QGIS` |qgis_version| by http://www.qgis.org

  The well known leading Open Source GIS for desktop, QGIS, is a cross-platform
  desktop application for viewing, editing, and analysing geospatial data from a
  variety of (proprietary and open) vector, raster, and database formats.

* :program:`Qt Designer` |qt_design_version| for QGIS by `<http://www.qt.io>`_

  Qt's Framework tool for designing and building graphical user interfaces
  (GUIs) from Qt components. With it, you can compose and customize widgets or
  dialogs in a what-you-see-is-what-you-get (WYSIWYG) manner, and also test them
  using different styles and resolutions. The tool has been extended with QGIS
  widgets (*e.g.*, project layer selector).

* :program:`Command Shell` (Optional) - for convenience, users are provided a
  pre-scripted terminal application with environment variable preconfigured for
  running Desktop command line utilities as well as providing a Python 3 console
  with access to the QGIS 3 Python API.
.. * :program:`PgAdmin 4` |pgadmin_version| (Optional) by `<http://www.pgadmin.org>`_

.. Feature-rich Open Source administration and development platform
     for `PostgreSQL <https://www.postgresql.org/>`_, the most advanced Open Source
     database in the world, which includes, among others, the `Postgis
     <http://postgis.org/>`_ spatial extension.

(See :ref:`components` section for more details on each component)

Dependencies and tools
......................

To support the core components functionality the core components are bundled with
the following tools:

* :program:`GDAL/OGR` |gdal_version| by http://www.gdal.org

  Geospatial Data Abstraction Library (GDAL/OGR) is a cross-platform C++
  translator library for raster and vector geospatial data formats, which
  supports over 50 raster formats, and OGR over 20 vector formats.

* :program:`Python` |python_version| interpreter by http://www.python.org

  Object-oriented, interpreted, and interactive programming
  language,  it combines remarkable power with very clear syntax. Python is also
  usable as an extension language for applications written in other languages
  that need easy-to-use scripting or automation interfaces, which is the case of
  QGIS, which uses python as its backbone for scripting and plugin creation.

* :program:`SAGA` |saga_version| by http://www.saga-gis.org

  SAGA (System for Automated Geoscientific Analyses) is a GIS software that has
  been designed for an easy and effective implementation of spatial algorithms.
  It offers a comprehensive, growing set of geoscientific methods.

  In Boundless Desktop, SAGA GUI is not exposed, and it works exclusively as an
  extra provider for QGIS processing framework.

* :program:`GRASS` |grass_version| by https://grass.osgeo.org

  GRASS (Geographic Resources Analysis Support System), is a free and open
  source GIS software suite used for geospatial data management and analysis,
  image processing, graphics and maps production, spatial modeling, and visualization.

  In Boundless Desktop, GRASS GUI is not exposed, and it works exclusively as an
  extra provider for QGIS processing framework.

..  * :program:`Orfeo Toolbox` |otb_version| by https://www.orfeo-toolbox.org`

To support the core components functionality and ensure compatibility with
not-so-open tools, the core components are bundled with the following proprietary
drivers:

* :program:`MrSID SDK` |mrsid_drv_version| for GDAL  by
  https://www.extensis.com - adds read and visualization support to MrSID/MG4
  compressed raster and LiDAR files.

* :program:`ERDAS ECW/JP2 SDK` |ecw_version| for GDAL by
  https://www.hexagongeospatial.com - adds read and write (limited to
  500mb) support for ECW and JPEG2000 formats.

* :program:`ESRI FileGDB API driver` |filegdb_version| for GDAL by
  https://www.esri.com - Read and Write support for vector layer in ESRI File
  Geodatabases.

* :program:`Oracle Geospatial DB client libraries` |oracle_version| by
  https://www.oracle.com - Adds read and write support support to Oracle spatial
  database connections from within QGIS.

Plugins
.......

Boundless Desktop is also extended by a set of both community and
:ref:`Boundless-supported plugins <qgis.plugins>` for QGIS. The plugins are
aimed at improving QGIS functionality, but also for better integration with
other Boundless products, like :server:`Boundless Server <>` and
:exchange:`Boundless Exchange <>`.

(See :ref:`qgis.plugins` section for more details on the available plugins)

.. figure:: img/boundless_desktop_simplified_ecosystem.png

   Boundless Desktop ecosystem

Offline documentation
.....................

For convenience, a documentation bundle is shipped with the installer. This allows
offline access to the following:

* **Boundless Desktop Documentation** - the current pages, which also include
  Boundless plugins for QGIS Documentation with installation and usage
  instructions.

* **QGIS User manual** - extensive user manual created by the community. The QGIS
  application help buttons, normally linked to this online document, will
  fallback to the offline version, if there is no internet connection.

* **PyQGIS Cookbook** - PyQGIS instruction and recipes created by the community
  on how to use the QGIS classes and methods with Python

Security
--------

Commercial support, among other things, means security. In order to support
rapidly changing customer needs or respond to customer-specific security
standards, Boundless Desktop is composed of a modernized, open, conda-forge
development stack. That means as software components age or upgrade, user needs
change, or a bug is identified, it can be addressed quickly by targeting a
single package in a plug-and-play packaging methodology, supported by a
community based approach.

- Full control of the source code provenance by fully building all binaries for
  all components and its dependencies.
- Security scans (Fortify, SonarQube, Dependency Checker) at multiple parts of
  the building pipeline.

Testing and QA
--------------

During development, we use continuous integration with a Docker QGIS testing
environment, testing every single change to code.

For plugins, we have created the Tester plugin, which allows us to run
manual and semi-automatic tests in a much more effective way.

Besides, each Boundless Desktop release is tested manually for core components
functionality (in most cases, also with the help of the Tester plugin) ensuring
broadly that the software performs as expected.

Support
-------

Boundless Desktop is not composed solely of zeros and ones! It also comes with
the deep technical knowledge and immediate readiness of our experts, both
internally and amongst the community. From product maintenance to day-to-day
online support through our ZenDesk, we have you covered.

.. USe Major version (x.y) if available

.. |qgis_version| replace:: 3.4
.. |qt_design_version| replace:: 5.9
.. |pgadmin_version| replace:: ?v3.?
.. |gdal_version| replace:: 2.4
.. |grass_version| replace:: 7.4
.. |saga_version| replace:: 2.3
.. |python_version| replace:: 3.7
.. |otb_version| replace:: 5.0
.. |mrsid_drv_version| replace:: 9.5
.. |ecw_version| replace:: 5.6
.. |filegdb_version| replace:: 1.5.1
.. |oracle_version| replace:: 12.1
