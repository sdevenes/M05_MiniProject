import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../scripts/")

import algorithm
import database
import analysis
import download_data
import zipfile
import requests
import numpy as np

import nose.tools

# Get the path of this file to easily build relative path
base_path = os.path.dirname(os.path.realpath(__file__))

def test_unzip_file_not_a_zip():
    path_to_zip_file = base_path + "/inputs/not_a_zip.txt" # not a zip
    directory_to_extract_to = base_path # extract here
    nose.tools.assert_raises(zipfile.BadZipFile, download_data.unzip_file, path_to_zip_file, directory_to_extract_to)

def test_unzip_file_invalid_zip_path():
    path_to_zip_file = base_path + "/simpleZip.zip" # Invalid path
    directory_to_extract_to = base_path # extract here
    nose.tools.assert_raises(FileNotFoundError, download_data.unzip_file, path_to_zip_file, directory_to_extract_to)

def test_unzip_file():
    path_to_zip_file = base_path + "/inputs/simpleZip.zip"
    directory_to_extract_to = base_path + "/output/" # extract here
    download_data.unzip_file(path_to_zip_file, directory_to_extract_to)
    nose.tools.ok_(os.path.isfile(base_path + "/output/f1.txt"), msg="SimpleZip not correctly unzipped")

def test_download_url_invalid_url():
    url = "https://invalid_url.zip"
    save_path = base_path + "/output/invalid_dl.zip"
    nose.tools.assert_raises(requests.exceptions.ConnectionError, download_data.download_url, url, save_path)

def test_download_url():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00405/Postures.zip" # Smaller zip to test
    save_path = base_path + "/output/test_dl.zip"
    download_data.download_url(url, save_path)
    nose.tools.ok_(os.path.isfile(save_path), msg="Dataset not correctly downloaded")
