from tabulate import tabulate
from rr.experiment import algorithm, database, analysis
import numpy as np
import os.path


def base_experiment(protocol, variables, filepath, nb_tree_per_forest=50, max_depth=10):
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
    x_train, y_train = database.get(
        protocol, "train", database.CLASSES, variables, filepath
    )
    model = algorithm.Model(nb_tree_per_forest, max_depth)
    model.train(x_train, y_train)
    x_test, y_test = database.get(
        protocol, "test", database.CLASSES, variables, filepath
    )
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
    table = tabulate(
        np.vstack((np.hstack(([[""]], classes)), np.hstack((classes.T, cm))))
    )
    return table


def experiment_impact_nb_trees(tabnum, filepath, nb_trees, max_depth, plot_path):
    """Evaluates the impact of the number of trees per forest on the classifiers performance

    Args:
        tabnum (int): first confusion matrix numbering
        filepath (str): path to the file containing the dataset to load
        nb_trees (list): list of number of trees to evaluate
        max_depth (int): trees maximum depth
        plot_path (str): folder where to store confusion matrix plots
    Returns:
        str : experiment results
    Raises:
        None
    """
    print("Starting experiment on number of trees impact...")
    result = "\nImpact of number of trees per forest"
    for n, p in enumerate(database.PROTOCOLS):
        print("Processing `protocol` {}...".format(p))
        for m, nb_tree_per_forest in enumerate(nb_trees):
            num = (n * len(nb_trees)) + m + tabnum
            result += "\nTable {table_number}: Confusion matrix with {nb_trees} tree(s) for Protocol `{protocol}`".format(
                table_number=num,
                protocol=p,
                nb_trees=nb_tree_per_forest,
            )
            cm = base_experiment(
                p,
                database.VARIABLES,
                nb_tree_per_forest=nb_tree_per_forest,
                max_depth=max_depth,
                filepath=filepath,
            )
            result += pretty_confusion_matrix(cm)
            analysis.plot_confusion_matrix(
                cm,
                database.CLASSES,
                file_name=os.path.join(plot_path, "table_{}".format(num)),
            )
    print("Experiment completed\n")
    return result


def experiment_impact_tree_depth(tabnum, filepath, nb_trees, max_depths, plot_path):
    """Evaluates and the impact of the trees depth on the classifiers performance

    Args:
        tabnum (int): first confusion matrix numbering
        filepath (str): path to the file containing the dataset to load
        nb_trees (int): number of trees in forest
        max_depths (list): list of trees maximum depths to evaluate
        plot_path (str): folder where to store confusion matrix plots
    Returns:
        str : experiment results
    Raises:
        None
    """
    print("Starting experiment on tree depth impact...")
    result = "\nImpact of trees maximum depth"
    for n, p in enumerate(database.PROTOCOLS):
        print("Processing `protocol` {}".format(p))
        for m, max_depth in enumerate(max_depths):
            num = (n * len(max_depths)) + m + tabnum
            result += "\nTable {table_number}: Confusion matrix with trees maximum depth of {max_depth} for Protocol `{protocol}`".format(
                table_number=num,
                protocol=p,
                max_depth=max_depth,
            )
            cm = base_experiment(
                p,
                database.VARIABLES,
                nb_tree_per_forest=nb_trees,
                max_depth=max_depth,
                filepath=filepath,
            )
            result += pretty_confusion_matrix(cm)
            analysis.plot_confusion_matrix(
                cm,
                database.CLASSES,
                file_name=os.path.join(plot_path, "table_{}".format(num)),
            )
    print("Experiment completed\n")
    return result
