import urllib2
from bs4 import BeautifulSoup

website = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)').read()
# print website

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
soup = BeautifulSoup(website, 'html.parser')
# print (soup.prettify())
# print soup.title.string
# print soup.h1.span.string
# print soup.h2.span.string
# for link in soup.find_all('a'):
#     print (link.get('href'))

# Extract all text from a web page
# print(soup.get_text())

for link in soup.find_all('a'):
    print ("===============")
    print (link.string)
    print (link.get('href'))
    print ("===============")
    print (" ")
