#!/usr/bin/env python
from tabulate import tabulate
import algorithm
import database
import analysis
import numpy as np


def base_test(protocol, variables, filepath, nb_tree_per_forest=50, max_depth=10):
    """Basic test for the random forest classifier

    Args:
        protocol (str): protocol to use
        variables (1d-array): list of desired variables (features)
        filepath (str): path to the file containing the dataset to load
        nb_tree_per_forest: number of decision trees in the forest
        max_depth: max depth of the trees
    Returns:
        numpy.ndarray: A 2D array (with a dtype of int) containing the confusion matrix.
    Raises:
        None
    """
    x_train, y_train = database.get(protocol, 'train', database.CLASSES, variables, filepath)
    model = algorithm.Model(nb_tree_per_forest, max_depth)
    model.train(x_train, y_train)
    x_test, y_test = database.get(protocol, 'test', database.CLASSES, variables, filepath)
    test_predictions = model.predict(x_test)
    cm = analysis.get_confusion_matrix(test_predictions, y_test)
    return cm


def pretty_confusion_matrix(cm):
    """Adds labels to confusion matrix

    Args:
        cm (numpy.ndarray): A 2D array (with a dtype of int) containing the confusion matrix.
    Returns:
        str: nicely formatted confusion matrix for printing
    Raises:
        None
    """
    classes = np.array([database.CLASSES])
    table = tabulate(np.vstack((np.hstack(([[""]], classes)),
                                np.hstack((classes.T, cm)))))
    return table


def test_impact_nb_trees(tabnum, filepath):
    """Evaluates and print the impact of the number of trees per forest on the classifiers performance

    Args:
        tabnum (int): first confusion matrix numbering
        filepath (str): path to the file containing the dataset to load
    Returns:
        None
    Raises:
        None
    """
    nb_trees = [1, 5, 10]
    print("\nImpact of number of trees per forest")
    for n, p in enumerate(database.PROTOCOLS):
        for m, nb_tree_per_forest in enumerate(nb_trees):
            print("\nTable {table_number}: Confusion matrix with {nb_trees} tree(s) for Protocol `{protocol}`".format(
                table_number=(n * len(nb_trees)) + m + tabnum,
                protocol=p,
                nb_trees=nb_tree_per_forest)
            )
            cm = base_test(p, database.VARIABLES, nb_tree_per_forest=nb_tree_per_forest, filepath=filepath)
            print(pretty_confusion_matrix(cm))


def test_impact_tree_depth(tabnum, filepath):
    """Evaluates and print the impact of the trees depth on the classifiers performance

    Args:
        tabnum (int): first confusion matrix numbering
        filepath (str): path to the file containing the dataset to load
    Returns:
        None
    Raises:
        None
    """
    depths = [1, 5, 10]
    print("\nImpact of trees maximum depth")
    for n, p in enumerate(database.PROTOCOLS):
        for m, max_depth in enumerate(depths):
            print(
                "\nTable {table_number}: Confusion matrix with trees maximum depth of {max_depth} for Protocol `{protocol}`".format(
                    table_number=(n * len(depths)) + m + tabnum,
                    protocol=p,
                    max_depth=max_depth)
            )
            cm = base_test(p, database.VARIABLES, max_depth=max_depth, nb_tree_per_forest=10, filepath=filepath)
            print(pretty_confusion_matrix(cm))


if __name__ == '__main__':
    print("Main script for Human Activity Recognition with Random Forest classifier")
    test_impact_nb_trees(1, filepath='../data/csh101/csh101.ann.features.csv')
    test_impact_tree_depth(7, filepath='../data/csh101/csh101.ann.features.csv')
