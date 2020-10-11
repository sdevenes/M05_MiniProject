------------
Installation
------------

This package depends on the python libraries listed in `requirements.txt <https://github.com/sdevenes/M05_MiniProject/blob/master/requirements.txt>`_  to run properly. 
Please install a modern version of these packages before trying to run the code examples.
Or create directly a conda virtual environment using the requirements.txt file as in the following
exemple.

To download a copy of this package, clone it from its repository in GitHub:

.. code:: sh

   $ git clone https://github.com/sdevenes/M05_MiniProject.git project
   $ cd project
   $ conda create -q -n project python=3.8 -c plotly --file requirements.txt
   $ conda activate project

   (project) $ #you are ready to run baselines!

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
