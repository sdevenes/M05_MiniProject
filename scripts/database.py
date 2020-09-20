#!/usr/bin/env python
import numpy as np
import csv
import os

PROTOCOLS = {
    'proto1': {'train': (0, 0.6), 'validation': (0.6, 0.8), 'test': (0.8, 1)},
    'proto2': {'train': (0.4, 1), 'validation': (0, 0.2), 'test': (0.2, 0.4)},
}

SUBSETS = [
    'train',
    'validation',
    'test'
]

CLASSES = [
    'Other_Activity',
    'Watch_TV',
    'Sleep_Out_Of_Bed',
    'Bathe',
    'Cook_Breakfast',
    'Dress',
    'Toilet',
    'Personal_Hygiene',
    'Sleep',
    'Read',
    'Relax',
    'Cook_Dinner',
    'Drink',
    'Eat_Breakfast',
    'Morning_Meds',
    'Evening_Meds',
    'Wash_Breakfast_Dishes',
    'Cook_Lunch',
    'Wash_Dishes',
    'Leave_Home',
    'Cook',
    'Enter_Home',
    'Entertain_Guests',
    'Wash_Dinner_Dishes',
    'Phone',
    'Groom',
    'Step_Out',
    'Eat_Dinner',
    'Eat_Lunch',
    'Wash_Lunch_Dishes',
    'Bed_Toilet_Transition',
    'Eat',
    'Go_To_Sleep',
    'Wake_Up',
    'Work_At_Table'
]

VARIABLES = [
    'lastSensorEventHours',
    'lastSensorEventSeconds',
    'lastSensorDayOfWeek',
    'windowDuration',
    'timeSinceLastSensorEvent',
    'prevDominantSensor1',
    'prevDominantSensor2',
    'lastSensorID',
    'lastSensorLocation',
    'lastMotionLocation',
    'complexity',
    'activityChange',
    'areaTransitions',
    'numDistinctSensors',
    'sensorCount-Bathroom',
    'sensorCount-Bedroom',
    'sensorCount-Chair',
    'sensorCount-DiningRoom',
    'sensorCount-Hall',
    'sensorCount-Ignore',
    'sensorCount-Kitchen',
    'sensorCount-LivingRoom',
    'sensorCount-Office',
    'sensorCount-OutsideDoor',
    'sensorCount-WorkArea',
    'sensorElTime-Bathroom',
    'sensorElTime-Bedroom',
    'sensorElTime-Chair',
    'sensorElTime-DiningRoom',
    'sensorElTime-Hall',
    'sensorElTime-Ignore',
    'sensorElTime-Kitchen',
    'sensorElTime-LivingRoom',
    'sensorElTime-Office',
    'sensorElTime-OutsideDoor',
    'sensorElTime-WorkArea'
]


def load(setname='csh101'):
    data = dict([(k, []) for k in CLASSES])
    with open(os.path.join('../data', setname, '{}.ann.features.csv'.format(setname)), 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for k, row in enumerate(reader):
            if not k: continue
            data[row[-1]].append(np.array([z for z in row[:-1]]))
    for k in CLASSES:
        data[k] = np.vstack(data[k])
    return data


def split_data(data, subset, splits):
    return dict([(k, data[k][range(int(splits[subset][0] * data[k].shape[0]),
                                   int(splits[subset][1] * data[k].shape[0]))]) for k in data])


def get(protocol, subset, classes=CLASSES, variables=VARIABLES, setname='csh101'):
    retval = split_data(load(setname), subset, PROTOCOLS[protocol])
    varindex = [VARIABLES.index(k) for k in variables]
    retval = dict([(k, retval[k][:, varindex]) for k in classes])
    return np.array([retval[k] for k in classes], dtype=object)
