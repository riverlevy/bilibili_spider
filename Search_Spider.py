import requests
import http.cookiejar
from bs4 import BeautifulSoup as BS
import re
import lxml
import urllib
import time
class SearchSpider(object):
  def search():
    res={}
    header={
       "Accept":"text/html, application/xhtml+xml, image/jxr, */*",
       "Accept-Encoding": "gzip, deflate,br",
       "Accept-Language": "zh-CN",
       "Connection": "Keep-Alive",
       "Host":"search.bilibili.com",
       "Cookie":"LIVE_BUVID=AUTO6415241132292796; fts=1524113240; buvid3=88073770-A271-4417-A7B4-01D1C8942A3720802infoc; sid=7yu0i1co; im_notify_type_40057704=0; pgv_pvi=1666568192; UM_distinctid=16329f26e3ab5-0bb6bf90ed8a92-4323461-149c48-16329f26e3b20d; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1525102263,1525157391,1525412027,1525417367; finger=edc6ecda",
       # "Referer":"cn.bing.com",
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
    }
    # search_word="赵同学"
    search_word=input("搜索啥呢？\n")
    pages=input("搜几页？\n")
    bilibili_session=requests.Session()
    bilibili_session.cookies=http.cookiejar.LWPCookieJar(filename='search_cookie')
    try:
        bilibili_session.cookies.load(ignore_discard=True)
    except:
        pass
    # search_word=input("Search Word:")

    # bilibili_session.cookies={
    #     "buvid3":"AB4F5027-236C-4A82-AE2F-25FC8308538028016infoc",
    #     "finger":"ee9500f4", 
    #     "LIVE_BUVID":"AUTO8015255207487580", 
    #     "fts":"1525531711",
    #     "_dfcaptcha":"3c91632e3dfb3b0503ca332a58f1fc09"
    # }
    # bilibili_session.cookies="buvid3=AB4F5027-236C-4A82-AE2F-25FC8308538028016infoc; finger=ee9500f4; LIVE_BUVID=AUTO8015255207487580; fts=1525531711; _dfcaptcha=3c91632e3dfb3b0503ca332a58f1fc09"
    for page in range(1,int(pages)+1):
      data={
          "keyword":search_word,
          "from_source":"banner_search",
      }
      if page>1:
        data['page']=page
      time.sleep(1)
      ds=urllib.parse.urlencode(data)
      bilibili_search_url="https://search.bilibili.com/all?"+ds
      print(bilibili_search_url)
      page=bilibili_session.get(bilibili_search_url,headers=header,)
      bilibili_session.cookies.save()
      html=page.text
      bs=BS(html,"lxml")
      video_li=bs.find_all("li",class_="video matrix")
      for li in video_li:
          a=li.find("a",class_="title")
          title=a['title']
          link=a['href']
          res[link]=title
      print(res)
    return res

SearchSpider.search()
          # print("%s %s"%(title,link))
      # sleep(1000)
    # bilibili_login_url='''https://passport.bilibili.com/login'''
    # bilibili_session=requests.Session()
    # bilibili_session.cookies=http.cookiejar.LWPCookieJar(filename=bilibili_cookies)
    # try:
    #     bilibili_session.cookies.load(ignore_discard=True)
    # except:
    #     bs=BS(bilibili_session.get(bilibili_login_url,headers=header).text,"lxml").find()
    #     data={
    #         'userid':'18538116893',
    #         'pwd':'1973187507zhao',
    #         'vcode':''
    #     }
    # response=bilibili_session.post(bilibili_login_url,data=data,headers=header)
    # bilibili_session.cookies.save()
    # r=bilibili_session.get("",timeout=20,headers=header)
    # reg=r'<input type="hidden" name="authenticity_token" value=.*/>'
    # pattern=re.compile(reg)
    # token=pattern.findall(r.text)[0]
    # my_data={
    #     "commit":"Sign in",
    #     "authenticity_token":token,
    # }
    # r=sss.post("http://www.github.com/session",headers=header,data=my_data)
    # print(r.status_code)

    # print(request.content.decode("utf-8"))
