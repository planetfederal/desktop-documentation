Python interpreter
==================

A full Python interpreter install is embedded within Boundless Desktop. Desktop does not use any Python interpreter or modules that you have installed on your system.

To manage packages available to the embedded Python install, open the included Command Shell application (as an administrator) and use ``pip``:

::

        pip --help

Please see `pip documentation <https://pip.pypa.io/en/stable/>`_ for more details.

Pre-installed Packages
----------------------

The ``IPython`` and ``Jupyter`` packages are installed with Desktop. This allows for easy installation of the `IPyConsole plugin <http://plugins.qgis.org/plugins/IPyConsole/>`_ for QGIS, an excellent additional console to QGIS's embedded Python console.

Know issues
...........

**IPython and Jupyter consoles on Windows**

When using the Command Shell application, the following commands will produce errors:

* ``ipython``
* ``jupyter-console``

Alternatively, until a fix is provided, you can run these commands:

* ``ipython --simple-prompt``
* ``jupyter-qtconsole`` (when run from a graphical user interface login)
