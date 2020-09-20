from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

import logging
logger = logging.getLogger()


def make_labels(X):
    """Generate label array from the given data

    Args:
        X (list): A list of 1D array (with a dtype of float64) showing the input
                  training samples, where each item of the list correspond to one class.
    Returns:
        numpy.ndarray: A 1D array (with a dtype of int) containing the
        label for each sample
    Raises:
        None
    """
    return np.hstack([k*np.ones(len(X[k]), dtype=int) for k in range(len(X))])


class Model:
  def __init__(self, nb_tree_per_forest=50, max_depth=10):
    """Create a new ML model (Random forest classifier from scikitlearn)

    Args:
        nb_tree_per_forest: number of decision trees in the forest
        max_depth: max depth of the trees
    Returns:
        None
    Raises:
        None
    """
    # Create a random forest model
    self.model = RandomForestClassifier(n_estimators=nb_tree_per_forest, max_depth=max_depth,
                                        random_state=0)


  def train(self, X):
    """Train the model using the given data

    Args:
        X (list): A list of 1D array (with a dtype of float64) showing the input training samples, 
                  where each item of the list correspond to one class.
    Returns:
        None
    Raises:
        None
    """
    # Get features
    X_features = np.vstack([k for k in X])

    # Get labels
    y = make_labels(X)

    # Train the model
    self.model.fit(X_features, y)


  def predict(self, X):
    """Make a prediction on the data using the trained model

    Args:
        X (list): A list of 1D array (with a dtype of float64) showing the input training samples, 
                  where each item of the list correspond to one class.
    Returns:
        numpy.ndarray: A 1D array (with a dtype of int) containing the predicted
        label for each sample
                       
    Raises:
        None
    """
    # Get features
    X_features = np.vstack([k for k in X])

    # Predict using the trained model
    prediction = self.model.predict(X_features)

    return prediction