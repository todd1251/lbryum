===========================================
lbryum - lbrycrd client |travis| |coverage|
===========================================

.. _introduction:


Lightweight lbrycrd client library in Python; based on the the Electrum bitcoin client.


Installation
============

To install lbryum, run the following from this directory (use of a virtualenv is recommended):

.. code-block:: shell

    pip install -r requirements.txt
    pip install -e .


Usage
=====

To run start the lbryum daemon, run:

.. code-block:: shell

    lbryum daemon start
  
  
To stop the lbryum daemon, run:

.. code-block:: shell

    lbryum daemon stop
  
  
For a list of lbryum commands, run:

.. code-block:: shell

    lbryum help


.. |travis| image:: https://travis-ci.org/lbryio/lbryum.svg?branch=master
   :target: https://travis-ci.org/lbryio/lbryum
   :alt: Build

.. |coverage| image:: https://codecov.io/gh/lbryio/lbryum/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lbryio/lbryum
   :alt: Test Coverage
