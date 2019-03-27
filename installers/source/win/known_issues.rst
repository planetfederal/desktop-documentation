* If Boundless Desktop |version| is installed in a custom directory as a sub-folder of
  the previous install directory, Boundless Desktop older version uninstaller
  (e.g. 1.1.1) will remove the newest version. However, using the default
  installation directory poses no issues, and the older versions removal won't
  affect the latest ones.
* Boundless Desktop |version| installation changes QGIS project files (qgs
  and qgz) application mapping, disconnecting them from previous installation of
  QGIS. In the same way, uninstalling Boundless Desktop |version| will leave
  those files unmaped.
* Uninstaller leaves an empty ``Program Files\Boundless\Desktop\2.0`` directory
* Current available versions of IPython console plugin (v1.9) is not compatible with
  IPython 7.2, which is the version deployed with Boundless Desktop. The plugin
  will not work properly.

.. * In PgAdmin 4, in the SSL tab of the Create Server dialog, browsing to a file
     (e.g., for getting a Client certificate) will fill all the other certificate
     fields with that path. The user must clean and manually edit the other fields
     for the connection to work.
.. * In PgAdmin 4, while setting up an SSL connection, the user is asked to provide
     a password anyway. As a workaround, the user can just enter a fake password.

For a complete list of QGIS active regressions see:
https://issues.qgis.org/projects/qgis/issues?query_id=115
