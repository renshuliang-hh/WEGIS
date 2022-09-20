import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database='postgis_32_sample', port=5432, host='localhost', user='postgres',
                        password='RSLrsl123')
cursor = conn.cursor()
print(111)
# 实例化一个可编辑数据模型
sql = "SELECT * FROM wegame_testpoint;"
cursor.execute(sql)
# 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
data = cursor.fetchall()
