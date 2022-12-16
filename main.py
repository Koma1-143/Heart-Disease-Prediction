import numpy as np
import pandas as pd
import sys
import time
from tkinter import messagebox
from tkinter import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDial, QApplication, QMainWindow
from PyQt5.uic import loadUi
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#training model
heart_data = pd.read_csv('heart_disease_data.csv')
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
model = LogisticRegression()
model.fit(X_train, Y_train)
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# bulduing UI


class ui(QMainWindow):
    def __init__(self):
        super(ui, self).__init__()
        loadUi('front.ui', self)
        self.process.clicked.connect(self.prediction)

    def prediction(self):
        age = int(self.age.text())
        sex = int(self.sex.text())
        cp = int(self.cp.text())
        trestbps = int(self.trestbps.text())
        chol = int(self.chol.text())
        fbs = int(self.fbs.text())
        restecg = int(self.restecg.text())
        thalach = int(self.thalach.text())
        exang = int(self.exang.text())
        oldpeak = int(self.oldpeak.text())
        slope = int(self.slope.text())
        ca = int(self.cp.text())
        thal = int(self.thal.text())
        
        
        input_data = (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

# change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        print(prediction)
        if (prediction[0] == 0):
            Window = Tk()
            Window.geometry("800x600")
            Window.title("Success")
            messagebox.showinfo("Congratulations","The Person does not have a Heart Disease")
            Window.destroy()
            Window.mainloop()
        else:
            Window = Tk()
            Window.geometry("800x600")
            Window.title("Warning")
            messagebox.showinfo("warning","The Person might have a Heart Disease")
            Window.destroy()
            Window.mainloop()
            


app = QApplication(sys.argv)
fv = ui()
widget = QtWidgets.QStackedWidget()
widget.addWidget(fv)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
