Chapter 10 - Example of a Service
=================================

Structure
---------
At a glance:

    - ``libs``: With the Python packages (dependencies) needed by the service.
    - ``statusweb``: The service itself. Imports its dependencies from ``libs```.

The service itself is placed in the ``statusweb`` directory.
The ``./libs`` directory contains Python packages that dependencies. Typically, (unless you follow a mono-repo
structure, which is also a possibility), they would belog in a separate repository, but this directory should make it
clear that they're other packages, tailor-made for internal use.


Service
-------
Case: A delivery platform. Check the status of each delivery order by an HTTP GET.

    Service: Delivery Status
    Persistency: A RDBMS
    Response Format: JSON


Running the Service
-------------------
In order to test the service locally, you'd need to set the following environment variable: ``DBPASSWORD``, and then
build the images::

   make build

Note: this Makefile target runs the ``docker`` command line interface. Depending on your configuration you might need to
run it with ``sudo`` if you get permission errors.

Run the service with::

   make run

Note: If you still need to run the previous command with ``sudo``, pass the ``-E`` flag, so that the environment
variables are passed along.


Assuming data has been loaded, this can be tested with any HTTP client::

    $ curl http://localhost:5000/status/1
    {"id":1,"status":"dispatched","msg":"Order was dispatched on 2018-08-01T22:25:12+00:00"}

    $ curl http://localhost:5000/status/99
    Error: 99 was not found
