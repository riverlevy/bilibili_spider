import os
import SQL_Handler
import UpLoad_Videos
class Upload_Unloaded():
    def __init__(self,path):
        self.sql_handler=SQL_Handler.SQLHandler()
        self.uploader=UpLoad_Videos.UpLoad_Video()
        self.sql_handler.cur.execute("select name,format from bilibili where uploaded=0")
        for one in self.sql_handler.cur.fetchall():
            new_path=path+os.path.sep+one[0]+"."+one[1]
            if os.path.exists(new_path):
                self.uploader.upload_to_youtube(self.sql_handler,new_path,one[0])
#Upload_Unloaded("E:\\Code\\Python\\bilibili_spider\\videos")

