import plotly.express as px
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools

def get_confusion_matrix(prediction_label, true_label):
    return confusion_matrix(true_label, prediction_label)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    # Normalize if wanted
    if normalize:
        cm = cm / np.sum(cm)

    # Create confusion matrix graph
    fig = px.imshow(cm,
                    labels=dict(x="Predicted label", y="True label", color="value"),
                    x=classes,
                    y=classes,
                    color_continuous_scale='Blues',
                    title=title
                )
    fig.show()
