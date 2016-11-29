.. (c) 2016 Boundless, http://boundlessgeo.com
   This code is licensed under the GPL 2.0 license.


.. _intro:


IPython features
================

IPython has a `comprehensive online documentation <https://ipython.org/documentation.html>`_.


IPyConsole specific features
============================

Pre-import of the most common classes
*************************************

QGIS integration in the plugin, makes immediately available to the user the
following QGIS instances and classes:

* `iface`: instance of `QgisInterface`
* `canvas`: instance of `QgsMapCanvas`
* `core`: module `qgis.core`
* `gui`: module `qgis.gui`

For the user convenience, the most often used classes are already imported by
IPyConsole when the plugin starts::

   from PyQt4.QtCore import *
   from PyQt4.QtGui import *
   from qgis.core import *
   from qgis.gui import *


Propertize: better introspection for QGIS API
*********************************************

QGIS Python bindings are generated semi-automatically by SIP, the resulting
API is not "Pythonic" at all: most if not all accessors are functions and
not properties of the objects, this makes it impossible to build a long
auto-completion chain because the function calls break the chain.

Note that TAB-completion is not only useful to prevent typing errors but also
to explore the methods available in the QGIS API.

For example, if a user wanted to access to the CRS (Coordinate Reference System)
of a vector layer he'd normally do::

   layer.dataProvider().crs().authid()

the TAB-completion will break at the first parenthese.

Propertize adds a property (prefixed by `p_` to all returning-something and
zero-argument functions and methods in the QGIS API, so that a user can easily
do this::

   layer.p_dataProvider.p_crs.p_authid

in the above snippet, the TAB-completion will actually work.
