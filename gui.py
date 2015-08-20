# -*- coding: utf-8 -*-
__author__ = "Radim Spigel"
__version__ = "0.1"

from PySide import QtCore, QtGui
from PySide.QtGui import QMainWindow, QApplication,QStatusBar,QMenuBar,QPlainTextEdit, QComboBox,QTableWidgetItem, QTableWidgetItem,QPushButton,QLineEdit,QWidget,QTableWidget,QLabel

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FilterLbl = QLabel(self.centralwidget)
        self.FilterLbl.setGeometry(QtCore.QRect(30, 150, 60, 15))
        self.FilterLbl.setObjectName("FilterLbl")
        self.FilterCB = QComboBox(self.centralwidget)
        self.FilterCB.setGeometry(QtCore.QRect(450, 150, 100, 22))
        self.FilterCB.setObjectName("FilterCB")
        self.FilterCB.addItem("")
        self.FilterCB.addItem("")
        self.FilterCB.addItem("")
        self.FilterCB.addItem("")         
        self.FilterTF = QLineEdit(self.centralwidget)
        self.FilterTF.setGeometry(QtCore.QRect(100, 150, 320, 20))        
        self.tableView = QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 180, 781, 511))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(4)
        self.tableView.setRowCount(0)
        item = QTableWidgetItem("Cena za kg/l")
        self.tableView.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("Cena ze kus")
        self.tableView.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem(u"Gramaž")
        self.tableView.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem("Popis")
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableView.setHorizontalHeaderItem(3, item)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        
        self.SaveBtn = QPushButton(self.centralwidget)
        self.SaveBtn.setGeometry(QtCore.QRect(30, 10, 100, 23))
        self.SaveBtn.setObjectName("SaveBtn")
        self.PrintSelectedToFileBtn = QPushButton(self.centralwidget)
        self.PrintSelectedToFileBtn.setGeometry(QtCore.QRect(225, 10, 100, 23))        
        self.PrintSelectedToFileBtn.setObjectName("PrintSelectedToFileBtn")
        self.PriceForUnitTF = QLineEdit(self.centralwidget)
        self.PriceForUnitTF.setGeometry(QtCore.QRect(100, 70, 113, 20))
        self.PriceForUnitTF.setObjectName("PriceForUnitTF")
        self.PriceForUnitLbl = QLabel(self.centralwidget)
        self.PriceForUnitLbl.setGeometry(QtCore.QRect(30, 70, 60, 13))
        self.PriceForUnitLbl.setObjectName("PriceForUnitLbl")
        self.ArtikelTF = QLineEdit(self.centralwidget)
        self.ArtikelTF.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.ArtikelTF.setObjectName("ArtikelTF")
        self.ArtikelLbl = QLabel(self.centralwidget)
        self.ArtikelLbl.setGeometry(QtCore.QRect(30, 100, 46, 13))
        self.ArtikelLbl.setObjectName("ArtikelLbl")
        self.DescriptionLbl = QLabel(self.centralwidget)
        self.DescriptionLbl.setGeometry(QtCore.QRect(455, 70, 75, 13))
        self.DescriptionLbl.setObjectName("DescriptionLbl")
        self.UnitLbl = QLabel(self.centralwidget)
        self.UnitLbl.setGeometry(QtCore.QRect(250, 70, 60, 15))
        self.UnitLbl.setObjectName("UnitLbl")
        self.WeightLbl = QLabel(self.centralwidget)
        self.WeightLbl.setGeometry(QtCore.QRect(250, 100, 60, 13))
        self.WeightLbl.setObjectName("UnitLbl")
        self.WeightTF = QLineEdit(self.centralwidget)
        self.WeightTF.setGeometry(QtCore.QRect(320, 100, 100, 20))
        self.WeightTF.setObjectName("WeightTF")        
        self.UnitCB = QComboBox(self.centralwidget)
        self.UnitCB.setGeometry(QtCore.QRect(320, 70, 100, 22))
        self.UnitCB.setObjectName("UnitCB")
        self.UnitCB.addItem("")
        self.UnitCB.addItem("")
        self.DescriptionTE = QPlainTextEdit(self.centralwidget)
        self.DescriptionTE.setGeometry(QtCore.QRect(540, 30, 241, 61))
        self.DescriptionTE.setObjectName("DescriptionTE")
        self.PrintToFileBtn = QPushButton(self.centralwidget)
        self.PrintToFileBtn.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.PrintToFileBtn.setObjectName("PrintToFileBtn")
        self.AddRecordBtn = QPushButton(self.centralwidget)
        self.AddRecordBtn.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.AddRecordBtn.setObjectName("AddRecordBtn")        
        self.SaveChangeBtn = QPushButton(self.centralwidget)
        self.SaveChangeBtn.setGeometry(QtCore.QRect(550, 100, 75, 23))
        self.SaveChangeBtn.setObjectName("SaveChangeBtn")
        self.DeleteRecordBtn = QPushButton(self.centralwidget)
        self.DeleteRecordBtn.setGeometry(QtCore.QRect(650, 100, 75, 23))
        self.DeleteRecordBtn.setObjectName("DeleteRecordBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
   
        self.FilterTF.textChanged.connect(self.on_lineEdit_textChanged)
        self.FilterCB.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def myFilter(self,col=None):
        filt = self.FilterTF.text()
        for ix in range(self.tableView.rowCount()):
            match = False
            if col == None:
                for jx in range(self.tableView.columnCount()):
                    item = self.tableView.item(ix,jx)
                    if filt in item.text():
                        match = True
                        break
                self.tableView.setRowHidden(ix, not match)
            else:
                item = self.tableView.item(ix, col)
                if filt in item.text():
                    match = True
                self.tableView.setRowHidden(ix, not match)

    #@QtCore.pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        self.myFilter()

    #@QtCore.pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, index):
        self.myFilter(col=index)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stitky - {0}".format(__version__)))
        self.SaveBtn.setText(_translate("MainWindow", "Uloz stav tabulky"))
        self.PrintSelectedToFileBtn.setText(_translate("MainWindow", "Tisk vybranych"))
        self.PriceForUnitLbl.setText(_translate("MainWindow", "Cena za kus:"))
        self.ArtikelLbl.setText(_translate("MainWindow", "Artikl:"))
        self.DescriptionLbl.setText(_translate("MainWindow", "Popis produktu:"))
        self.UnitLbl.setText(_translate("MainWindow", "Jednotka:"))
        self.FilterLbl.setText(_translate("MainWindow", "Filtr:"))
        self.WeightLbl.setText(_translate("MainWindow", "Hmotnost:"))
        self.PrintToFileBtn.setText(_translate("MainWindow", "Vytvor txt"))
        self.SaveChangeBtn.setText(_translate("MainWindow", "Uloz zmeny"))
        self.AddRecordBtn.setText(_translate("MainWindow", "Pridej zaznam"))
        self.DeleteRecordBtn.setText(_translate("MainWindow", "Smaz zaznam"))
        self.UnitCB.setItemText(0, _translate("MainWindow", "g"))
        self.UnitCB.setItemText(1, _translate("MainWindow", "ml"))
        self.FilterCB.setItemText(0, _translate("MainWindow", "Cena za kg/l"))
        self.FilterCB.setItemText(1, _translate("MainWindow", "Cena ze kus"))
        self.FilterCB.setItemText(2, _translate("MainWindow", "Gramaz"))
        self.FilterCB.setItemText(3, _translate("MainWindow", "Popis"))
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
