# bilibili_spider




本项目为搬运小恶魔小组的python作业。

这个是我们做项目初始目标：

爬取国内部分视频网站和音频网站的资源，并将资源进行下载（暂定为Bilibili，如果有精力还会爬取荔枝FM等网站的资源），	将下载的资源上传到YouTube

各个文件大概文件名大概就是功能了🙄，然而有着表述不清，将就着看吧😅。



实现的过程：

step1：爬取哔哩哔哩的视频信息，统一为url，title的格式并且保存到字典。

step2：从数据库搜索相应的url看看是否已经下载，如果已经存在就就从字典中删除。

step3：从字典的title中搜索关键词，存在则删除。

step4：设置多线程，子线程调用you-get的轮子进行下载🙄。you-get这个轮子并不是太好，最后的文件名有出入，所以找到相应文件并且重命名为title。

step5：文件下载好之后检索相应信息，用MySQL进行做简单的数据库的处理存储。

step6：将文件信息提取出来，调用youtube-upload这个轮子上传到youtobe上面去。


用到的大轮子：

you-get：https://github.com/soimort/you-get

具体使用方法可见you-get的README文件🙄（好啦好啦，为了照顾英语不好的同学，我翻译一下，翻译过来文件的名字就是“读我”）

youtube-uoload：https://github.com/tokland/youtube-upload

“读我”文件我就不翻译了🤭

啦啦啦啦啦啊，我们的那个古狗账号是zhaohaha362@gmail.com，密码是**********

啦啦啦啦啦~~~~~

附上：

我们小组三个成员：

李昌河，程治语，赵业伟

学号，20172106**

学校：北京邮电大学

分工：

李昌河：主要负责爬虫爬取网页，获得必要信息

程治语：主要负责数据的整理和数据库相关操作

赵业伟：端茶倒水，，咳咳。明确需求，指定步骤，测试代码，找轮子。并且将小组所写的代码进行整合与测试。将可以并发的处理的步骤多线程执行，优化代码提高运行效率。

贡献上面，三人分别就分工做出了相对应的贡献。
