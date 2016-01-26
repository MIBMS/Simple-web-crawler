from bs4 import BeautifulSoup
from urllib import request as req

url = input('Enter URL: ')
html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')

sum_of_values = 0
for span in spans:
    num = span.contents[0]
    num = int(num)
    sum_of_values += num

print(sum_of_values)
