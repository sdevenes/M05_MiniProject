from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

import logging
logger = logging.getLogger()


def make_labels(X):
  return np.hstack([k*np.ones(len(X[k]), dtype=int) for k in range(len(X))])


class Model:
  def __init__(self, nb_tree_per_forest=50, max_depth=10):
    # Create a random forest model
    self.model = RandomForestClassifier(n_estimators=nb_tree_per_forest, max_depth=max_depth,
                                        random_state=0)


  def train(self, X):

    # Get features
    X_features = np.vstack([k for k in X])

    # Get labels
    y = make_labels(X)

    # Train the model
    self.model.fit(X_features, y)


  def predict(self, X):
    # Get features
    X_features = np.vstack([k for k in X])

    # Predict using the trained model
    prediction = self.model.predict(X_features)

    return prediction