import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
from DatabasemMainWindow import Ui_DataBaseMainWindow
from functools import partial
from PyQt5.QtSql import QSqlDatabase
from NewDBDialog import Ui_newdbDialog
from ConnectDBDialog import Ui_connectdbDialog
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from PyQt5 import QtPrintSupport, QtGui
from PyQt5.QtCore import Qt, QMimeData, QDate, QDateTime, QTime
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFormLayout, QLabel, QLineEdit, QPushButton, QGridLayout, \
    QCalendarWidget, QVBoxLayout, QDateTimeEdit, QAction, QMainWindow, QTextEdit, QStatusBar, QFileDialog, QDialog, \
    QTableView


class DatabaseWindow(QMainWindow, Ui_DataBaseMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newdbButton.clicked.connect(self.create_db)
        self.connectButton.clicked.connect(self.connect_db)
        self.browseButton.clicked.connect(self.view_data)
        self.Newdb = NewdbDialog()
        self.Connectdb = ConnectdbDialog()
        self.name = None
        self.host = None
        self.port = None
        self.bd = None
        self.username = None
        self.PWD = None
        self.connection = None
        self.Newdb._signal.connect(self.get_db_info)
        self.Connectdb._signal.connect(self.get_db_info)

    def get_db_info(self, name, host, port, bd, user, pwd):
        self.name = name
        self.host = host
        self.port = port
        self.bd = bd
        self.username = user
        self.PWD = pwd

        print(self.name, self.host, self.port, )

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

            conn = psycopg2.connect(database=self.bd, port=self.port, host=self.host, user=self.username,
                                    password=self.PWD)
            cursor = conn.cursor()
            cursor.execute(
                "create extension postgis;"
                "CREATE TABLE POLYGON_Layer (FID SERIAL PRIMARY KEY,layer_ID BIGINT NOT NULL,polygon_ID BIGINT NOT NULL,polygon_label VARCHAR(255),polygon_self_attributeValue VARCHAR(255),polygon GEOMETRY(POLYGON, 26910));"
                "CREATE TABLE LINE_Layer (FID SERIAL PRIMARY KEY,layer_ID BIGINT NOT NULL,line_ID BIGINT NOT NULL,line_label VARCHAR(255),line_self_attributeValue VARCHAR(255),line GEOMETRY(LINESTRING, 26910));"
                "CREATE TABLE POINT_Layer (FID SERIAL PRIMARY KEY,layer_ID BIGINT NOT NULL,point_ID BIGINT NOT NULL,point_label VARCHAR(255),point_self_attributeValue VARCHAR(255),geom GEOMETRY(Point, 26910));"
                "CREATE TABLE Layer (FID SERIAL PRIMARY KEY,Shape_Type CHAR(600) NOT NULL,Other_info VARCHAR(255));")
            conn.commit()
            QMessageBox.information(self, "成功", "创建数据库成功", QMessageBox.Yes)


        except Exception as e:
            print(str(e))
            QMessageBox.critical(self, "错误", str(e))

    def connect_db(self):

        self.Connectdb.exec_()
        try:
            db = QSqlDatabase("QPSQL")
            db.setUserName(self.username)  # postgres is the default root username
            db.setPassword(self.PWD)
            db.setHostName(self.host)
            db.setPort(int(self.port))
            db.setDatabaseName(self.bd)

            if db.open():
                self.connection = db
                QMessageBox.information(self, "成功", "已经连接" + self.bd + "数据库", QMessageBox.Yes)
                print(db.open())
            else:
                QMessageBox.critical(self, "失败", "请检查")


        except Exception as e:
            print(str(e))
            QMessageBox.critical(self, "错误", str(e))

            # conn = psycopg2.connect(database=self.bd, port=self.port, host=self.host, user=self.username,
            #                         password=self.PWD)
            # self.cursor = conn.cursor()

    def view_data(self):
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")  # postgres is the default root username
        db.setPassword('RSLrsl123')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('postgis_32_sample')
        print(db.open())
        self.model = QtSql.QSqlTableModel()
        self.dbtableView.setModel(self.model)

        self.model.setTable("wegame_testpoint")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal, "GID")
        # self.model.setHeaderData(1, QtCore.Qt.Horizontal, "ID")
        self.dbtableView.setColumnHidden(2, True)




        # conn = psycopg2.connect(database='postgis_32_sample', port=5432, host='localhost', user='postgres',
        #                         password='RSLrsl123')
        # self.cursor = conn.cursor()
        # print(111)
        # # 实例化一个可编辑数据模型
        # sql = "SELECT * FROM wegame_testpoint;"
        # self.cursor.execute(sql)
        # # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        # data = self.cursor.fetchall()
        # # 打印测试
        # print(data)
        # row = self.cursor.rowcount  # 获取记录个数，用于设置表格的行数
        # vol = len(data[0])
        # self.model = QStandardItemModel(row, vol)
        # self.model.setHorizontalHeaderLabels(['gid', 'id', 'geom'])
        # self.dbtableView.setModel(self.model)
        #
        # for i in range(row):
        #     for j in range(vol):
        #         self.model.setItem(i, j, QStandardItem(str(data[i][j])))




class ConnectdbDialog(QDialog, Ui_connectdbDialog):
    _signal = QtCore.pyqtSignal(str, str, str, str, str, str)  # 声明信号

    def __init__(self):
        super(ConnectdbDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.connectdbBox.accepted.connect(self.slot1)
        self.connectdbBox.rejected.connect(self.close)

    def slot1(self):
        cdbName = self.cdbNamelineEdit.text()
        cdbHost = self.cdbHostlineEdit.text()
        cdbPort = self.cdbPortlineEdit.text()
        cdbDB = self.cdbDBlineEdit.text()
        cdbUser = self.cdbUserNamelineEdit.text()
        cdbPWD = self.cdbPWDlineEdit.text()

        self._signal.emit(cdbName, cdbHost, cdbPort, cdbDB, cdbUser, cdbPWD)
        self.close()


class NewdbDialog(QDialog, Ui_newdbDialog):
    _signal = QtCore.pyqtSignal(str, str, str, str, str, str)  # 声明信号

    def __init__(self):
        super(NewdbDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.newdbBox.accepted.connect(self.slot1)
        self.newdbBox.rejected.connect(self.close)

    def slot1(self):
        ndbName = self.ndbNamelineEdit.text()
        ndbHost = self.ndbHostlineEdit.text()
        ndbPort = self.ndbPortlineEdit.text()
        ndbDB = self.ndbDBlineEdit.text()
        ndbUser = self.ndbUserNamelineEdit.text()
        ndbPWD = self.ndbPWDlineEdit.text()
        self._signal.emit(ndbName, ndbHost, ndbPort, ndbDB, ndbUser, ndbPWD)
        self.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    DatabaseWindow = DatabaseWindow()
    DatabaseWindow.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
