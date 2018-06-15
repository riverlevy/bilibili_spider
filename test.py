import Bilibili_Ranking_Html_Parser
import Html_Downloader
import os
import subprocess
import time
import mysql.connector
import Html_Downloader
import Bilibili_Ranking_Html_Parser
import Upload_Unloaded
import Words_Fliter
words=Words_Fliter.WordsFliter.getWords()
print(words)
print('papi酱'==words[0])
# up=Upload_Unloaded.Upload_Unloaded('''E:\\Code\\Python\\bilibili_spider\\videos''');



# # s=subprocess.call("you-get -o E:\Videos\python-download %s"%('''http://www.bilibili.com/video/av1018798?from=search&seid=17955504789419019815'''),stdout=subprocess.PIPE)
# # print(s)
# # html_parser=Bilibili_Ranking_Html_Parser.Bilibili_Ranking_Html_Parser()
# # html_downloader=Html_Downloader.HtmlDownloader()
# # url_title=html_parser.parse_from_html(.download('''https://www.bilibili.com/ranking'''))
# # for k,v in url_title.items():
# #     print(k)
# class a():
#     # def __init__(self):
#     #     self.conn=None
#     #     self.cur=None
#     def con(self):
# self.conn=mysql.connector.connect(
#     user="reptile",
#     password="123456",
#     host='192.168.56.102',
#     database="VideoData")
# self.cur=self.conn.cursor()
#     def clean(self):
#         self.cur.close()
#         self.cur=self.conn.cursor()
#     def close(self):
#         self.conn.close()
#         self.con()

# conn=mysql.connector.connect(
#     user="reptile",
#     password="123456",
#     host='192.168.56.102',
#     database="VideoData")
# cur=conn.cursor()
# cur.execute("select name from bilibili where name regexp '^-!---';")
# s=""
# for name in cur.fetchall():
#     print(name)
#     s=s+'''update bilibili set name="%s" where name="%s";'''%(name[0][13:-7],name[0])
# cur.close();
# print(s)
# cur=conn.cursor()
# cur.execute(s)
# conn.commit()
# aa.con()
# aa=a()
# aa.con()
# aa.cur.execute("select name from bilibili where name regexp '^-!---';")
# s=""
# for name in aa.cur.fetchall():
#     s=s+'''update bilibili set name="%s" where name="%s";'''%(name[13:-7],name)
# aa.close()
# aa.cur.execute(s)
# aa.conn.commit()
# # cur.execute("select name from bilibili")
# # for i in cur.fetchall():
# #     print(i)
# # cur.nextset()
# # cur.close()
# # conn.commit()
# # conn.close()
# # html_downloader=Html_Downloader.HtmlDownloader()
# # html_praser=Bilibili_Ranking_Html_Parser.Bilibili_Ranking_Html_Parser()
# # url_title=html_praser.parse_from_html(html_downloader.download('''https://www.bilibili.com/ranking'''))



# path='''E:\\Code\\Python\\bilibili_spider\\videos'''
# files=os.listdir(path)
# title="【咬人猫】激昂壮志"
# for file in files:
#     if file.find(title)>=0:
#         if file.split(".")[-1]=="xml" or file.split(".")[-1]=="cmt":
#             os.remove(path+os.path.sep+file)
#         elif file.split(".")[-1]=="flv":
#             exp=file.split(".")[-1]
#             os.rename(path+os.path.sep+file,path+os.path.sep+title+"."+exp)
#             full_name=title+"."+exp
#             full_path=path+os.path.sep+full_name
#             print(full_path)
#             break


# files=os.listdir(path)
# for file in files:
#     if not os.path.isdir(file):
#         cmd='''python ../youtube-upload-master\\bin\youtube-upload --client-secrets=../youtube-upload-master\client_secret.json --title="%s" "%s"'''%(file.split(".")[0],path+"\\"+file)
#         os.system(cmd);



#         # if file.split(".")[-1]!="flv":
#             # os.remove("E:\\Code\\Python\\bilibili_spider\\videos\\"+file)
#         if file.split(".")[0][0]=='-':
#             new_name=file.split(".")[0][1:]+".flv";#+file.split(".")[0][0:-8]+".flv"
#             # print(new_name)
#             os.rename('E:\\Code\\Python\\bilibili_spider\\videos\\'+file,'E:\\Code\\Python\\bilibili_spider\\videos\\'+new_name)

        # if file.endswith("flv"):
        # if file.find(".cmt")>=0:
        #     os.remove(path+os.path.sep+file)
        # elif file.startswith("-!------span-"):
        #     os.rename(path+os.path.sep+file,path+os.path.sep+file.split(".")[0][13:-7]+"."+file.split(".")[-1])

            # command_str='''python ../youtube-upload-master\\bin\youtube-upload --client-secrets=../youtube-upload-master\client_secret.json --title="'''+file.split(".")[0]+'''" "'''+path+os.sep+file+'"'
            # res=subprocess.run(command_str,stdout=subprocess.PIPE)
            # res_t=res.stdout.decode("UTF-8")
# #             # os.rename(path+os.path.sep+file,path+os.path.sep+file[:-4]+"."+file[-3:-1])
# #             os.rename(path+os.path.sep+file,path+os.path.sep+file+"v")
# #     print(file)
#         # if file.endswith(".xml") or file.endswith(".download"):
#         #     os.remove(path+os.sep+file)
#         # else:
# cur.execute("insert into bilibili(link,name,format,size,datetime,uploaded) values('%s','%s','%s',%d,'%s',%d);"%(website,file.split(".")[0],info["format"],info["size"],info["datetime"],0))
# conn.commit()
# cur.execute("select count(*) from bilibili")
# print(cur.fetchall()[0][0])
# #         #     print(res_t)
# website="http://www.bilibili.com"
# for k,v in url_title.items():
#     if v==file.split(".")[0]:
#         website="http:"+k
#         info={}
#         info["format"]=os.path.splitext(path+os.sep+file)[1][1:]
#         info["size"]=os.path.getsize(path+os.sep+file)
#         st=time.localtime(os.path.getctime(path+os.sep+file))
#         info["datetime"]= time.strftime("%Y-%m-%d %H:%M:%S",st)


