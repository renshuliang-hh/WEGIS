from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
try:
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setPort(5432)
    db.setUserName('postgres')
    db.setPassword('RSLrsl123')c
    db.setDatabaseName('test123'+'.db')
    aa=db.open()
    print(aa)
except Exception as e:
    print(e)


