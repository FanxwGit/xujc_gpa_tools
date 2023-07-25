from regex import P
import requests as res
from bs4 import BeautifulSoup as bs


# configs
cookies = {
    'PHPSESSID': 'na28epngm0e29cpjvqv5p7nvi4',
}
# 需要删除的课程
dele = ['马克思主义基本原理', '西方音乐赏析', '体育俱乐部', '数字逻辑(B)', 'Windows服务器安装与配置']

# 不需要修改
headers = {
    'Proxy-Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'null',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Referer': 'http://jw.xujc.com/student/index.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
}

# 北大算法
def f(point):
    if point >= 90:
        return 4.0
    elif point >= 85:
        return 3.7
    elif point >= 82:
        return 3.3
    elif point >= 78:
        return 3.0
    elif point >= 75:
        return 2.7
    elif point >= 72:
        return 2.3
    elif point >= 68:
        return 2.0
    elif point >= 64:
        return 1.5
    elif point >= 60:
        return 1.0


total_score = 0
total_point = 0
for i in range(2019, 2022):
    for j in range(1, 3):
        id = str(i) + str(j)
        re = res.get(
            "http://jw.xujc.com/student/index.php?c=Search&a=cj&tm_id="+id, headers=headers, cookies=cookies)
        bs_html = bs(re.text, 'lxml')
        ls = bs_html.find("tbody").find_all("tr")
        for item in ls:
            # 1课程名 2学分 3成绩
            name = item.find_all("td")[1].string
            point = item.find_all("td")[2].string
            score = item.find_all("td")[3].string
            point = eval(point)
            score = eval(score)
            if score >= 60 and point != 0 and name not in dele:
                print(name, point, score)
                total_point += point
                total_score += score*point

gpa = total_score/total_point
print(gpa)
