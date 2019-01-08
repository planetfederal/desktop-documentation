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
  pre-scripted terminal application, providing a mechanism for running Desktop
  command line utilities as well as providing a Python console [need version
  number as well as more detain about scripts/customization]

.. * :program:`PgAdmin 4` |pgadmin_version| (Optional) by `<http://www.pgadmin.org>`_

.. Feature-rich Open Source administration and development platform
     for `PostgreSQL <https://www.postgresql.org/>`_, the most advanced Open Source
     database in the world, which includes, among others, the `Postgis
     <http://postgis.org/>`_ spatial extension.

(See :ref:`components` section for more details on each component)

Components dependencies and tools
.................................

To support the core components functionality the core components are bundled with
the following tools:

* :program:`GDAL/OGR` |gdal_version| by `<http://www.gdal.org>`_

  Geospatial Data Abstraction Library (GDAL/OGR) is a cross-platform C++
  translator library for raster and vector geospatial data formats, which
  supports over 50 raster formats, and OGR over 20 vector formats.

* :program:`Python` |python_version| interpreter by `<http://www.python.org>`_

  Object-oriented, interpreted, and interactive programming
  language,  it combines remarkable power with very clear syntax. Python is also
  usable as an extension language for applications written in other languages
  that need easy-to-use scripting or automation interfaces, which is the case of
  QGIS, which uses python as its backbone for scripting and plugin creation.

* :program:`SAGA` |saga_version| by http://www.saga-gis.org/

  SAGA (System for Automated Geoscientific Analyses) is a GIS software that has
  been designed for an easy and effective implementation of spatial algorithms.
  It offers a comprehensive, growing set of geoscientific methods.

  In Boundless Desktop, SAGA GUI is not exposed, and it works exclusively as an
  extra provider for QGIS processing framework.

* :program:`GRASS` |grass_version| by https://grass.osgeo.org/

  GRASS (Geographic Resources Analysis Support System), is a free and open
  source GIS software suite used for geospatial data management and analysis,
  image processing, graphics and maps production, spatial modeling, and visualization.

  In Boundless Desktop, GRASS GUI is not exposed, and it works exclusively as an
  extra provider for QGIS processing framework.

..  * :program:`Orfeo Toolbox` |otb_version| by https://www.orfeo-toolbox.org`

Proprietary drivers
...................

To support the core components functionality and ensure compatibility with
not-so-open tools, the core components are bundled with the following proprietary
drivers:

* :program:`MrSID SDK` |mrsid_drv_version| for GDAL  by
  https://www.extensis.com/ - adds read and visualization support to MrSID/MG4
  compressed raster and LiDAR files.

* :program:`ERDAS ECW/JP2 SDK` |ecw_version| for GDAL by
  https://www.hexagongeospatial.com/ - adds read and write (limited to
  500mb) support for ECW and JPEG2000 formats.

* :program:`ESRI FileGDB API driver` |filegdb_version| for GDAL by
  https://www.esri.com - Read and Write support for vector layer in ESRI File
  Geodatabases.

* :program:`Oracle Geospatial DB client libraries` |oracle_version| by
  https://www.oracle.com - Adds read and write support support to Oracle spatial
  database connections from within QGIS.

Plugins
-------

Boundless Desktop is also extended by a set of :ref:`Boundless-supported plugins
<qgis.plugins>` for QGIS. The plugins are aimed at improving QGIS functionality,
but also for better integration with other Boundless products, like
:server:`Boundless Server <>` and :exchange:`Boundless Exchange <>`.

**THE FIGURE MUST BE REDONE OR REMOVED**

.. figure:: img/boundless_desktop_simplified_ecosystem.png

   Boundless Desktop ecosystem

.. Commenting until necessary The central element of our QGIS installation is the
   :bd_plugins:`Boundless connect plugin <connect/1.1>`, which acts
   as a single entry point to Boundless technology and content for QGIS. This
   provides access to :connect:`Boundless Connect <>`
   content, which currently includes Boundless-supported plugins, basemaps,
   and knowledge-based content, like documentation, tutorials and lessons
   for lessons plugins.

Security
--------

- Full control of the source code provenance by fully building all binaries for
  all components and its dependencies.
- Security scans (Fortify, SonarQube, Dependency Checker) at multiple parts of
  the building pipeline.

**THE FIGURE NEEDS A SIMPLIFIED VERSION**

.. figure:: img/BD_2.0_pipeline.png

Testing and QA
--------------

Each Boundless Desktop release is smoke-tested ensuring broadly that the
software performs as expected.

Support
-------

Boundless Desktop is not composed solely of zeros and ones! It also comes with
the deep technical knowledge and immediate readiness of our experts. From
product maintenance to day-to-day online support, whatever are your needs,
there is a support plan suited for you (get more information
`here <https://boundlessgeo.com/boundless-desktop-gis-software-mapping-solutions/>`_).
