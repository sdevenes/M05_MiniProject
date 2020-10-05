import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../scripts/")

import download_data
import zipfile
import requests

import algorithm
import analysis
import numpy as np

import database

import nose.tools

# Get the path of this file to easily build relative path
base_path = os.path.dirname(os.path.realpath(__file__))


def test_unzip_file_not_a_zip():
    path_to_zip_file = base_path + "/inputs/not_a_zip.txt"  # not a zip
    directory_to_extract_to = base_path  # extract here
    nose.tools.assert_raises(zipfile.BadZipFile, download_data.unzip_file, path_to_zip_file, directory_to_extract_to)


def test_unzip_file_invalid_zip_path():
    path_to_zip_file = base_path + "/simpleZip.zip"  # Invalid path
    directory_to_extract_to = base_path  # extract here
    nose.tools.assert_raises(FileNotFoundError, download_data.unzip_file, path_to_zip_file, directory_to_extract_to)


def test_unzip_file():
    path_to_zip_file = base_path + "/inputs/simpleZip.zip"
    directory_to_extract_to = base_path + "/output/"  # extract here
    download_data.unzip_file(path_to_zip_file, directory_to_extract_to)
    nose.tools.ok_(os.path.isfile(base_path + "/output/f1.txt"), msg="SimpleZip not correctly unzipped")


def test_download_url_invalid_url():
    url = "https://invalid_url.zip"
    save_path = base_path + "/output/invalid_dl.zip"
    nose.tools.assert_raises(requests.exceptions.ConnectionError, download_data.download_url, url, save_path)


def test_download_url():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00405/Postures.zip"  # Smaller zip to test
    save_path = base_path + "/output/test_dl.zip"
    download_data.download_url(url, save_path)
    nose.tools.ok_(os.path.isfile(save_path), msg="Dataset not correctly downloaded")


def test_make_labels():
    X = [np.array([0, 1, 0]), np.array([2, 3]), np.array([7, 4, 6, 9])]
    labels = algorithm.make_labels(X)
    ref = np.array([0, 0, 0, 1, 1, 2, 2, 2, 2])
    nose.tools.ok_((labels == ref).all(), msg="{} != {}".format(labels, ref))


def test_get_confusion_matrix():
    prediction = [1, 2, 3, 1, 2, 2, 3]
    true_val = [1, 2, 3, 1, 2, 3, 2]
    cm = analysis.get_confusion_matrix(prediction, true_val)
    ref = np.array([[2, 0, 0], [0, 2, 1], [0, 1, 1]])
    nose.tools.ok_((cm == ref).all(), msg="{} != {}".format(cm, ref))


def test_load():
    default_data_len = 321428
    num_columns = len(database.VARIABLES)
    expected_x_shape = (default_data_len, num_columns)
    expected_y_shape = (default_data_len,)
    x, y = database.load('../data/csh101/csh101.ann.features.csv')
    nose.tools.ok_(x.shape == expected_x_shape,
                   msg='x.shape != {}'.format(expected_x_shape))
    nose.tools.ok_(y.shape == expected_y_shape,
                   msg='y.shape != {}'.format(expected_y_shape))


def test_split_data_test():
    default_data_len = 321428
    num_columns = len(database.VARIABLES)
    protocol = 'proto1'
    subset = 'test'
    expected_test_len = np.ceil(database.PROTOCOLS[protocol][subset] * default_data_len)
    x, y = database.load('../data/csh101/csh101.ann.features.csv')
    x_test, y_test = database.split_data(x, y, subset, database.PROTOCOLS[protocol])
    nose.tools.ok_(x_test.shape[0] == expected_test_len,
                   msg='x_test.shape[0] != {}'.format(expected_test_len))
    nose.tools.ok_(y_test.shape[0] == expected_test_len,
                   msg='y_test.shape[0] != {}'.format(expected_test_len))


def test_split_data_train():
    default_data_len = 321428
    protocol = 'proto1'
    subset = 'train'
    expected_train_len = np.floor(database.PROTOCOLS[protocol][subset] * default_data_len)
    x, y = database.load('../data/csh101/csh101.ann.features.csv')
    x_train, y_train = database.split_data(x, y, subset, database.PROTOCOLS[protocol])
    nose.tools.ok_(x_train.shape[0] == expected_train_len,
                   msg='x_test.shape[0] != {}'.format(expected_train_len))
    nose.tools.ok_(y_train.shape[0] == expected_train_len,
                   msg='y_test.shape[0] != {}'.format(expected_train_len))


def test_get_default():
    protocol = 'proto1'
    subset = 'test'
    default_data_len = 321428
    num_columns = len(database.VARIABLES)
    expected_len = np.ceil(database.PROTOCOLS[protocol][subset] * default_data_len)
    expected_x_shape = (expected_len, num_columns)
    expected_y_shape = (expected_len,)
    x, y = database.get(protocol, subset, filepath='../data/csh101/csh101.ann.features.csv')
    nose.tools.ok_(x.shape == expected_x_shape,
                   msg='x.shape != {}'.format(expected_x_shape))
    nose.tools.ok_(y.shape == expected_y_shape,
                   msg='y.shape != {}'.format(expected_y_shape))


def test_get_limited_variables():
    protocol = 'proto1'
    subset = 'test'
    variables = ['lastSensorEventHours', 'complexity']
    variables_indices = [0, 10]
    x_full, y_full = database.get(protocol, subset, filepath='../data/csh101/csh101.ann.features.csv')
    x, y = database.get(protocol, subset, variables=variables, filepath='../data/csh101/csh101.ann.features.csv')
    nose.tools.ok_(np.array_equal(x, x_full[:, variables_indices]),
                   msg="x != x_full[:, ('lastSensorEventHours', 'complexity')]")


def test_get_limited_classes():
    protocol = 'proto1'
    subset = 'test'
    classes = ['Other_Activity', 'Work_At_Table']
    other_classes = database.CLASSES[1:-1]
    x, y = database.get(protocol, subset, classes=classes, filepath='../data/csh101/csh101.ann.features.csv')
    nose.tools.ok_(not np.isin(y, other_classes).any(),
                   msg='y contains other classes than: {}'.format(classes))
    nose.tools.ok_(x.shape[0] == y.shape[0],
                   msg='x.shape[0] != y.shape[0]')
