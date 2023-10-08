import requests
import json
import re
import pymysql

if __name__ == "__main__":
    db = pymysql.connect(
        host="localhost", user="root", password="abc123", database="fzuxier"
    )

    cur = db.cursor()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }
    for t in range(1, 13):

        if t < 10:
            t1 = "0" + str(t)
        else:
            t1 = str(t)
        url = f"https://baike.baidu.com/cms/home/eventsOnHistory/{t1}.json?_=1696661583910"

        page_text = requests.get(url=url, headers=headers).text
        data = json.loads(page_text)
        data1 = data[f"{t1}"]

        for da in range(1, 32):
            try:

                if da < 10:
                    da1 = "0" + str(da)
                else:
                    da1 = str(da)
                tx = t1 + da1
                print("**********************************************")
                print("这是" + t1 + "月" + da1 + "日")
                data2 = data1[f"{tx}"]
                for i in data2:
                    year = i["year"]
                    print(year)

                    title1 = re.sub(r"<[^>]*>", "", i["title"])
                    print(title1)

                    ty = i["type"]
                    print(ty)

                    desc1 = re.sub(r"<[^>]*>", "", i["desc"])
                    print(desc1 + "...")

                    print("********************************************")
                    print()
                    sql = (
                        "INSERT INTO exam02(today, date,title,type,contant)VALUES ('%s','%s','%s','%s','%s');"
                        % (tx, year, title1, ty, desc1)
                    )
                    # 执行sql语句
                    cur.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                    print("数据插入成功")
            except:
                print("没有" + t1 + "月" + da1 + "日的信息")
