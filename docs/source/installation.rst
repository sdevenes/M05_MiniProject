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