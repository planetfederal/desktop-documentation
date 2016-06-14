.. _components:

Boundless Desktop components
============================

QGIS
----

QGIS is the central piece of the Boundless Desktop package installation. The well known leading Open Source GIS for desktop, QGIS, is a cross-platform desktop application for viewing, editing, and analyzing geospatial data from a variety of (proprietary and open) vector, raster, and database formats.

QGIS’s development is steered by the QGIS Project, which works with hundreds of volunteers and companies (including Boundless spatial) from all over the world, that helps enhance and maintain QGIS.

For convenience, outside the supported scope of Boundless Desktop, the following processing providers are available for QGIS’s Processing framework:

* SAGA 2.1 by www.saga-gis.org
* GRASS 7.0 by grass.osgeo.org
* Orfeo Toolbox 5.0 by www.orfeo-toolbox.org

Quick start guide
~~~~~~~~~~~~~~~~~

Project's Documentation
~~~~~~~~~~~~~~~~~~~~~~~

Boundless plugins for QGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~

pgAdmin
-------

“pgAdmin is the most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world. (...)
pgAdmin is designed to answer the needs of all users, from writing simple SQL queries to developing complex databases. The graphical interface supports all PostgreSQL features and makes administration easy. The application also includes a syntax highlighting SQL editor, a server-side code editor, an SQL/batch/shell job scheduling agent, (...) and much more. pgAdmin is developed by a community of PostgreSQL experts around the world and is available in more than a dozen languages. It is Free Software released under the PostgreSQL License.” in www.pgadmin.org (2016-05-18) 

Qt designer for QGIS
--------------------

“Qt Designer is Qt [Framework]'s tool for designing and building graphical user interfaces (GUIs) from Qt components. You can compose and customize your widgets or dialogs in a what-you-see-is-what-you-get (WYSIWYG) manner, and test them using different styles and resolutions.” in www.qt.io (2016-05-18)

The shipped version brings a set of special widgets for QGIS that make it easier to create custom forms and dialogs for your PyQGIS projects and custom attribute editing forms within QGIS.

For more information on Qt Designer usage, check the Qt Designer Documentation. 

GDAL/OGR
--------

“Geospatial Data Abstraction Library (GDAL/OGR) is a cross-platform C++ translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful command line utilities for data translation and processing.
GDAL supports over 50 raster formats, and OGR over 20 vector formats.” in www.osgeo.org (2016-05-18)

In Boundless Desktop installation, GDAL/OGR utilities are available through QGIS or the installed  Command Shell. The shipped version of GDAL/OGR includes two extra libraries, LibKML and  OpenJPEG2, for .kmz and JPEG2000 support, respectively.
