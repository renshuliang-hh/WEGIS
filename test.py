from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication

app = QApplication([])

db = QSqlDatabase.addDatabase("QPSQL")
db.setUserName("postgres")  # postgres is the default root username
db.setPassword('RSLrsl123')
db.setHostName('localhost')
db.setPort(5432)
db.setDatabaseName('postgis_32_sample')
print(db.open())
query = QSqlQuery()
isSuccess = query.exec("select count(*) from wegame_testpoint;")
if not isSuccess:
    print(query.lastError().text())

if query.next():
    count = query.value(0)
