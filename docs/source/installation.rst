------------
Installation
------------

Use pip:

.. code:: sh

   $ pip install --extra-index-url https://test.pypi.org/simple rr_sdas


Building the documentation
--------------------------

The project documentation is generated with sphinx and can simply be build using these two commands:

.. code:: sh

   $ sphinx-apidoc -fMeT -o docs/source/api rr
   $ sphinx-build docs/source docs/build

The first command will generates restructured files containing API documentation for all the python 
modules located in `scripts <https://github.com/sdevenes/M05_MiniProject/tree/master/scripts>`_ 
based on their docstring. And the second command will packages all the rst files together and build this
html doc.
