import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    user = "postgres"
    pwd = "RSLrsl123"
    port = 5432
    host = "localhost"
    db_name = "test"

    conn = psycopg2.connect(database="postgres", port=port, host=host, user=user, password=pwd)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = conn.cursor()

    # 创建数据库
    cursor.execute("CREATE DATABASE {}".format(db_name))
    # cursor.execute("CREATE TABLE Layer (FID SERIAL PRIMARY KEY,Shape_Type CHAR(600) NOT NULL,Other_info VARCHAR(255));")
except Exception as e:
    print(e)
conn = psycopg2.connect(database=db_name, port=port, host=host, user=user, password=pwd)
cursor = conn.cursor()
cursor.execute(
    "create extension postgis;"
    "CREATE TABLE POLYGON_Layer (FID SERIAL PRIMARY KEY,layer_ID BIGINT NOT NULL,polygon_ID BIGINT NOT NULL,polygon_label VARCHAR(255),polygon_self_attributeValue VARCHAR(255),polygon GEOMETRY(POLYGON, 26910));"
    "CREATE TABLE LINE_Layer (FID SERIAL PRIMARY KEY,layer_ID BIGINT NOT NULL,line_ID BIGINT NOT NULL,line_label VARCHAR(255),line_self_attributeValue VARCHAR(255),line GEOMETRY(LINESTRING, 26910));"
    "CREATE TABLE POINT_Layer (FID SERIAL PRIMARY KEY,layer_ID BIGINT NOT NULL,point_ID BIGINT NOT NULL,point_label VARCHAR(255),point_self_attributeValue VARCHAR(255),geom GEOMETRY(Point, 26910));"

    "CREATE TABLE Layer (FID SERIAL PRIMARY KEY,Shape_Type CHAR(600) NOT NULL,Other_info VARCHAR(255));")
conn.commit()
