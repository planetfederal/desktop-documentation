# Installers files builder

This sphinx project aims to create files that should be included with the Boundless Destop installers. It makes possible to create files for different platforms and components from the same sources.

Currently it produces only one file, but more can be added:

 * README.txt

## Update sources

When a new installer is created one should make sure that all relevant information in sources is updated:

* Boundless Desktop Version:

  sources/conf.py`

* Supported and Additional Components, and their versions for each platform:

  sources/<platform>/supported_components.rst
  sources/<platform>/additional_components.rst

* Install and uninstall procedures for each platform:

  sources/<platform>/install_uninstall.rst

## Build sources

To build the files one have to specify the aimed platform in make command:

  `make text SPHINXOPTS="-t <platform>"`

Current platforms available are `win` and `osx`
