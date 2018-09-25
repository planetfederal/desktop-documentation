* If Boundless Desktop 1.1 is installed in a custom directory as a sub-folder of
  the previous install directory, Boundless Desktop older version uninstaller
  (e.g. 1.0.1) will remove the newest version. However, using the default
  installation directory poses no issues, and the older versions removal won't
  affect the latest ones.
* Uninstaller leaves an empty ``Program Files\Boundless\Desktop\1.1`` directory
* In PgAdmin 4, in the SSL tab of the Create Server dialog, browsing to a file
  (e.g., for getting a Client certificate) will fill all the other certificate
  fields with that path. The user must clean and manually edit the other fields
  for the connection to work.
* In PgAdmin 4, while setting up an SSL connection, the user is asked to provide
  a password anyway. As a workaround, the user can just enter a fake password.

For a complete list of QGIS 2.18 LTS active regressions see:
https://issues.qgis.org/projects/qgis/issues?query_id=143
