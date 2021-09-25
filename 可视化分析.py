import pandas as pd
import pyecharts as pe
from scipy.misc import imread
data = pd.read_excel(r"C:\Users\DaiSimon\Desktop\数据分析\某站数据\b站罗翔童话镇数据.xlsx")
#加载数据
df = data.copy()
#为了防止原数据被破坏，操作之前备份
df = df.sort_values(by = '点赞数',ascending = False)
#按照点赞数进行排序，然后筛选前20条数据
df_top20 = df.iloc[:20]
x = df_top20['评论']
#作为x轴
y = df_top20['点赞数']
#作为y轴
#使用的是0.5.11版本
bar = pe.Bar('童话镇评论数据分析')
bar.add('评论Top20', x, y, is_datazoom_show = True,
        datazoom_range = [0,100], mark_line=[ "average"],
        tooltip_axispointer_type = 'cross')
bar.render('1.html')

import jieba

# 导入jieba库
comment_str_all = ''
for comment in df['评论']:
    comment_str_all += comment
comment_str_all = comment_str_all.replace('卢本伟', 'lbw')
# 把comment中的数据全部拼接成为字符串，然后在替换重复的数据

seg_list = jieba.lcut(comment_str_all)
# 中文分词
keyword_count = pd.Series(seg_list)
# keyword_count.str.len()
# 这里是查看切割数据后不同长度的情况

keyword_count = keyword_count[keyword_count.str.len() > 1]
# 剔除数据长度为1的数据
keyword_count.value_counts()
# 进行数据排序，这一步就是为了下一步设置filter_words做的准备

filter_words = ['回复', '不是', '什么', '真的', '就是', '这么', '那么', '怎么', '现在', '是的', '这个', '那个', '这种', '时候',
                '什么', '这部', '没有', '还有', '觉得', '什么', '就是', '没有', '一个', '不是', '还是', '最后', '我们', '但是',
                '因为', '真的', '还是', '现在 ', '可能', '可以', '只是', '其实', '所以', '这样', '也许', '一直', '第一', '为了', '它们',
                '看到', '看过', '自己', '不会', '一下', '然后', '真有', '他们', '已经']
keyword_count = keyword_count[~keyword_count.str.contains('|'.join(filter_words))]
# 排除filters_word里面的数据
keyword_count = keyword_count.value_counts()[:100]
# 选择前100个重要的词汇进行词云展示
wd = pe.WordCloud("关键词汇挖掘-词云图")
# 提取每个词
words = keyword_count.index.tolist()
# 提取每个词的词频
words_counts = keyword_count.values.tolist()
# 绘制图表
wd.add("词频", words, words_counts, shape='star',
       word_size_range=[20, 100], rotate_step=10)
# 生成图表
wd.render('2.html')

df_shuijun = df[['用户名','评论']].groupby(by = '用户名').count().sort_values(by = '评论',ascending = False)
#进行分组计数，然后按照从大到小的顺序进行排列
#df[df['member'].str.contains('华洛丽桑卓')]
#这个是用来查找包含某个内容的原始数据
len(df_shuijun[df_shuijun['评论'] >= 10])
#查看一下动态超过10条的数据量，也就是下面61的依据

shuijun_data_over_10 = df_shuijun.iloc[:61]
x = shuijun_data_over_10.index.tolist()
y = shuijun_data_over_10['评论'].tolist()
#设置x，y数据
bar = pe.Bar('水军数据排行榜')
bar.add('动态数据大于10条的排名信息', x, y, is_datazoom_show = True,
        datazoom_range = [0,100], mark_line=[ "average"],
        tooltip_axispointer_type = 'cross')
bar.render('3.html')
