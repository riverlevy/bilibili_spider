import os
import time
class GetFileInfo():
    def __init__(self,path,title):
        self.full_name=None
        self.full_path=None
        files=os.listdir(path)
        for file in files:
            if file.find(title)>=0:
                if file.split(".")[-1]=="xml" or file.split(".")[-1]=="cmt":
                    os.remove(path+os.path.sep+file)
                elif file.split(".")[-1]=="flv":
                    exp=file.split(".")[-1]
                    os.rename(path+os.path.sep+file,path+os.path.sep+title+"."+exp)
                    self.full_name=title+"."+exp
                    self.full_path=path+os.path.sep+self.full_name
                    print(self.full_path)
                    break
    def get_format_info(self):
        info={}
        if self.full_path==None:
            return info
        #link,name,format,size,datetime,uploaded
        info["format"]=self.full_name.split(".")[1]
        info["size"]=os.path.getsize(self.full_path)
        st=time.localtime(os.path.getctime(self.full_path))
        info["datetime"]= time.strftime("%Y-%m-%d %H:%M:%S",st)
        info["full_path"]=self.full_path
        #info["datetime"]= time.strftime("%Y-%m-%d %H:%M:%S",os.path.getctime(self.full_path))
        return info
