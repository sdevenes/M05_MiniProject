from sklearn.ensemble import RandomForestClassifier

import logging

logger = logging.getLogger()


class Model:
    def __init__(self, nb_tree_per_forest=50, max_depth=10):
        """Create a new ML model (Random forest classifier from scikitlearn)

        Args:
            nb_tree_per_forest (int): number of decision trees in the forest
            max_depth (int): max depth of the trees
        Returns:
            None
        Raises:
            None
        """
        self.model = RandomForestClassifier(
            n_estimators=nb_tree_per_forest, max_depth=max_depth, random_state=0
        )

    def train(self, X, y):
        """Train the model using the given data

        Args:
            X (numpy.ndarray):A NxM 2D-array where each row corresponds to a sample and each column to a feature
            y (numpy.ndarray): A 1D-array of length N, where each element corresponds to a sample label
        Returns:
            None
        Raises:
            None
        """
        self.model.fit(X, y)

    def predict(self, X):
        """Make a prediction on the data using the trained model

        Args:
            X (numpy.ndarray):A NxM 2D-array where each row corresponds to a sample and each column to a feature
        Returns:
            numpy.ndarray: A 1D array (with a dtype of int) containing the predicted
            label for each sample

        Raises:
            None
        """
        prediction = self.model.predict(X)

        return prediction
