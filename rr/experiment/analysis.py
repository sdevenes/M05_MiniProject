import plotly.express as px
from sklearn.metrics import confusion_matrix
import numpy as np


def get_confusion_matrix(prediction_label, true_label):
    """Get the confusion matrix given the predicted and true labels

    Args:
        prediction_label (list): Estimated targets as returned by a classifier.
        true_label (list): Ground truth (correct) target values.
    Returns:
        numpy.ndarray: A 2D array (with a dtype of int) containing the confusion matrix.
    Raises:
        None
    """
    return confusion_matrix(true_label, prediction_label)


def plot_confusion_matrix(
    cm, classes, normalize=False, title="Confusion matrix", file_name="graph"
):
    """Generate a plot of the given confusion matrix using plotly express

    Args:
        cm (numpy.ndarray): A 2D array (with a dtype of int) containing the confusion matrix.
        classes (numpy.ndarray): A 1D array (with a dtype of str) containing the lable name for each class
        normalize (boolean): Flag to normalize the data
        title (str): The title of the plot
        file_name (str): File name to export the graph
    Returns:
        None
    Raises:
        None
    """
    if normalize:
        cm = cm / np.sum(cm)

    # Create confusion matrix graph
    fig = px.imshow(
        cm,
        labels=dict(x="Predicted label", y="True label", color="value"),
        x=classes,
        y=classes,
        color_continuous_scale="Blues",
        title=title,
    )
    fig.write_html("{}.html".format(file_name))
