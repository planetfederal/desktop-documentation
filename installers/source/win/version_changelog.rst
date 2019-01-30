**Version 2.0.0**

**Added**

The Boundless Desktop 2.0.0 release contains numerous component upgrades, new
functionality, and bug fixes. The highlights include:

* QGIS updated to 3.4.4
* GDAL/OGR updated to 2.4.0
* GRASS updated to 7.4.4
* Python updated to 3.7.1
* Qt Designer updated to 5.9.6

.. New installers both for Mac and Windows, which will allow partial package updates

QGIS 3.4 receives a major update from its LTR predecessor (2.18). QGIS 3.4 is
based on Qt 5 and Python 3 and adds many new features. Some examples are:

* Support for user profiles
* Unified data source manager dialog
* Improved support for Geopackage, which is now the default format on
  processing tools
* Multiple map views
* 3D surface and layer rendering, with animations
* Support for running processes as background tasks, allowing the user to
  keep using QGIS interface while the job is running
* Improved layout creation including reports
* Master password integration with win, mac and linux keychains
* Locator bar for quick access to tools and commands
* Improved consistency to the user interface
* Tens of new expression functions, including array functions
* Improved expressions editor with auto-completion and error highlighting
* New units for symbols and layouts, including pixels and inches
* Point cluster renderer
* Easy styling of discrete rasters
* Note tool is replaced by a much improved and functional vertex tool
* Auxiliary storage support, which allows, for example, saving custom label
  positions on the project)
* Several Improvements to the feature forms and widgets, including drill-down
  (cascading) forms (aka domains and sub-domains in forms)
* Several new processing algorithms, and performance improvements to existing ones.
* Improved processing modeler window
* New Geonode data provider
* Opening of vector and raster stored on HTTP(S), FTP, or cloud services
* Save and load QGIS projects in PostgreSQL database
* Support for mesh layers (GRIB, XMDF, Netcdf)
* Automatically set default style for layers from ArcGIS Feature Server layers
* OpenCL based acceleration
* Polished browser panel interface and experience
* GPS tracking improvements
* Processing “Edit in place” mode
* Store processing models inside project
* OAuth2 authentication method plugin
* ESRI Token Authentication support
* Support for encrypted zips in the Plugin Manager¶

For a full list of new features check the visual changelogs for versions 3.0, 3.2 and 3.4 https://www.qgis.org/en/site/forusers/visualchangelogs.html

**Removed**

* Standalone QGIS browser application has been deprecated
* Connect plugin will not be shipped in this release
* Boundless OAuth2 and Master Password plugins, has its functionality was integrated into
  QGIS 3 core
* Orfeo toolbox processing provider removed temporarily
* PgAdmin 4 was temporarily removed from installer

**Fixed**

Community fixes:

* Browser panel restore causes unwanted WMS connections when expanded
* Invalid fields error when using auto-complete in Layer properties Edit widget:Value Relation
* Date edit widget only shows current date whatever the real data is underneath
* QGIS crashes when opening project file with nonexisting NTV2 grid file location
* Date widget: cosmetic issue with NULL values
* Date widget: current date can't be picked
* Processing/geoprocessing operations failing in 2.18 with memory layers
* Processing script editor: incorrect read of degree symbol
* Spatial Bookmark Panel: precision gets trimmed
* DXF Export generates many numbered layers (1 layer for each feature)
* Reference point property of the composer item is not working properly
* GDAL algorithms ignore feature filter
* Clipping of raster with GDAL may hang QGIS
* Print composer:  Changing "orientation" in Page Setup has no effect
* File picker window slow
* Tooltip type changed automatically
* The QGIS intersection tool yields incomplete results
* Names of Print layout items not reused
* Rephrase Draw map canvas items
* Font size in Form view does not take into account default font size settings
* Scalebar addition when dealing with multiple map frames
* Let user set histograms in mm
* While exporting composer, WMS warning appears only if WMS layer is visible in the map canvas
* Processing gdal tools do not work if Windows username contain non ascii chars.
* Processing Toolbox Doesn't Pick Up New Database Connections
* When advanced (CAD) digitizing is ON, Overview panel cannot be resized
* Composer map doesn't rotate when angle is set using "data define override" option
* Coverage layer not checked before parsing filename expression in atlas generation
* Style Manager filter ignores currently selected group
* Processing:runalg locks input file
* Configure Shortcuts problem on Mac
* Python bindings for QgsDxfExport.addLayers causes crash
* Adding geojson via add vector layer causes strange behaviour
* Add PostGIS layers is too slow on connecting to a database
* PostGIS views not handled correctly
* Incorrect evaluation of Rule-Base features
* resolution problem with the rule rendering dialog window
* Grey  "Export symbology" option in the "save vector layer as ..."  CSV
* The toggle editing pencil becomes orange without changing values of the layer
* Progress bar and setText not working on a mac with user script
* Project loads layers not seen in legend
* Right to Left formating in Map Composer
* No vertical scrollbar for tall forms and bad display when maximized
* SRS 102003 not recognized
* Map rotation in print composer: make behaviour more uniform
* Wrong rendering of line pattern fill (custom dash pattern)
* Using PostGIS over a slow connection unfeasible: unnecessary loading of data?
* Save dialogue for Geoprocessing outputs is inconsistent
* Names of colour ramp categories
* Do not list non-geometric layers in layer order
* Postgis: commit errors leads to loosing data
* Help in Save raster as... help dialog
* Results from field calculator wrong format
* Browser not accessing Windows network
* Toolbox misaligned
* SAGA vector produced without .prj if the input layer does not have it
* Arrow in composer - "bounding box" corners

For a full list of fixed issues see https://issues.qgis.org/projects/qgis/issues?query_id=176

**Version 1.1.1**

**Added**

* QGIS updated to 2.18.14
* GDAL/OGR updated to 2.2.2
* GRASS updated to 7.2.2
* PgAdmin 4 updated to v2.0
* New offline Desktop documentation included in installer
* New OGR plugin for MSSQL geospatial databases
* SAGA GIS updated to LTS version
* System certificate method supports PostgreSQL connections

**Fixed**

Sponsored by Boundless:

* Fixed all authentication plugin in multithreaded connections
* Lines To Polygons, Polygonize and Refactor Fields change all attributes to string 255
* Segmentation fault with 'Create raster icons' on and loading a WMS
* Windows: Cannot use anymore d&d in DB Manager to import a layer from Spatialite/GPKG into PostGIS
* WMTS rendering problems in 2.18 and Master
* PostGIS issue when using 'Merge selected features' tool (Geometry type does not match column type)
* "Paste features as..." always creates vector layer/scratch layer that can only handle just single part features
* Crash when no value is entered in min or max fields in Singleband pseudocolor in styling dock
* Processing: "import into PostGIS" parameter "table to import to" is mandatory on 2.18.10 and should be optional
* After downloading a R script this is not immediately added to the Processing tree and QGIS restart is needed
* SAGA raster calculator not working in QGIS 2.18.10
* Attribute table: crash removing features when cell is in editing mode
* Processing is broken on QGIS 2.18.2 for macOS from KyngChaos
* Attribute table: rows are switching when adding attributes
* Rows of the attribute table seem to be duplicated when saving edits in a shapefile
* Security fix on Windows that securely remove certs used during PKI connections
* Frequent errors in DB Manager: "pyqtSignal must be bound to a QObject, not 'PGVectorTable'"
* 2.18: Move Selection to Top not working in attribute table
* Support for TLS v1.2 in custom OpenSSL setup

Community fixes:

* Processing: GRASS64 does not work in both latest 2.14 and 2.18
* Processing: GRASS7 nviz does not work
* Rasterize and Rasterize Over algorithms not opening
* Images do not show anymore in GRASS docs in Processing
* Python error in Processing/QGIS clip"
* QGIS Print Composer: Overview, selection of the map frame is not possible
* SAGA Mosaic raster layers don't run in QGIS 2.18.10
* Unicode character in query in db_manager makes appear a never-ending hourglass
* Saving point vector as CSV in 2.18.10 X/Y values are not exported anymore
* Since 2.18.10 "save as GPX" not recognising GPX_USE_EXTENSIONS setting
* GRASS plugin/Processing tools not loading QGIS 2.18.10 installer (both standalone and osgeo4w)
* regression: adding a multi-part feature to a shapefile dataset fails
* python error in Processing result viewer
* Processing scripts: cannot concatenate 'str' and 'NoneType' objects
* Adding PostGIS layers from the browser or DB-Manager crashes QGIS (mini-dump)
* No "Recently used expressions" in expression editor
* WFS crashing QGIS on 2.18.8
* Segmentation fault when importing CSV file with coordinates
* No fields display in expression editor under Fields an values (QGIS 2.18.8)
* Extremely slower time to open attribute table in 2.18.7 compared to 2.14.14
* Edit Widget Properties dialog shrinks fields while resizing
* Inserting data on version views not working in 2.18 (OK in 2.14)
* Locked raster layers do not refresh in Composer
* Creating a join freezes QGIS 2.18/master if target layer attributes table is open
* QGIS 2.18.2 (KyngChaos build) crashes after latest Mac OS X update to 10.12.4
* Broken io_gdal raster import in SAGA LTR package shipped with OSGeo4W
* Processing (on Windows): external SAGA does not work anymore
* "hidden" edit widget does not work on QGIS 2.18.5 (and master)
* copy/paste features does not include attributes
* Spatial Bookmark Panel: crash on export
* Quick calculation bar causes QGIS crash when updating fields with aliases
* (macOS) layers imported into a Spatialite Database with DB manager are not recognized as spatial tables
* QGIS 2.18.4 saves always with absolute paths
* Escaping out of Dialog causes QGIS to crash
* "Join by attributes" generates incomplete results
* Processing merge vector layers returns incomplete result
* QGIS crashes with GEOS Exception: IllegalArgumentException: Invalid number of points in LinearRing found 3 - must be 0 or >= 4
* Layer "Scale-dependent visibility" doesn't work anymore since 2.16
* Warp tool requires CRS of extent when no extent set

For a full list of fixed issues see https://issues.qgis.org/projects/qgis/issues?query_id=141

**Quality Assurance**

* In-house testing suite, covering Windows 10 and Windows 7 with latest updates

**Version 1.1.0**

**Added**

* QGIS updated to 2.18.10
* QgsSettings (a QGIS 3.0 feature) backported to 2.18 Boundless release
  branch
* New qgis_global_setting.ini customization file, with Boundless plugins and
  plugin repo enabled by default
* New init_scripts support for running customization scripts on QGIS launch
* pgAdmin3 replaced by pgAdmin4 (code-signed)
* New Master Password Helper (C++ core plugin)
* New OAuth2 authentication method plugin
* New Reporting Tool plugin and createreport command line script
* GDAL/OGR updated to 2.2.0
* Updated license files for included third-party software
* Added custom OpenSSL and QtNetwork builds, and OpenSSL configuration for
  CAPI backend engine, to support Keystore plugin
* New 'Boundless Desktop Documentation' URL link in Start menu and shortcuts on
  user's desktop
* New winhttp-head.exe sub.domain.tld utility for auto-loading missing CAs of
  endpoints in Win cert store (overcomes Qt4 flaw)
* OpenGeo QGIS logo dropped in favor of the official QGIS 2.x logo

**Fixed**

* SAGA "slope, aspect, curvature" returns wrong output
* Crash when zooming a reprojected PostGIS layer
* Degradation of rendering performances in MSSQL provider
* Encoding problems with Processing toolbox
* Python filter expression don't work on "value relation"
* DB Manager: previewing layers in Virtual layers section remove them from the Layers panel
* Intersection causes crash with specific inputs
* Crashes when switching to some UTM CRSs with certain data
* Errors while trying run IPython and Jupyter consoles in Windows.

**Quality Assurance**

* In-house testing suite, covering Windows 10 and Windows 7 with latest updates
