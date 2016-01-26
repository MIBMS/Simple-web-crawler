from urllib import request as req
from bs4 import BeautifulSoup

url = input('Enter URL: ')

m = int(input('Enter the position of the link you want to follow on each page (1st link is 1 and so on): '))

n = int(input('How many times do you want to follow the link at position %s? ' % m))

def process_url(url):
    html = req.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    anchors = soup('a')

    return anchors[m-1].get('href')




for i in range(n):
    url = process_url(url)


html = req.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(str(soup.title.contents[0]).split()[2])
