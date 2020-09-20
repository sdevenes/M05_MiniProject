#!/usr/bin/env python
from tabulate import tabulate
import algorithm
import database
import analysis
import numpy as np


def base_test(protocol, variables, setname='csh101', nb_tree_per_forest=50, max_depth=10):
    # get train data
    train = database.get(protocol, 'train', database.CLASSES, variables, setname)
    # make and train model
    model = algorithm.Model(nb_tree_per_forest, max_depth)
    model.train(train)
    # get test data
    test = database.get(protocol, 'test', database.CLASSES, variables, setname)
    test_labels = algorithm.make_labels(test).astype(int)
    # make prediction on test
    test_predictions = model.predict(test)
    # get and return confusion matrix
    cm = analysis.get_confusion_matrix(test_predictions, test_labels)
    return cm


def pretty_confusion_matrix(cm):
    classes = np.array([database.CLASSES])
    table = tabulate(np.vstack((np.hstack(([[""]], classes)),
                                np.hstack((classes.T, cm)))))
    return table


if __name__ == '__main__':
    print("Main script for Human Activity Recognition with Random Forest classifier")
    print(pretty_confusion_matrix(base_test('proto1', database.VARIABLES)))
