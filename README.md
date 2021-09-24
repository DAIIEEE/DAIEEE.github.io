# DAIEEE.github.io
#### python 3.7.3
#### request
#### bs4
### 一、B站视频评论数据爬取
-
+童话镇评论数据：[Link](https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=585787515&sort=2&pn=)
+获取了对应的文件.xlsx，对于评论爬取.py文件，所爬文件大小 limit 2.56MB
+修改了输出txt的数据布置形式，便于数据提取


+'headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }'修改header信息
    
    
+'url = "https://api.bilibili.com/x/v2/reply?pn=" + str(page) + "&type=1&**oid=759395091**&sort=2"'此处的oid及对应b站改版前的av号
### 二、弹幕爬取及数据
-
-
### 三、可视化
-
-
-
-
-
### 四、情感分析
-
-
-
### 五、复刻tableau社区作品-
-
-
-
-
+- Bulleted
+- List
+1. Numbered
+2. List
+**Bold** and _Italic_ and `Code` text
+[Link](url) and ![Image](src)
+```
+For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
