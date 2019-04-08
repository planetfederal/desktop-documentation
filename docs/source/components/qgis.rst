.. _components.qgis:

QGIS
====

About
-----

QGIS is the centerpiece of the Boundless Desktop package installation. The
well-known leading Open Source GIS for desktop, QGIS, is a cross-platform
desktop application for viewing, editing, and analyzing geospatial data from a
variety of (proprietary and open) vector, raster, and database formats.

QGIS’s development is steered by the :qgis:`QGIS Project <>`, which works
with hundreds of volunteers and companies (including Boundless) from all over
the world, that helps enhance and maintain QGIS.

For convenience, outside the supported scope of Boundless Desktop, the following
processing providers are available for QGIS’s Processing framework:

* SAGA 2.3 by `<http://www.saga-gis.org>`_
* GRASS 7.4 by `<http://grass.osgeo.org>`_

.. * Orfeo Toolbox 5.0 by `<https://www.orfeo-toolbox.org>`_

.. _components.qgis.quickstart:

Quickstart guide
----------------

This brief overview of QGIS will focus on QGIS's graphical user interface (GUI)
and some of the most common operations like loading data, managing layers and
printing a map. For more detailed information on QGIS usage see the tutorials
in our learning center and consult :qgis_docs:`QGIS's official documentation <2.18>`.

We will use the `Natural Earth <http://www.naturalearthdata.com>`_ data in
the examples that follow. Please, download the `Natural Earth
Quickstart Kit
<http://naciscdn.org/naturalearth/packages/Natural_Earth_quick_start.zip>`_ and
unzip it to any folder that you find convenient to access.

QGIS user interface
~~~~~~~~~~~~~~~~~~~

#. Use any of the available QGIS's shortcuts on your computer to open QGIS.

   By default, the QGIS interface should resemble the one presented in the next figure.

   .. figure:: img/qgis_GUI.png

      QGIS Graphical User Interface (GUI)

   As a simple overview of the default GUI we have:

   * On the top of the screen, you will find the menu bar (1). The menu bar
     provides access to various QGIS features using a standard hierarchical
     menu.

   * The main toolbar area (2) is below the menu bar. Toolbars provide quick
     access to many functions present in the menus, plus additional tools for
     interacting with the map. Hold your mouse over the item for a short
     description of the tool's purpose. Toolbars can be moved by dragging and
     dropping them elsewhere and even hidden using :menuselection:`View -->
     Toolbars`.

   * On the left side of the interface, there are two panels by default: The :guilabel:`Browser Panel`
     (3), which is used to browse and load data, and the :guilabel:`Layers
     Panel` (4) which is used to toggle layers visibility, setting their
     relative order, accessing the layer's properties and much more. Panels
     can also be moved by drag and drop, or even hidden using :guilabel:`View
     --> Panels`.

   * To the right and middle of the screen, you find the map canvas (5) where
     all visible layers' geometries are displayed.

   * The status bar (6) s located at the bottom of the interface. It provides
     useful information and controls related to the current map scale, including the
     coordinates under the mouse pointer, the current Coordinate Reference System's
     EPSG code, and more.


Loading data
~~~~~~~~~~~~

Data can be loaded into QGIS using the :guilabel:`Browser Panel`, the
:guilabel:`Manage Layers Panel`, or by dragging and dropping from the
operating system file manager.

#. Using the :guilabel:`Browser Panel`, browse to the sample data location,
   more precisely into the ``Natural_Earth_quick_start\10m_physical`` folder.
   Double-click a folder's name or click the plus signs next to it to view
   its contents. Find the ``ne_10m_coastline.shp`` shapefile and drag and
   drop it from the browser to the map canvas. This will load the layer.

   .. figure:: img/qgis_dragndrop_from_browser.gif

      Loading a layer using the Browser Panel

   The layer should now be visible on the map canvas and :guilabel:`Layers Panel`
   list.

#. Let's open another file, this time using the :guilabel:`Data source manager`.
   Click the :guilabel:`Open Data source manager` button. In the  :guilabel:`Data
   source manager`, notice that there is a tab for each type of source. Select the
   :guilabel:`Raster` tab. Then, click the :guilabel:`...` button.

   .. figure:: img/qgis_open_data_source_manager.png


#. Navigate to the ``Natural_Earth_quick_start\50m_raster\NE1_50M_SR_W`` folder,
   select the ``NE1_50M_SR_W.tif`` file, and click :guilabel:`Open`.

   .. figure:: img/qgis_loading_raster.png

      Loading a layer using Add Raster Layer

#. Back in the :guilabel:`Data source manager`, click :guilabel:`Add`, followed
   by :guilabel:`Close`. The ``NE1_50M_SR_W.tif`` will show on the map canvas and
   :guilabel:`Layers` panel.

#. Finally, to load data into QGIS, you can drag and drop files from
   your operating system's file manager (Windows Explorer in Windows or
   Finder in Mac OS X) into QGIS Map canvas to load them. Load the
   :file:`ne_10m_admin_1_states_provinces.shp` from the :file:`10m_cultural` folder.

   .. figure:: img/qgis_dragndrop_from_explorer.gif

      Loading layer from the file manager (Windows)

#. Feel free to add any other data. Remember that you can load
   several files at once by holding the :kbd:`Ctrl` key during file selection,
   in any of the three methods described above.

Navigating the map canvas
~~~~~~~~~~~~~~~~~~~~~~~~~

Navigation in the map canvas can be done entirely with the mouse wheel.
In the absence of a mouse wheel, or for more precise control over the
map canvas, you can also use the :guilabel:`Map Navigation Toolbar` tools.

#. Position your mouse pointer anywhere on the map and spin your mouse wheel
   up to Zoom In. Spin the mouse wheel in the opposite direction to Zoom Out.

#. To pan, click and drag on the map canvas with the middle mouse button (wheel).

#. As stated above, the :guilabel:`Map Navigation Toolbar` provides more
   precise ways to navigate the map.

   Select the :guilabel:`Zoom In` tool and draw a rectangle around
   an area of interest using by clicking and dragging the left-mouse-button
   on the map canvas. Press the :guilabel:`Zoom Full` button to show the full
   extent of your data.

   .. figure:: img/qgis_zooming.gif

      Navigating the map canvas

#. Notice you can use the :guilabel:`Zoom last` and :guilabel:`Zoom last` to
   undo and redo changes to the map canvas extent

Managing Layers
~~~~~~~~~~~~~~~

We have been using the :guilabel:`Layers` panel already, but let's have a
more in-depth look into its potential.

#. Select a layer by clicking on its name on the layers list/legend. The
   layer becomes the `active layer`, meaning that many layer specific tools
   and actions will apply to that layer in particular. For example, select
   the ``ne_10_coastline`` layer and, in the :guilabel:`Map Navigation
   Toolbar`, click the :guilabel:`Zoom to Layer` button. This zooms the
   map canvas to the full extent of the layer.

   .. figure:: img/qgis_active_layer.png

      Layer active in the Layers Panel

#. You can change the order of the layers (and consequently their rendering
   order) by dragging them up and down in the :guilabel:`Layers`. Do this
   making sure to put the raster layer at the bottom, the polygons layer above
   it, and the line layer at the top.

   .. figure:: img/qgis_ordering_layers.gif

      Changing the order of the layers

#. You can change the visibility status of the layers by toggling the
   small checkbox next to its name. Give it a try and see the result on the map
   canvas. (Make sure to keep all layers visible in the end)

   .. figure:: img/qgis_change_layer_visibility.png

      Changing the layers' visibility

#. You can change how the layers are displayed on the map. Having
   the ``ne_10m_admin_1_states_provinces`` layer active, click the
   :guilabel:`Open the Layer Styling Panel` button.

   .. figure:: img/qgis_open_layer_styling_panel.png

      Opening the Layer Styling panel

#. The :guilabel:`Layer Styling` panel will open on the right side of the interface.
   Click the :guilabel:`Simple fill` in the symbols
   layers list, and in the Fill :guilabel:`Fill type` select ``No brush``. The
   change applies immediately on the map canvas.

   .. figure:: img/qgis_change_vector_layer_style.png

      Changing the layers' style in the Styling panel

#. Close the :guilabel:`Layer Styling` panel.

#. You may want to save your project at this time. Go to
   :menuselection:`Project --> Save` or hit :kbd:`Ctrl+S`. Choose the
   destination folder where your project will be saved, type in a descriptive
   name and click :guilabel:`Save`.

Exploring data's attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make proper use of the dataset, one should be familiar with its attributes.
Let's see how to retrieve the attributes of our layers.

#. Make sure the ``ne_10m_admin_1_states_provinces`` layer is still active
   and in the :guilabel:`Attributes toolbar` (if not visible, go to
   :menuselection:`View --> Toolbars`), select the :guilabel:`Identify tool`.
   Then, click the map over one of the geometries of the layer. The
   :guilabel:`Identify Results` Panel will show up, where you can see the
   feature's fields and respective values. (You may need to expand the panel a
   bit to see it all).

   .. figure:: img/qgis_identify.png

      Seeing layer's attributes using the identify tool in a feature

#. You can also see all the attributes of your layer in its attributes table.
   Having the ``ne_10m_admin_1_states_provinces`` layer selected, click the
   :guilabel:`Open Attributes table` in the :guilabel:`Attributes toolbar` (or
   right-click the layer's name in the :guilabel:`Layers Panel` and choose
   :guilabel:`Open Attribute Table` ). The layer's attribute table will show up.

   .. figure:: img/qgis_attribute_table.png

      Seeing layer's full attributes using the attribute table

#. In the attribute table, use the mouse wheel to scroll up and down
   the attributes, or the scroll bar to move horizontally.

#. Select one feature by clicking its id number at the left side of the
   feature's row of attributes. Then, use the :guilabel:`Zoom to Selected Rows`
   tool at the top of the attribute table to zoom the map to that particular
   layer.

   .. figure:: img/qgis_attribute_table_selected_row.png

      Selecting a row in the attribute table and zooming to its feature

#. Repeat step 4 selecting several rows by holding the :kbd:`Ctrl` key while
   clicking the id numbers. In the end, make sure to deselect all features
   using the :guilabel:`Deselect All` button in the attribute table.

Add simple labels
~~~~~~~~~~~~~~~~~

Now, that we already know our data attributes, let's use one as a label for our
geometries.

#. Open the :guilabel:`Layer Styling` panel again. Go to the Labels
   tab, and select ``Single labels``. Then, in the
   :guilabel:`Label with` option, select the ``abbrev`` field. The labels are
   added immediately.

   .. figure:: img/qgis_label_layer.png

      Layer's properties Label tab


Print a simple map
~~~~~~~~~~~~~~~~~~

Let's see how to print a simple map with the layers that we have
loaded. In QGIS, you can have as many print layouts as
you like, and you can manage them in the :guilabel:`Layout Manager`.

#. Once you are satisfied with the map's appearance, click the :guilabel:`New
   Print Layout` button in the :guilabel:`File toolbar`, type a
   representative name for the layout and click :guilabel:`Ok`.

   .. figure:: img/qgis_create_print_composer.png

      Creating a new layout and choosing a name

#. The layout composer will open showing an empty page. To add a map item, click
   the :guilabel:`Add Map` in the :guilabel:`Toolbox` toolbar and draw a
   rectangle covering most of the page by clicking and dragging over it. The
   map content should appear.

   .. figure:: img/qgis_add_map_item_composer.gif

      Adding a map item to the print composer page

#. You can adjust the map item position and size by clicking and dragging the
   corner and side handles.

#. You can also adjust the map extent using the :guilabel:`Move item content`
   tool. While this tool is selected, you can pan the map content clicking and
   dragging inside of it, and change its scale using the mouse wheel. More
   precise controls to set the map item position, size, scale, and extent can
   be found in the :guilabel:`Item properties tab/panel`.

   .. figure:: img/qgis_adjusting_map_item_composer.png

      Adjusting map item's scale and extent

#. Now, that we are satisfied with our very minimalist map, let's export it.
   In the :guilabel:`Layout` toolbar, click :guilabel:`Export to PDF`. Choose
   a location and name for your PDF file and click :guilabel:`Ok`.

More complex maps can be created by adding other items like legends,
labels, and images. Please see our learning center to learn how to work with
them. This `QGIS Map Gallery
<https://www.flickr.com/groups/qgis/pool/>`_ has more exampls of what can be
accomplished with the print composer.


Online resources
----------------

* :qgis:`Official Site <>`
* :qgis_docs:`Documentation <>`
* :qgis_plugins:`Official Plugins Repository <>`
