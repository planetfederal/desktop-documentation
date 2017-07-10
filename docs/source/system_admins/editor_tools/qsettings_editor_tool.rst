QSettings editor tool
=====================

This editor tool allows you to edit `QSettings`.

The tool's arguments can be listed by running the tool with the ``-h``
option:

::

  $ tools/qsettings/editor.py -h
  usage: editor.py [-h] [--org_name ORG_NAME] [--org_domain ORG_DOMAIN]

                   [--app_name APP_NAME] [-d] [-s] [-v VALUE] [--debug]
                   key

  QSettings editor.

  positional arguments:
    key                   Get or set a single entry with this key (set requires
                          --name)

  optional arguments:
    -h, --help            show this help message and exit
    --org_name ORG_NAME   Organisation name (default=QGIS)
    --org_domain ORG_DOMAIN
                          Organisation domain (used on OSX, default=qgis.org)
    --app_name APP_NAME   Application name (default=QGIS2)
    -d, --delete          Delete a single entry (requires --key)
    -s, --strict          Strict mode
    -v VALUE, --value VALUE
                          Set a single entry with this value
    --debug               Print debug information

Arguments
---------

In addition to the mandatory arguments in common for all tools, the following
optional arguments can be specified:


* ``org_name``: Organisation Name (default=QGIS)
* ``org_domain``: Organisation Domain (used on OSX, default=qgis.org)
* ``app_name``: Application Name (default=QGIS2)

Examples
--------

To disable the default official plugin repository:

::

  ./editor.py --value false "Qgis/plugin-repos/QGIS Official Plugin Repository/enabled"



To add a new repository:

::

  ./editor.py --value "http://plugins-server.cfapps.io/plugins.xml" "Qgis/plugin-repos/QGIS Custom Plugin Repository/url"

To disable the QuickWKT Python plugin:

::

  ./editor.py --value=false PythonPlugins/QuickWKT

