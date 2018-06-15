import os
import time
import threading
import Url_Manager
import subprocess
import UpLoad_Videos
import Get_File_Info
import SQL_Handler

class DownloadVideos(object):
    def __init__(self,thread_num):
        self.max_threads=thread_num
        self.threads_num=0
        self.url_manager=Url_Manager.Url_Manager()

    def download_single_video(self,url,title,path,other_command,upload_now):
        thread_name=threading.current_thread().getName()
        print("Tread:%s start download:%s"%(thread_name,title))
        try:
            #make url
            url=self.url_manager.complete_url(url) 
            sql_handler=SQL_Handler.SQLHandler()
            # subprocess.run("you-get -o "+path+" "+url,stdout=subprocess.PIPE)
            os.system('''you-get -o "%s" %s "%s" '''%(path,other_command,url))
            # i have attempted following,but the speed is tooooooooooo low
            
            # downloaded=subprocess.call('''you-get -o "%s" %s "%s" '''%(path,other_command,url),stdout=subprocess.PIPE)
            # if downloaded==0:
            #     print("Thread:%s Download Success:\t%s"%(thread_name,title))
            # else:
            #     print("Thread:%s\t Download Fail:\t%s"%(thread_name,title))
            #     self.threads_num=self.threads_num-1
            #     return False

            # a easy way to get title
            f_info=Get_File_Info.GetFileInfo(path,title).get_format_info()
            if f_info=={}:
                print("未查询到文件信息：%s"%title)
                self.threads_num=self.threads_num-1
                return 
            sql_command="insert into bilibili(link,name,format,size,datetime,uploaded) values(%s,%s,%s,%s,%s,%s);"
            sql_handler.cur.execute(sql_command,(url,title,f_info["format"],f_info["size"],f_info["datetime"],0))
            sql_handler.conn.commit()
            if upload_now==True:
                # print("starting upload...")
                upload_videos=UpLoad_Videos.UpLoad_Video()
                upload_videos.upload_to_youtube(sql_handler,f_info["full_path"],title)
        except:
            self.threads_num=self.threads_num-1
            return False
        else:
            self.threads_num=self.threads_num-1
            return True

    def download_multipule_videos(self,url_title,path,other_command,upload_now):
        print("开始下载：")
        for url,title in url_title.items():
            while self.threads_num>=self.max_threads:
                time.sleep(1)
            try:
                self.threads_num=self.threads_num+1
                t=threading.Thread(target=self.download_single_video,name="%s"%(self.threads_num),args=(url,title,path,other_command,upload_now))
                t.start()
            except:
                self.threads_num=self.threads_num-1
                print("Download Error")
        return True



