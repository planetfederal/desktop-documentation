QGIS Plugin Management
======================

System administrators have several tools that allow them to deliver and
install QGIS plugins for users.

Create common plugins folder
----------------------------

QGIS plugins are usually installed in the user's local space in a
specific profile folder.

 * GNU/Linux: ``/home/(user)/.local/share/QGIS/QGIS3/profiles/(profile)/python/plugins``
 * Windows: ``C:\Users\(user)\AppData\Roaming\QGIS\QGIS3\profiles\(profile)\python\plugins``
 * macOS: ``/Users/(user)/Library/Application Support/QGIS/QGIS3/profiles/(profile)/python/plugins``

In situations where users are not allowed to install plugins or when a
set of plugins must be available for all users (*e.g.*, for a training
course), the system administrator can extract plugin packages into a
folder and point the ``QGIS_PLUGINPATH`` environment variable to it.
This variable sets an extra location for QGIS to search for Python
plugins.

When QGIS is launched, all plugins in the specified folder will be loaded
(together with any plugins available on the user's local space).

With this method, the system administrator can, at any time, update,
add, and remove plugins from the folder, with the following advantages
when users reload QGIS:

 * If the folder is a shared location for the OS, it will affect all users
   on the machine.
 * If the folder is a mounted shared network location, this affects all
   machines and users using the shared folder.
