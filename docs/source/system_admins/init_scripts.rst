QGIS Initialization scripts
===========================

QGIS has the native ability to run a specified Python script when it starts.
By loading an init script that will in turn load and run all the scripts in
a given directory, this system allows Boundless Desktop's QGIS to be configured
every time it starts.

Setting the scripts path to a network shared folder, allows the system
administrator to perform QGIS configuration tasks in several machines by simply
adding or changing the scripts in that folder.

Usage
-----

Set the ``QGIS_INIT_SCRIPTS_DIRECTORY`` environment variable to a directory path
containing Python scripts to run at QGIS start, if the variable
is not set, QGIS will look in a default local folder determined by
``QgsApplication.pkgDataPath()`` + ``/init_scripts``.

On Windows, the default local folder is::

  C:\Program Files\Boundless\Desktop\2.0\Library\apps\qgis\init_scripts

On Mac OS, the default local folder is::

  /Library/Boundless/Desktop/2.0/apps/QGIS for Boundless Desktop.app/Contents/Resources/init_scripts


.. tip::

  Setting the ``QGIS_INIT_SCRIPTS_DIRECTORY`` environment variable to a network
  shared folder, allows the system administrator to perform configuration tasks
  in several machines by simply adding or changing the scripts in that folder.

.. note::

   **Scripts are alphabetically sorted**

   Scripts run in alphabetically order, so if necessary prefix them with
   with some integers.

.. warning::

   In Windows, if the ``QGIS_INIT_SCRIPTS_DIRECTORY`` environment variable is
   set to a folder other than the default one, the
   :file:`000_win_load_authorities.py` script must be copied from the default
   `init_scripts` folder to the new one. Otherwise, when trying to connect to
   some services endpoints, users may receive SSL Errors warnings
   claiming that a valid certificate for that URL is not available.

Scripts examples
----------------

Inside the ``init_scripts`` default folder there is an ``examples`` folder with
some example scripts to illustrate a few common customization tasks, which
are transcript below.

.. tip::

   In order to run the examples, you can set ``QGIS_INIT_SCRIPTS_DIRECTORY``
   environment variable to point to the examples directory before launching
   QGIS as specified above.

Checking for a setting value
............................

.. literalinclude:: script_examples/001_settings.py

Single run script
.................

.. literalinclude:: script_examples/002_runonce.py
   :language: python

Install a plugin from a zip file
................................

.. literalinclude:: script_examples/003_plugin_install.py
   :language: python

Add a WMS connection
....................

.. literalinclude:: script_examples/004_wms_add_config.py
   :language: python

Set a default project
.....................

.. literalinclude:: script_examples/005_add_default_project.py
   :language: python

Add an authentication configuration
...................................

.. literalinclude:: script_examples/006_add_authcfg.py
   :language: python

Show a message on start up
..........................

.. literalinclude:: script_examples/007_info_dialog.py
   :language: python
