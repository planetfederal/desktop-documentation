* QGIS.app from Desktop install may not show up in Spotlight search until after initial launch.
* Due to a Qt bug in Mac OS undocking panels may cause QGIS to crash (e.g. Styling Panel)
* PyQt4-Phonon module is broken on Mac OS
* In QGIS, using the Quick field calculator, the attribute table won't update until you scroll down.
* In PgAdmin 4, in the SSL tab of the Create Server dialog, browsing to a file
  (e.g., for getting a Client certificate) will fill all the other certificate
  fields with that path. The user must clean and manually edit the other fields
  for the connection to work.
* In PgAdmin 4, while setting up an SSL connection, the user is asked to provide
  a password anyway. As a workaround, the user can just enter a fake password.


For a complete list of QGIS 2.18 LTS active regressions see:
https://issues.qgis.org/projects/qgis/issues?query_id=143
