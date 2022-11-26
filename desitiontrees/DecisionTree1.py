from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot
import numpy
import pandas
import os


class DecisionTree1:
    def predicting_breast_cancer(self):
        dataset = pandas.read_csv("/Users/josuevargas/PycharmProjects/machineLearn/datasets/archive"
                                  "/train_genetic_disorders.csv")
        print(dataset.head())



    def print_current_directory(self):
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))