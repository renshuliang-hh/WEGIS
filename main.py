import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QDialog,QMessageBox
from PyQt5 import QtGui,QtCore,QtWidgets,QtSql
from DatabasemMainWindow import Ui_DataBaseMainWindow
from functools import partial

from NewDBDialog import Ui_newdbDialog
from ConnectDBDialog import Ui_connectdbDialog
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT




class DatabaseWindow(QMainWindow,Ui_DataBaseMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newdbButton.clicked.connect(self.create_db)
        self.connectButton.clicked.connect(self.connect_db)
        self.Newdb = NewdbDialog()
        self.Connectdb = ConnectdbDialog()
        self.name=None
        self.host = None
        self.port = None
        self.bd = None
        self.username = None
        self.PWD = None
        self.Newdb._signal.connect(self.get_db_info)
        self.Connectdb._signal.connect(self.get_db_info)


    def get_db_info(self,name,host,port,bd,user,pwd):
        self.name = name
        self.host = host
        self.port = port
        self.bd = bd
        self.username = user
        self.PWD = pwd
        print(self.name, self.host, self.port,)








    def create_db(self):
        self.Newdb.exec_()
        print('连接数据库准备')

        try:
            conn = psycopg2.connect(database="postgres", port=self.port, host=self.host, user=self.username,
                                    password=self.PWD)
            # conn = psycopg2.connect(database="postgres", port=5432, host='localhost', user='postgres', password='RSLrsl123')

            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE {}".format(self.bd))

            QMessageBox.information(self, "成功", "创建数据库成功", QMessageBox.Yes)


        except Exception as e:
            print(str(e))
            QMessageBox.critical(self, "错误", str(e))








    def connect_db(self):

        self.Connectdb.exec_()
        # self.Connectdb = ConnectdbDialog()

        # self.Connectdb.show()
        # self.Connectdb._signal.connect(self.get_db_info)






class ConnectdbDialog(QDialog,Ui_connectdbDialog):
    _signal = QtCore.pyqtSignal(str, str,int, str,str, str)#声明信号
    def __init__(self):
        super(ConnectdbDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.connectdbBox.accepted.connect(self.slot1)
        self.connectdbBox.rejected.connect(self.close)
    def slot1(self):
        cdbName = self.cdbNamelineEdit.text()
        cdbHost = self.cdbHostlineEdit.text()
        cdbPort= self.cdbPortlineEdit.text()
        cdbDB = self.cdbDBlineEdit.text()
        cdbUser = self.cdbUserNamelineEdit.text()
        cdbPWD = self.cdbPWDlineEdit.text()

        self._signal.emit(cdbName,cdbHost,cdbPort,cdbDB,cdbUser,cdbPWD)
        self.close()



class NewdbDialog(QDialog,Ui_newdbDialog):
    _signal = QtCore.pyqtSignal(str, str,str, str,str, str)#声明信号
    def __init__(self):
        super(NewdbDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.newdbBox.accepted.connect(self.slot1)
        self.newdbBox.rejected.connect(self.close)
    def slot1(self):
        ndbName = self.ndbNamelineEdit.text()
        ndbHost = self.ndbHostlineEdit.text()
        ndbPort= self.ndbPortlineEdit.text()
        ndbDB = self.ndbDBlineEdit.text()
        ndbUser = self.ndbUserNamelineEdit.text()
        ndbPWD = self.ndbPWDlineEdit.text()
        self._signal.emit(ndbName,ndbHost,ndbPort,ndbDB,ndbUser,ndbPWD)
        self.close()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app=QApplication(sys.argv)
    DatabaseWindow=DatabaseWindow()
    DatabaseWindow.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
