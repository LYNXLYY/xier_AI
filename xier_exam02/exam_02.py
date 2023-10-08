import requests
import json
import pymysql
from lxml import etree


# 02是福州大学
# 021,022是读取福州大学的通知人，日期，附件下载次数，并且处理、画图,结果是：注册中心,教改办,实践科，教研教改的下载次数较多(发的也多),大部分通知的周期都是5天
# 03是历史上的今天


if __name__ == "__main__":
    db = pymysql.connect(
        host="localhost", user="root", password="abc123", database="fzuxier"
    )

    cur = db.cursor()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }
    for pageNum in range(180, 183):
        url = f"https://jwch.fzu.edu.cn/jxtz/{pageNum}.htm"
        page_text = requests.get(
            url=url,
            headers=headers,
        ).content

        # 数据解析
        tree = etree.HTML(page_text)
        # 里标签对象
        li_list = tree.xpath('//ul[@class="list-gl"]/li')

        fp = open("fuzhou.txt", "w", encoding="utf-8")

        for li in li_list:
            date = li.xpath("span/text()")[0]
            if date == " ":
                continue
            type = li.xpath("span/text()/following::text()")[0]
            title = li.xpath("a/text()")[0]
            link = "https://jwch.fzu.edu.cn/" + li.xpath("a/@href")[0]
            print(date)
            print(type)
            print(title)
            print(link)
            print()
            sql = (
                "INSERT INTO exam01(notifier,title, date, link)VALUES ('%s','%s','%s','%s');"
                % (type, title, date, link)
            )

            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("数据插入成功")

            page_text1 = requests.get(
                url=str(link),
                headers=headers,
            ).content
            # 数据解析
            tree1 = etree.HTML(page_text1)
            # 里标签对象
            li_list1 = tree1.xpath('//ul[@style="list-style-type:none;"]/li')

            for li in li_list1:

                second = li.xpath("a/text()")[0]
                link1 = "https://jwch.fzu.edu.cn" + li.xpath("a/@href")[0]
                down1 = li.xpath("span/@id")[0][7:]

                print(second)
                print(link1)
                url2 = f"https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={down1}&owner=1744984858&type=wbnewsfile&randomid=nattach"
                response = requests.get(url=url2, headers=headers).content
                data = json.loads(str(response.decode()))
                number = data.get("wbshowtimes")
                print("下载次数是" + str(number))

            print()
            print("*****************************************")
