import subprocess
import os
import SQL_Handler
class UpLoad_Video(object):
    def upload_to_youtube(self,sql_handler,full_path,title):
        print("start upload:%s"%title)
        command_str='''python ../youtube-upload-master\\bin\\youtube-upload --client-secrets=../youtube-upload-master\\client_secret.json --title="%s" "%s"'''%(title,full_path)
        try:
            upload_file=subprocess.call(command_str, stdout=subprocess.PIPE)
        except:
            print("Upload Fail:\t"+title)
            return
        if upload_file==0:
            print("Upload Success:\t"+title)
            sql_command="update bilibili set uploaded=%s where name=%s;"
            sql_handler.cur.execute(sql_command,(1,title))
            sql_handler.conn.commit()

