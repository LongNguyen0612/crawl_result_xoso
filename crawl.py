"""
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]

Các thư viện:

- requests
- requests_html hay beautifulsoup4 [tuỳ chọn]
- argparse hay sys.argv

Gợi ý:

- ``nargs`` https://docs.python.org/2/library/argparse.html
"""

import requests
from bs4 import BeautifulSoup
import bs4
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number",help="dau vao",type=str)
args = parser.parse_args()

url = "http://ketqua.net/"

def get_result():
    result = []
    response = requests.get(url)
    tree = bs4.BeautifulSoup(response.text,"html.parser")
    for element in tree.find_all("td"):
        if 'data-pattern' in str(element):
            result.append(element.text)
    result.pop(0)
    return result


def get_2digits_result():
    result_2digits = []
    for data in get_result():
        result_2digits.append(data[-2:])
    return result_2digits[-8:]


def check_result(number):
    list_number = get_2digits_result()
    for data in list_number:
        if number in data:
            return 'you have won a price with the number:{}'.format(number)
        else:
            return list_number


def main():
    number = args.number
    print(check_result(number))

if __name__ == "__main__":
    main()