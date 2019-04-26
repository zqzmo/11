import requests
import time
from lxml import etree


url = 'https://book.douban.com/top250'
data = requests.get(url).text
s = etree.HTML(data)

file = s.xpath('//*[@id="content"]/div/div[1]/div/table')

for div in file:
    title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
    score = div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
    num = div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")")
    scribe = div.xpath("./tr/td[2]/p[2]/span/text()")

    time.sleep(2)

    print("{}{}{}{}".format(title,  score, num, scribe[0]))