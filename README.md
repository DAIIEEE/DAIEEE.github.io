# DAIEEE.github.io
#### python 3.7.3
#### request
#### bs4
### 一、B站视频评论数据爬取
-
童话镇评论数据：[Link](https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=585787515&sort=2&pn=)用的是ver1.0

获取了对应的文件.xlsx，对于评论爬取ver2.0.py文件，所爬文件大小 limit 2.56MB

评论爬取ver2.0修改了输出txt的数据布置形式，便于数据提取

`headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }`修改header信息

`url = "https://api.bilibili.com/x/v2/reply?pn=" + str(page) + "&type=1&**oid=759395091**&sort=2"`此处的oid及对应b站改版前的av号，此处的oid是何同学的视频

### 二、可视化
#### pyecharts 0.1.9.4
#### jieba
#### pandas

-![童话镇评论数据分析](https://user-images.githubusercontent.com/78712551/134761227-91f3357a-304c-450f-9e75-6961cbb38f13.png)

对top20评论进行获取

![童话镇词云](https://user-images.githubusercontent.com/78712551/134761272-9f4b1fef-1d7f-457d-8b13-9429cceeae98.png)

（1） 对于罗翔老师的视频，张三这个词必定会出现

（2） 立意、真相、大哭，内容方面可以看出整个视频的基调是悲伤的

（3） 媒体、报道、知道、真相等词基本上能够看出是网络舆论影响力的

![水军数据排行榜](https://user-images.githubusercontent.com/78712551/134763516-fc052e2a-610f-4b8d-96e2-8710391c137c.png)

查看评论数大于10条的用户

### 三、复刻tableau社区作品
![image](https://user-images.githubusercontent.com/78712551/134800553-aeaf4551-42ae-42ff-8c3e-5a46fa3e7b1a.png)

![image](https://user-images.githubusercontent.com/78712551/134800582-60026f09-5b48-4ccc-8ce5-f41bf35e0201.png)

### 四、客户价值分析RMF模型（python和tableau）

数据来源和鲸社区
![下载](https://user-images.githubusercontent.com/78712551/152515338-7792b6f0-547b-4f88-8f1c-4ef77305d11b.png)

+- Bulleted
+- List
+1. Numbered
+2. List
+**Bold** and _Italic_ and `Code` text
+[Link](url) and ![Image](src)
+```
+For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
