QGIS Plugin management
======================

System administrator have several tools that allow them to deliver and installed
QGIS plugins in the users machines.

Create common plugins folder
----------------------------

QGIS Plugins are usually installed at the user's local space in a specific profile
folder.

 * GNU/Linux: ``/home/(user)/.local/share/QGIS/QGIS3/profiles/(Profile)/python/plugins``
 * Windows: ``C:\Users\(user)\AppData\Roaming\QGIS\QGIS3\profiles\(profile)\python\plugins``

In situations that the users are not allowed to install plugins or when a
set of plugins must be available for all users (*e.g.*, for a training course),
the system administrator can extract the plugin packages into a network shared
folder and, in each machine, point the ``QGIS_PLUGINPATH`` environment variable
to it. This variable sets an extra location for QGIS to search for plugins.

When QGIS is launched, all plugins on the provided folder will be loaded
(together with any plugin available on the user's local space).

With this method, the system administrator can, at any time, update, add, and
remove plugins from the shared folder, which will take effect on all
machines/users once they reload QGIS.
