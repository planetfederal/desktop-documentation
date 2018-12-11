.. _components.pgadmin:

pgAdmin
=======

About
-----

`pgAdmin` is a feature rich Open Source administration and development platform
for `PostgreSQL <https://www.postgresql.org/>`_, the most advanced Open Source
database in the world, which includes, among others, the `Postgis
<http://postgis.org/>`_ spatial extention.

`pgAdmin` is developed by a community of PostgreSQL experts around the world and
is available in more than a dozen languages. It is Free Software released under
the PostgreSQL License.

`pgAdmin` is aimed to answer the needs of all users, from writing simple SQL
queries to developing complex databases. The graphical interface supports all
PostgreSQL features and makes its administration easy. The application includes,
among other things: syntax highlighting SQL editor, a server-side code editor,
an SQL/batch/shell job scheduling agent, and much more. See more about it in the
:pgadmin:`official website <>`.

Quick start guide
-----------------

.. note::

    To execute this Quick Start Guide you will need a running instance of
    :program:`PostgreSQL` database with the spatial extension :program:`PostGIS`
    installed, please ask your system administrator for the connection
    parameters. For further information about :program:`PostgreSQL` or
    :program:`PostGIS` see :ref:`pgadmin.online_resources`.

The following quick start guide will introduce you to :program:`pgAdmin` basics.
It will show how to access to a spatially enabled database and run some simple
queries on its tables.

#. Download the data for this tutorial :download:`here
   <data/events_data_sample.zip>` and unzip it anywhere you think it's
   convenient.

#. Import the geodata from the shapefile into the database, if you have
   :command:`shp2pgsql` command line utility at hand you can import the data with::

     shp2pgsql events.shp | psql -U postgres pg_test

   If you don't have this command available you can still use :program:`QGIS`
   *db manager* to import you data into the database.

#. Open :program:`pgAdmin4` using any of the available shortcuts in your
computer.

   By default, :program:`pgAdmin4` will show the following window on opening:

   .. figure:: img/pgadmin_first_open.png

#. On the :guilabel:`Browser` panel, right-click on the :guilabel:`Servers`,
   and navigate to :menuselection:`Create --> Server...` to create a new
   database connection.

#. In the :guilabel:`Create - Server` dialog, enter the connection
   :guilabel:`Name`. Click the :guilabel:`Connection` tab,
   enter the connection parameters in the dialog and click :guilabel:`Save`.. figure:: img/

   A database connection is usually identified by:

   * host
   * port
   * username
   * password

   .. figure:: img/pgadmin_register_new_server.png

#. Click on the newly added server to open its objects tree and select the
   `events` table or any other table you want to query. Then, click the
   :guilabel:`Properties` tab.

   .. figure:: img/pgadmin_schema_tree.png

#. Perform operations on selected tables with :kbd:`Right-Click`

   .. figure:: img/pgadmin_right_click_table_operations.png

#. Preview data with :menuselection:`View Data --> View First 100 Rows`

   .. figure:: img/pgadmin_right_click_table_preview.png

   .. figure:: img/pgadmin_right_click_table_preview_result.png

#. In the menus, click :menuselection:`Tools --> Query`

#. In the query editor, type the following query::

       SELECT name, St_AsText( geom ) FROM events;

#. Then, click the :guilabel:`Execute/Refresh` button or press :kbd:`F5`

   .. figure:: img/pgadmin_execute_sql_results.png

   .. _pgadmin.online_resources:

Online resources
----------------

* :pgadmin:`Official Site: <>`
* :pgadmin:`Documentation <docs/pgadmin4/dev/#>`
* :program:`PostgreSQL <https://www.postgresql.org>`_
* :program:`PostGIS <http://postgis.net>`_
