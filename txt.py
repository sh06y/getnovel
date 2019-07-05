from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

urlx = 'http://www.aouchina.com/shu/6/'

def get(url):
    html = urlopen(url)  # 发出请求并且接收返回文本对象
    # html = response.read()  # 调用read()进行读取
    soup = BeautifulSoup(html,features="lxml")
    title = soup.h1
    txt = soup.findAll(id="content")
    txt = re.sub('<br/><br/>    ', '\n', str(txt))
    txt = re.sub('[][divid="content"</>]', '', str(txt))
    title = re.sub('[</h1>]','',str(title))
    novel = title + '\n' + txt
    return novel

def save():
    f=open("novel.txt","a+",encoding='utf-8')
    f.write(novel)
    f.close()

novel = ''

for i in range(2829,2879):#2879
    print("正在保存",urlx + str(i) + '.html')
    # novel = novel + get(urlx + str(i) + '.html')
    novel = get(urlx + str(i) + '.html')
    save()