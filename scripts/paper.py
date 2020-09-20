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


def test_impact_nb_trees(tabnum):
    nb_trees = [1, 5, 10]
    print("\nImpact of number of trees per forest")
    for n, p in enumerate(database.PROTOCOLS):
        for m, nb_tree_per_forest in enumerate(nb_trees):
            print("\nTable {table_number}: Confusion matrix with {nb_trees} tree(s) for Protocol `{protocol}`".format(
                table_number=(n * len(nb_trees)) + m + tabnum,
                protocol=p,
                nb_trees=nb_tree_per_forest)
            )
            cm = base_test(p, database.VARIABLES, nb_tree_per_forest=nb_tree_per_forest)
            print(pretty_confusion_matrix(cm))

def test_impact_tree_depth(tabnum):
    depths = [1, 5, 10]
    print("\nImpact of trees maximum depth")
    for n, p in enumerate(database.PROTOCOLS):
        for m, max_depth in enumerate(depths):
            print("\nTable {table_number}: Confusion matrix with trees maximum depth of {max_depth} for Protocol `{protocol}`".format(
                table_number=(n * len(depths)) + m + tabnum,
                protocol=p,
                max_depth=max_depth)
            )
            cm = base_test(p, database.VARIABLES, max_depth=max_depth, nb_tree_per_forest=10)
            print(pretty_confusion_matrix(cm))


if __name__ == '__main__':
    print("Main script for Human Activity Recognition with Random Forest classifier")
    test_impact_nb_trees(1)
    test_impact_tree_depth(7)
