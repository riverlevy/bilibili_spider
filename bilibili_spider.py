#encoding=utf-8
import requests
import Html_Downloader
import Url_Manager
import DownloadVideos
import Bilibili_Ranking_Html_Parser
import Upload_Unloaded
import subprocess

download_path="E:\\code\\python\\bilibili_spider\\videos"

upload_now=subprocess.call("ping  www.youtube.com",subprocess.PIPE)
if upload_now==0:
    upload_now=True
else:
    upload_now=False
# Upload those unloaded
upload_now=True

Upload_Unloaded.Upload_Unloaded(download_path)
#url to reptile
bilibili_rank_url='''https://www.bilibili.com/ranking'''

#download page and parse page objects
html_downloader=Html_Downloader.HtmlDownloader()
html_praser=Bilibili_Ranking_Html_Parser.Bilibili_Ranking_Html_Parser()

#parse page
url_title=html_praser.parse_from_html(html_downloader.download(bilibili_rank_url))
url_manager=Url_Manager.Url_Manager()
url_title=url_manager.clean(url_title)
# for k,v in url_title.items():
#     print(v)

#set thread numbers
# print("create download objects")
download_videos=DownloadVideos.DownloadVideos(1)
download_videos.download_multipule_videos(url_title,download_path,"",upload_now)
# print("over")
