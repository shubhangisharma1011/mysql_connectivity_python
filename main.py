import mysql.connector as connector
import sqlite3
import pandas as pd

#connect with sql
"""con = connector.connect(host='localhost',port='3306',user='root',password='Queen#123',database='TestData',auth_plugin='mysql_native_password')
print(con)
"""
#extract csv file
amazon_data = pd.read_csv('Amazon.csv', index_col=False, delimiter = ',')
print(amazon_data.head())


import mysql.connector as msql
from mysql.connector import Error
try:
    con = connector.connect(host='localhost',port='3306',user='root',password='Queen#123',database='Students',auth_plugin='mysql_native_password')
    print(con)
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS Amaz;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        query = "CREATE TABLE if not exists Amaz(title VARCHAR(255),title_url VARCHAR(300),zgbadgete VARCHAR(10),aiconrow VARCHAR(300),airconat VARCHAR(300),price VARCHAR(100),field_1_text VARCHAR(500),Field_1_link VARCHAR(200),field_2_text VARCHAR(500),Field_2_link VARCHAR(200))"
        cursor.execute(query)
        print("Created ....")
        #query = 'create table if not exists user(userid int primary key, username varchar(200),phone varchar(12))'
        print("Table is created....")
        #loop through the data frame
        amazon_data = pd.read_csv('Amazon.csv', index_col=False, delimiter = ',')
        #print(amazon_data.head())
        for i,row in amazon_data.iterrows():
            #sql = "INSERT INTO Amaz(title,title_url,zgbadgete,aiconrow,airconat,price,field_1_text,Field_1_link,field_2_text,Field_2_link)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            sql = "insert into Amaz(title,title_url,zgbadgete,aiconrow,airconat,price,field_1_text,Field_1_link,field_2_text,Field_2_link)values({},'{}','{}')".format(title,title_url,zgbadgete,aiconrow,airconat,price,field_1_text,Field_1_link,field_2_text,Field_2_link)
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
        con.commit()
except Error as e:
    print("Error while connecting to MySQL", e)


#convert the sql file into csv
"""query='select * from Product'
data=pd.read_sql(query,con)
data.to_csv('result.sql')
con.close()"""
"""class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Queen#123',database='Students',auth_plugin='mysql_native_password')
        query = 'create table if not exists user(userid int primary key, username varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")
        cur = self.con.cursor()

    def insert_user(self,userid, username, phone):
        query = "insert into user(userid,username,phone)values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User ID: ", row[0])
            print("User Name: ", row[1])
            print("Phone: ", row[2])
            print()
            print()
helper = DBHelper()
helper.fetch_all()"""
"""helper.insert_user(124,'s','1234567891')
helper.insert_user(125,'a','1234567891')
helper.insert_user(126,'u','1234567891')
helper.insert_user(127,'y','1234567891')
helper.insert_user(128,'f','1234567891')
helper.insert_user(129,'g','1234567891')
helper.insert_user(132,'r','1234567891')
helper.insert_user(133,'y','1234567891')
helper.insert_user(134,'e','1234567891')
helper.insert_user(135,'i','1234567891')
helper.insert_user(136,'m','1234567891')
helper.insert_user(137,'n','1234567891')"""

