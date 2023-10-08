import requests
import json
import pymysql
from lxml import etree
import re
import csv

if __name__ == "__main__":
    list1 = [[]]
    lista = ["type", "date", "download"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }
    x = 0
    for pageNum in range(153, 183):

        url = f"https://jwch.fzu.edu.cn/jxtz/{pageNum}.htm"
        page_text = requests.get(
            url=url,
            headers=headers,
        ).content

        # 数据解析
        tree = etree.HTML(page_text)
        # 里标签对象
        li_list = tree.xpath('//ul[@class="list-gl"]/li')

        for li in li_list:
            list1.append([])
            date = li.xpath("span/text()")[0]
            if date == " ":
                continue
            type = li.xpath("span/text()/following::text()")[0]
            title = li.xpath("a/text()")[0]
            link = "https://jwch.fzu.edu.cn/" + li.xpath("a/@href")[0]
            date1 = date[10:]
            if date1[0] == 0:
                date2 = int(date1[1])
            else:
                date2 = int(date1)
            print(date2)

            res = re.findall("[\u4e00-\u9fa5]", type)
            type1 = ""
            for i in res:
                type1 += i

            print(type1)

            page_text1 = requests.get(
                url=str(link),
                headers=headers,
            ).content
            # 数据解析
            tree1 = etree.HTML(page_text1)
            # 里标签对象
            li_list1 = tree1.xpath('//ul[@style="list-style-type:none;"]/li')
            tot = 0

            for li in li_list1:

                second = li.xpath("a/text()")[0]
                link1 = "https://jwch.fzu.edu.cn" + li.xpath("a/@href")[0]
                down1 = li.xpath("span/@id")[0][7:]

                url2 = f"https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={down1}&owner=1744984858&type=wbnewsfile&randomid=nattach"
                response = requests.get(url=url2, headers=headers).content
                data = json.loads(str(response.decode()))
                number = data.get("wbshowtimes")
                tot += number

            print("下载总次数是" + str(tot))

            list1[x].append(type1)
            list1[x].append(date2)
            list1[x].append(tot)
            x = x + 1

            print()
            print("*****************************************")
    print(list1)

with open("example.csv", "w", encoding="UTF8") as file:
    writer = csv.writer(file)
    writer.writerow(lista)
    writer.writerows(list1)
