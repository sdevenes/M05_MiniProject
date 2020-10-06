.. image:: https://travis-ci.org/sdevenes/M05_MiniProject.svg?branch=master
   :target: https://travis-ci.org/github/sdevenes/M05_MiniProject
.. image:: https://coveralls.io/repos/github/sdevenes/M05_MiniProject/badge.svg?branch=master
   :target: https://coveralls.io/github/sdevenes/M05_MiniProject?branch=master
.. image:: https://img.shields.io/badge/docs-latest-orange.svg
   :target: https://sdevenes.github.io/M05_MiniProject/index.html
.. image:: https://img.shields.io/badge/github-project-0000c0.svg
   :target: https://github.com/sdevenes/M05_MiniProject
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

===============================================================
 Human Activity Recognition from Continuous Ambient Sensor Data
===============================================================

This mini project was developed during the M05 course "reproducibility and open science"
taught by Idiap as part of the AI master 2020-2021.

Working hypothesis
------------------

It is possible to perform human activity recognition using data from continuous ambient sensors

Dataset
-------

The dataset that was used for this project is the following: https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+from+Continuous+Ambient+Sensor+Data.
It represents ambient data collected in 30 homes with volunteer residents.
Data are collected continuously while residents perform their normal routines.
It contains 36 features measured plus one output for the classification label of the activity, for
a total of 13956534 entries.

Machine learning
----------------

Random forest classifiers from scikit-learn were used to obtains the results presented in this project.
