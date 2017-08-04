QGIS Global Settings File
=========================

Starting from Boundless Desktop 1.1, QGIS supports global settings: 
a feature that is currently only available in QGIS 3.x series.

Almost all settings for QGIS application are stored using the `QSettings`
framework that is provided by the `Qt` library upon which QGIS is built.

For every setting value, an optional default value can be specified inline 
in the application code, the global settings implementation allows the 
inline default values to be overridden by an external and totally optional
global settings file (in `.ini` format).

Therefore, by providing a global settings file, the order for a setting 
value lookup becomes:

- user settings file
- global settings file
- inline default

This global setting file can be used to provide pre-configuration and/or 
custom default values for all settings used inside QGIS.

QGIS Global settings and defaults can be set by editing the
``qgis_global_setting.ini`` file. Moreover, it is possible to overwrite the
path for the ``qgis_global_setting.ini``, by using one of the following:

* Specifying the file's path using the --globalsettings option when running
  QGIS. For instance:

  ::

     $ qgis --globalsettings /home/user/qgis_global_setting.ini

* Setting the ``QGIS_GLOBAL_SETTINGS_FILE`` environment variable with the file
  location.

.. tip::

   Setting the ``qgis_global_setting.ini`` file path to a network shared folder,
   allows the system administrator to change global settings and defaults
   in several machines by only editing one file.

If none of the two above methods is used, QGIS will use the file's default
location. On Windows, the default location folder is::

  C:\Program Files\Boundless\Desktop\1.1\osgeo4w\apps\qgis\qgis_global_setting.ini

While on Mac OS, the default location is::

  /Library/Boundless/Desktop/1.1/Cellar/qgis2-bdesk/2.18.10/QGIS for Boundless Desktop 1.1.app/Contents/MacOS/../Resources/qgis_global_setting.ini


Exporting QGIS settings to ini format
-------------------------------------

Since Windows and macOS versions of QGIS don't store settings in a ``.ini``
format, having to create a ``qgis_global_setting.ini`` file from scratch can be
a laborious task.

For that purpose, a script is available to dump QGIS QgsSettings to a ``.ini``
file. The resultant file can then be used to help populate a
``qgis_global_settings.ini`` file.


#. Download :download:`qgis-settings-to-ini.py` file to your machine.

#. From within QGIS, open the :guilabel:`Python Console`
   (:menuselection:`Plugins --> Python Console`).

#. In the :guilabel:`Python Console`, click the :guilabel:`Show Editor` button.

#. In the Editor toolbar, click the :guilabel:`Load Script`, browse to the
   :download:`qgis-settings-to-ini.py` file and click :guilabel:`Open`.

#. Finally, click the :guilabel:`Run script` button.

A message in the :guilabel:`Python Console` will inform you the path of the
output file.