import numpy as np
import csv
from sklearn.model_selection import train_test_split

PROTOCOLS = {
    "proto1": {"train": 0.8, "test": 0.2, "random": 1},
    "proto2": {"train": 0.8, "test": 0.2, "random": 2},
}

SUBSETS = ["train", "validation", "test"]

CLASSES = [
    "Other_Activity",
    "Watch_TV",
    "Sleep_Out_Of_Bed",
    "Bathe",
    "Cook_Breakfast",
    "Dress",
    "Toilet",
    "Personal_Hygiene",
    "Sleep",
    "Read",
    "Relax",
    "Cook_Dinner",
    "Drink",
    "Eat_Breakfast",
    "Morning_Meds",
    "Evening_Meds",
    "Wash_Breakfast_Dishes",
    "Cook_Lunch",
    "Wash_Dishes",
    "Leave_Home",
    "Cook",
    "Enter_Home",
    "Entertain_Guests",
    "Wash_Dinner_Dishes",
    "Phone",
    "Groom",
    "Step_Out",
    "Eat_Dinner",
    "Eat_Lunch",
    "Wash_Lunch_Dishes",
    "Bed_Toilet_Transition",
    "Eat",
    "Go_To_Sleep",
    "Wake_Up",
    "Work_At_Table",
]

VARIABLES = [
    "lastSensorEventHours",
    "lastSensorEventSeconds",
    "lastSensorDayOfWeek",
    "windowDuration",
    "timeSinceLastSensorEvent",
    "prevDominantSensor1",
    "prevDominantSensor2",
    "lastSensorID",
    "lastSensorLocation",
    "lastMotionLocation",
    "complexity",
    "activityChange",
    "areaTransitions",
    "numDistinctSensors",
    "sensorCount-Bathroom",
    "sensorCount-Bedroom",
    "sensorCount-Chair",
    "sensorCount-DiningRoom",
    "sensorCount-Hall",
    "sensorCount-Ignore",
    "sensorCount-Kitchen",
    "sensorCount-LivingRoom",
    "sensorCount-Office",
    "sensorCount-OutsideDoor",
    "sensorCount-WorkArea",
    "sensorElTime-Bathroom",
    "sensorElTime-Bedroom",
    "sensorElTime-Chair",
    "sensorElTime-DiningRoom",
    "sensorElTime-Hall",
    "sensorElTime-Ignore",
    "sensorElTime-Kitchen",
    "sensorElTime-LivingRoom",
    "sensorElTime-Office",
    "sensorElTime-OutsideDoor",
    "sensorElTime-WorkArea",
]


def load(filepath="./data/csh101/csh101.ann.features.csv"):
    """Loads the dataset

    Args:
        filepath (str): path to the file containing the dataset to load
    Returns:
       x (numpy.ndarray):A NxM 2D-array where each row corresponds to a sample and each column to a feature
       y (numpy.ndarray): A 1D-array of length N, where each element corresponds to a sample label
    Raises:
        None
    """
    x = []
    y = []
    with open(filepath, "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for k, row in enumerate(reader):
            if not k:
                continue
            x.append(row[:-1])
            y.append(row[-1])
    return np.array(x), np.array(y)


def split_data(x, y, subset, splits):
    """Splits the data set

    Args:
        x (numpy.ndarray):A NxM 2D-array where each row corresponds to a sample and each column to a feature
        y (numpy.ndarray): A 1D-array of length N, where each element corresponds to a sample label
        subset (str): subset to extract (train or test)
        splits (dict): a dictionary mapping the subsets to their dataset proportion and the random state to use for splitting
    Returns:
        x_split (numpy.ndarray):A PxM 2D-array containing only a subset of samples
        y_split (numpy.ndarray): A 1D-array of length P containing only the labels corresponding to the subset x_split
    Raises:
        None
    """
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=splits["test"],
        train_size=splits["train"],
        random_state=splits["random"],
        stratify=y,
    )
    (x_split, y_split) = (x_train, y_train) if subset == "train" else (x_test, y_test)
    return x_split, y_split


def get(
    protocol,
    subset,
    classes=CLASSES,
    variables=VARIABLES,
    filepath="./data/csh101/csh101.ann.features.csv",
):
    """Get the desired subset

    Args:
        protocol (str): protocol to use
        subset (str): subset to extract (train or test)
        classes (list): list of desired classes
        variables (list): list of desired variables (features)
        filepath (str): path to the file containing the dataset to load
    Returns:
        ret_x (numpy.ndarray):A PxQ 2D-array containing only the desired subset of samples with the Q desired features
        ret_y (numpy.ndarray): A 1D-array of length P containing only the labels corresponding to the subset ret_x
    Raises:
        None
    """
    x, y = load(filepath)
    x_split, y_split = split_data(x, y, subset, PROTOCOLS[protocol])
    var_index = [VARIABLES.index(k) for k in variables]
    classes_condition = np.isin(y_split, classes)
    ret_x = x_split[classes_condition][:, var_index]
    ret_y = y_split[classes_condition]
    return ret_x, ret_y
