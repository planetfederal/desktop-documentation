* If Boundless Desktop |version| is installed in a custom directory as a sub-folder of
  a previous version's install directory, the uninstaller for the older version of
  Boundless Desktop (e.g. 1.1.1) will remove the newest version. However,
  using the default installation directory poses no issue, and removal of older
  versions won't affect the latest version.
* Boundless Desktop |version| installation changes application mapping for QGIS
  project files (qgs and qgz), dissociating them from the previous installation
  of QGIS. Uninstalling Boundless Desktop |version| after this change in application
  mapping will leave those files unmapped.
* Running QGIS from a pinned icon in the taskbar will prevent the execution of scripts
  in the init_script folder.
* Uninstaller leaves an empty ``Program Files\Boundless\Desktop\2.0`` directory
* Uninstaller on Windows 7 requires a system reboot before other programs can be
  uninstalled.
* Uninstallation on user workspace requires administrator permissions.
* Currently available version of IPython console plugin (v1.9) is not compatible with
  IPython 7.2, which is the version deployed with Boundless Desktop. The plugin
  will not work properly.
* Due to a problem in the OGDI driver, GDAL (and therefore QGIS) is not able to
  read OGDI ``VPF`` and ``RPF`` formats. The OGDI ``DTED`` format works as expected.

.. * In PgAdmin 4, in the SSL tab of the Create Server dialog, browsing to a file
     (e.g., for getting a Client certificate) will fill all the other certificate
     fields with that path. The user must clean and manually edit the other fields
     for the connection to work.
.. * In PgAdmin 4, while setting up an SSL connection, the user is asked to provide
     a password anyway. As a workaround, the user can just enter a fake password.

For a complete list of QGIS active regressions see:
https://issues.qgis.org/projects/qgis/issues?query_id=115
