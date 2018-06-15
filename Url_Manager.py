import SQL_Handler
import Words_Fliter
class Url_Manager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    def complete_url(self,url):
        if not (url.startswith("http://") or url.startswith("https://")) and url.startswith("//"):
            url="http:"+url
        elif not url.startswith("http:") or not url.startswith("https:"):
            url="http://"+url
        return url
    def clean(self,url_title):
        sql_handler=SQL_Handler.SQLHandler()
        dict_delete={}
        fliter=Words_Fliter.WordsFliter()
        words_list=fliter.getWords()
        for k,v in url_title.items():
            for word in words_list:
                if k.find(word)>=0:
                    dict_delete[k]=None
            sql_command="select count(*) from bilibili where link=%s or name=%s;"
            sql_handler.cur.execute(sql_command,(self.complete_url(k),v))
            if not sql_handler.cur.fetchall()[0][0] == 0:
                dict_delete[k]=None
        for key in dict_delete.keys():
            del url_title[key]
        return url_title
    # def add_new_url(self,url):
    #     if url  is None:
    #         return
    #     if url not in self.old_urls and url not in self.new_urls:
            # self.new_urls.add(url)
            # 
    # def has_new_url(self,url):
    #     return len(self.new_urls)!=0

    # def get_new_url(self,url):
    #     new_url=self.new_urls.pop()
    #     self.old_urls.add(new_url)
    #     return new_url

    # def add_new_urls(self,urls):
    #     if urls is None or len(urls)==0:
    #         return
    #     for url in urls:
    #         self.add_new_url(url)
    # def save_url(self,url):
    #     return None
    #     #to do with sql
    # def save_urls(self,urls):
    #     for url in urls:
    #         self.save_url(url)
    # def save_all(self):
    #     self.save_urls(self.new_urls)
    #     self.save_urls(self.old_urls)
    # def contain(self,url):
    #     # for item in new_urls:
    #     #     if item==url:
    #     #         return True
    #     for item in self.old_urls:
    #         if item==url:
    #             return True
    #     #to to with sql
    #     return False
