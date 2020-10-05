------------
Installation
------------

This package depends on the python libraries listed in requirements.txt to run properly. 
Please install a modern version of these packages before trying to run the code examples.
Or create directly a conda virtual environment using the conda.yml file as in the following
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

The project documentation is generated with sphinx and can simply be build using the command:

.. code:: sh

   $ make doc

The python API documentation will be automatically generated for all the python modules located
in `scripts <https://github.com/sdevenes/M05_MiniProject/tree/feature/documentation/scripts>`_, as long as their docstring is completed.