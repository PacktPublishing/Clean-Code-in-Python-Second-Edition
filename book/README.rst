Clean Code in Python
--------------------

Requirements
============
The code in this repository assumes, Python 3.8+ is installed in the system, and that ``python3.8`` is available in the
current path.

    - Python 3.8+
    - GNU make and building tools for the dependencies (gcc, python3 dev files, etc.)

Setup
=====
To install the dependencies, run::

    make setup

This will create a new virtual environment, called ``.env`` and install the dependencies on it. From this point, you
need to activate the virtual environment to run the rest of the code examples. The environment is activated by running::

    source .env/bin/activate

Each chapter has its corresponding directory given by its number.

Inside each chapter directory, tests can be run by::

    make test

This requires the ``make`` application installed (in Unix environments).
In environments without access to the ``make`` command, the same code can be
tested by running the commands on the ``Makefile``::

    python -m doctest *.py
    python -m unittest *.py


Chapters Index
==============

* Chapter 01; Introduction, Code Formatting, and Tools
* Chapter 02: Pythonic Code
* Chapter 03: Traits of Clean Code
* Chapter 04: The SOLID Principles
* Chapter 05: Decorators
* Chapter 06: Getting More out of our Objects with Descriptors
* Chapter 07: Using Generators
* Chapter 08: Unit Testing and Refactoring
* Chapter 09: Common Design Patterns
* Chapter 10: Clean Architecture
