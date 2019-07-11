from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

urlx = 'http://www.aouchina.com/shu/6/'
f = open("novel.txt","a+",encoding='utf-8')

# 获取小说内容部分
def get(url):
    html = urlopen(url) # 打开链接
    soup = BeautifulSoup(html,features="lxml") # 用BeautifulSoup对上一步获取到的网页进行解析
    title = soup.h1 # 提取小说章节标题
    txt = soup.findAll(id="content") # 查找正文
    # 去掉其中无用的文本
    txt = re.sub('<br/><br/>    ', '\n', str(txt))
    txt = re.sub('[][divid="content"</>]', '', str(txt))
    title = re.sub('[</h1>]','',str(title))
    # 将标题与正文进行合并
    novel = title + '\n' + txt
    return novel # 返回小说内容

# 保存部分
def save():
    f.write(novel)

novel = ''

# 开始爬
for i in range(2829,2880):
    print("正在保存",urlx + str(i) + '.html')
    novel = get(urlx + str(i) + '.html')
    save()

f.close() # 关闭文件