Setting QGIS Global settings file
=================================

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

