**Version 1.1.1**

**Added**

* QGIS updated to 2.18.14
* Activated QGIS Oracle data provider and Qt spatial database driver
* Activated QGIS's QSpatialite (Qt) database driver
* GDAL/OGR updated to 2.2.2
* New OGR plugin for OGDI format
* New OGR plugin for Oracle geospatial databases
* New GDAL/OGR plugin for PDF format
* New MySQL Qt database driver
* New Oracle (non-spatial) Qt database driver
* GRASS updated to 7.2.2
* Python updated to 2.7.14
* PgAdmin 4 updated to v2.0
* New offline Desktop documentation included in installer

**Fixed**

Sponsored by Boundless:

* Fixed all authentication plugin in multithreaded connections
* Fixed missing openssl command line tool on PATH
* Fixed NetCDF functionality (missing linkage to GCC libraries)
* Fixed GDAL/OGR geospatial PDF reading (now uses Poppler instead of PoDoFo libraries)
* Lines To Polygons, Polygonize and Refactor Fields change all attributes to string 255
* Segmentation fault with 'Create raster icons' on and loading a WMS
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

* In-house testing suite, covering Mac OS X 10.10 and macOS 10.12 and 10.13 with latest updates

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
* New 'Boundless Documentation' URL link in Start menu and shortcuts on
  user's desktop
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

* In-house testing suite, covering Mac OS X 10.9 and macOS 10.12 with latest updates
