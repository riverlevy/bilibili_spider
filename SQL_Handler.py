import mysql.connector
#table struct
#id link from name type size data uploaded 
#table create command create table if not exists bilibili(id int unsigned auto_increment primary key,link text not null,name text not null,type char(5) not null,size int unsigned not null,datetime datetime not null,uploaded boolean) charset=utf8;
class SQLHandler():
    def __init__(self):
        self.cur=None
        self.conn=None
        self.__create_conn()
    def __del__(self):
            self.conn.commit()
            self.conn.close()
    def __create_conn(self):
        self.conn=mysql.connector.connect(
            user="reptile",
            password="123456",
            host='192.168.56.102',
            database="VideoData")
        self.cur=self.conn.cursor()
