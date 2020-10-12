===========
 User Guide
===========

This guide explains how to use this package and obtain results published in our
paper.  Results can be re-generated automatically by executing the following
commands:

.. code-block:: sh

   $ rr-data 'datapath/'
   $ rr-paper 'datapath/csh101/csh101.ann.features.csv' 'output/'


For your reference, the paper tables are repeated below, so you can check the
reproducibility of our solution.

Working hypothesis
------------------

It is possible to perform human activity recognition using data from continuous ambient sensors

Dataset
-------

The dataset that was used for this project is the UCI ML Repository's Human Activity Recognition from Continuous Ambient Sensor Data Data Set [dua2019]_ [cook2012]_.
It represents ambient data collected in 30 homes with volunteer residents.
Data are collected continuously while residents perform their normal routines.
It contains 36 features measured plus one output for the classification label of the activity, for
a total of 13956534 entries.

Machine learning
----------------

Random forest classifiers from scikit-learn were used to obtains the results presented in this project.


Results for Protocol `proto1`
-----------------------------

Impact of number of trees with maximum depth of 15
==================================================

1 tree in forest

.. raw:: html
   :file: img/table_1.html

5 trees in forest

.. raw:: html
   :file: img/table_2.html

10 treea in forest

.. raw:: html
   :file: img/table_3.html


Impact of tree depth with 10 trees per forest
=============================================

Depth of 5

.. raw:: html
   :file: img/table_7.html

Depth of 10

.. raw:: html
   :file: img/table_8.html

Depth of 15

.. raw:: html
   :file: img/table_9.html


Results for Protocol `proto2`
-----------------------------

Impact of number of trees with maximum depth of 15
==================================================

1 tree in forest

.. raw:: html
   :file: img/table_4.html

5 trees in forest

.. raw:: html
   :file: img/table_5.html

10 treea in forest

.. raw:: html
   :file: img/table_6.html


Impact of tree depth with 10 trees per forest
=============================================

Depth of 5

.. raw:: html
   :file: img/table_10.html

Depth of 10

.. raw:: html
   :file: img/table_11.html

Depth of 15

.. raw:: html
   :file: img/table_12.html


.. [dua2019] Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
.. [cook2012] D. Cook. Learning setting-generalized activity models for smart spaces. IEEE Intelligent Systems, 27(1):32-38, 2012.
