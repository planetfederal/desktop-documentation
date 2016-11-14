# Installers files builder

This sphinx project aims to create files that should be included with the Boundless Destop installers. It makes possible to create files for different platforms and components from the same sources.

Currently it produces only one file, but more can be added:

 * README.txt

## Update sources

When a new installer is created one should make sure that all relevant information in sources is updated:

* Boundless Desktop Version:

        source/conf.py

* Supported and Additional Components, and their versions for each platform:

        source/<platform>/supported_components.rst
        source/<platform>/additional_components.rst

* Install and uninstall procedures for each platform:

        source/<platform>/install_uninstall.rst

## Build sources

Building takes a parameter for a supported platform: `win` or `osx`

To build the files one have to specify the aimed platform in make command:

        make text SPHINXOPTS="-t <platform>"

To build RTF files, you need [pandoc][pan] and [sphinxcontrib-restbuilder][srb]
installed:

[pan]: https://github.com/jgm/pandoc/releases
[srb]: https://pythonhosted.org/sphinxcontrib-restbuilder/

* Combine rst sources into one README.rst

        rm -Rf build && \
        sphinx-build -b rst -t <platform> source build/rst

* Build README.rtf

        pushd build/rst &&
        pandoc -s -f rst -t rtf -o README.rtf README.rst && \
        popd
        
* Optionally open the README on macOS (defaults to TextEdit.app)

        open build/rst/README.rtf
