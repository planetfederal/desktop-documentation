.. _command_line_install:

Command line install
====================

The Boundless desktop installer allows headless installation, which for system
administrators may be quicker and more convenient than using the graphical user
interface (GUI).

Several options are available::

  Boundless-Desktop-2.0.0-x64.exe [option=value], ...

  /S                 Silent install, mandatory for headless installation
  /InstallationType  Defines the type of installation
                     [AllUsers|JustMe]
                     Default: JustMe
  /NoRegistry        Don't write on the registry
                       [0|1] (False|True)
                       default: 0 (False)
  /D                 Path to installation prefix.
                     [path_to_prefix]
                     Defaults:
                       AllUsers: c:\AplicationData\Boundless\Desktop
                       JustMe: c:\Users\<user>\

.. note::

   One drawback of this type of installation is that there is no visual feedback
   on the installation progress. For this reason, it's recommended to preseed
   the command with::

     start "" /wait /b [install command]

    Using this command, the command prompt will be inactive until the
    installation is finishes.

Usage examples
--------------

Single-user installation in the default path::

  start "" /wait /b Boundless-Desktop-2.0.0-x64.exe /S

Install for all users in default path::

  start "" /wait /b Boundless-Desktop-2.0.0-x64.exe /S /InstallationType=AllUsers

.. note::

   For `Allusers` installations, the :program:`Command prompt` needs to be opened
   using the :guilabel:`Run as administrator` option.

Install for all users in specific path::

  start "" /wait /b Boundless-Desktop-2.0.0-x64.exe /S /InstallationType=AllUsers /D=C:\path\to\install\prefix

.. note::

   Due to limitations of the NSIS installer, the /D option needs to be at the
   end of the command; Otherwise, it will try to use other options in the path
   name.
