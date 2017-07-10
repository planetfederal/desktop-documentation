System administration tools
===========================

Boundless Desktop comes with a collection of Python tools to ease its
configuration and maintenance. The collection is composed by a master
Orchestrator application (``config_editor.py``) that executes the commands
contained in a json script by calling the editor tool specialized for the
particular settings format.

Every editor tool is a command line application able to edit a particular
settings format. For instance, the qsettings editor tool will edit `QSettings`
files.

All the editor tools have a common interface, but they may have additional
arguments. Each tool arguments can be listed from the command line by
using the ``-h`` argument. For example::

  tools/qsettings/editor.py -h

Currently, only the **QSettings Editor Tool** is available, which, thanks to a
QGIS 3.0 feature backport to version 2.18 (uniquely for including in Boundless
Desktop), allows editing QGIS configuration.

Orchestrator
------------

The orchestrator is a command line application to read configuration commands
from a JSON file and run them using the individual editor tools.

The path of the JSON script file can be specified on the command line by using
the ``-c`` argument or by using the environment variable
``BOUNDLESS_DESKTOP_CONFIG_PATH``

Running the application with the `-h` will list all its arguments.

::

  usage: config_editor.py [-h] [-c CONFIG] [-v]

  Boundless Desktop settings editor.

  optional arguments:
    -h, --help            show this help message and exit
    -c CONFIG, --config CONFIG
                          Path to the config file (also read from
                          BOUNDLESS_DESKTOP_CONFIG_PATH environment variable)
    -v, --verbose         Print debug information on stdout



The Orchestrator tool can be run with:

::

  $ config_editor.py  -c /path/to/the/script.json

Script JSON file syntax
.......................

The commands can be specified in a JSON script:

* ``format``: defines the tool to be used to edit the settings
  other arguments may depend on the tool (see the arguments accepted from the
  tool)
* ``actions``: a collection of actions

  * ``action``: can be set or delete
  * ``name``: name of the setting to be set or deleted
  * ``value``: the value of the setting to be set
  * ``strict``: will raise and error if the setting to be set already exists or
    if the setting to be deleted does not exist

Example commands to set one entry and delete another entry using the qsettings format:

.. code-block:: JSON

   [
       {
           "format": "qsettings",
           "app_name": "QGIS2",
           "org_name": "TEST_QGIS",
           "org_domain": "qgis.test",
           "actions" : [
               {
                   "action": "set",
                   "name": "Section/OptionalSubSections/Name",
                   "value": "A value for this setting",
               },
               {
                   "action": "delete",
                   "name": "Section/OptionalSubSections2/Name",
                   "strict": false
               }
           ]
       }
   ]

.. TODO:: Explain how to use this tools from the command line

Editor tools
------------

.. toctree::
   :maxdepth: 1
   :glob:

   editor_tools/*

