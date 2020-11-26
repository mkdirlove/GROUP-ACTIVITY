# -*- coding: utf-8 -*-

#                 $$\             $$\ $$\           $$\                               
#                 $$ |            $$ |\__|          $$ |                              
#   $$$$$$\$$$$\  $$ |  $$\  $$$$$$$ |$$\  $$$$$$\  $$ | $$$$$$\ $$\    $$\  $$$$$$\  
#   $$  _$$  _$$\ $$ | $$  |$$  __$$ |$$ |$$  __$$\ $$ |$$  __$$\\$$\  $$  |$$  __$$\ 
#   $$ / $$ / $$ |$$$$$$  / $$ /  $$ |$$ |$$ |  \__|$$ |$$ /  $$ |\$$\$$  / $$$$$$$$ |
#   $$ | $$ | $$ |$$  _$$<  $$ |  $$ |$$ |$$ |      $$ |$$ |  $$ | \$$$  /  $$   ____|
#   $$ | $$ | $$ |$$ | \$$\ \$$$$$$$ |$$ |$$ |      $$ |\$$$$$$  |  \$  /   \$$$$$$$\ 
#   \__| \__| \__|\__|  \__| \_______|\__|\__|      \__| \______/    \_/     \_______|
                                                                                  

from PyQt5 import QtCore, QtGui, QtWidgets
from bubble_sort import bubble_Sort
from quick_sort import quick_Sort
from shell_sort import shell_Sort
from heap_sort import heap_Sort
from merge_sort import merge_Sort
from insertion_sort import insertion_Sort
from selection_sort import selection_Sort

class MainWindow(object):
    def bubbleSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = bubble_Sort()
        self.ui.setupUi(self.window)
        self.window.show()

    def quickSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = quick_Sort()
        self.ui.setupUi(self.window)
        self.window.show() 

    def shellSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = quick_Sort()
        self.ui.setupUi(self.window)
        self.window.show()

    def heapSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = quick_Sort()
        self.ui.setupUi(self.window)
        self.window.show()

    def mergeSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = quick_Sort()
        self.ui.setupUi(self.window)
        self.window.show()

    def insertionSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = quick_Sort()
        self.ui.setupUi(self.window)
        self.window.show()

    def selectionSort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = quick_Sort()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(493, 306)
        self.pb4 = QtWidgets.QPushButton(Dialog)
        self.pb4.setGeometry(QtCore.QRect(19, 254, 225, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb4.setFont(font)
        self.pb4.setObjectName("pb4")
        self.pb4.clicked.connect(self.heapSort)
        self.pb8 = QtWidgets.QPushButton(Dialog)
        self.pb8.setGeometry(QtCore.QRect(250, 254, 224, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb8.setFont(font)
        self.pb8.setObjectName("pb8")
        self.pb6 = QtWidgets.QPushButton(Dialog)
        self.pb6.setGeometry(QtCore.QRect(250, 178, 224, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb6.setFont(font)
        self.pb6.setObjectName("pb6")
        self.pb6.clicked.connect(self.insertionSort)
        self.pb2 = QtWidgets.QPushButton(Dialog)
        self.pb2.setGeometry(QtCore.QRect(19, 178, 225, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb2.setFont(font)
        self.pb2.setObjectName("pb2")
        self.pb2.clicked.connect(self.quickSort)

        self.pb7 = QtWidgets.QPushButton(Dialog)
        self.pb7.setGeometry(QtCore.QRect(250, 216, 224, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb7.setFont(font)
        self.pb7.setObjectName("pb7")
        self.pb7.clicked.connect(self.selectionSort)
        self.l1 = QtWidgets.QLabel(Dialog)
        self.l1.setGeometry(QtCore.QRect(19, 9, 455, 125))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.pb3 = QtWidgets.QPushButton(Dialog)
        self.pb3.setGeometry(QtCore.QRect(19, 216, 225, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb3.setFont(font)
        self.pb3.setObjectName("pb3")
        self.pb3.clicked.connect(self.shellSort)
        self.pb1 = QtWidgets.QPushButton(Dialog)
        self.pb1.setGeometry(QtCore.QRect(19, 140, 225, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb1.setFont(font)
        self.pb1.setObjectName("pb1")
        self.pb1.clicked.connect(self.bubbleSort)

        self.pb5 = QtWidgets.QPushButton(Dialog)
        self.pb5.setGeometry(QtCore.QRect(250, 140, 224, 32))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.pb5.setFont(font)
        self.pb5.setObjectName("pb5")
        self.pb5.clicked.connect(self.mergeSort)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Group Activity"))
        self.pb4.setText(_translate("Dialog", "HEAP SORT"))
        self.pb8.setText(_translate("Dialog", "CLOSE PROGRAM"))
        self.pb6.setText(_translate("Dialog", "INSERTION SORT"))
        self.pb2.setText(_translate("Dialog", "QUICK SORT"))
        self.pb7.setText(_translate("Dialog", "SELECTION SORT"))
        self.l1.setText(_translate("Dialog", "      PYTHON SORTING ALGORITHMS"))
        self.pb3.setText(_translate("Dialog", "SHELL SORT"))
        self.pb1.setText(_translate("Dialog", "BUBBLE SORT"))
        self.pb5.setText(_translate("Dialog", "MERGE SORT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
