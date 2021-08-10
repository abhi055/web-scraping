# If you want to scrap website
# 1. use the APT
# 2. HTML web scraping using some tool like bs4


# Step 0: Install all the requirements
#     1. pip install requests
#     2. pip install bs4
#     3. pip install html5lib

from bs4 import element
from bs4.element import Comment, NavigableString
import requests
from bs4 import BeautifulSoup

url = "http://diversityinfotech.com/"

# step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# step 3: HTML Tree Traversal

# commonly used type of objects
# print(type(title))#     1. Tag
# print(type(title.string))#     2. NavigableString
# print(type(soup))#     3. BeautifulSoup

#     4. Comment
markup = "<p><!-- this is comment  --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

# get the title of HTML page
title = soup.title

# get all the paragraphs from HTML file
pararaphs = soup.find_all('p')
print(pararaphs)

# get first element in HTML page
print(soup.find('p'))

# get class of any element in HTML page
print(soup.find('p')['class'])

# find all elements with class = lead
print(soup.find_all("p" , class_="no-pad"))

# get the text from tags/soup
print(soup.find("p").get_text())
print(soup.get_text())

# get all the achor tags from HTML file
anchors = soup.find_all('a')
print(anchors)

# get all the links from page
all_links = set()
for link in anchors:
    if(link.get("href") != "#"):
        linkText = "http://diversityinfotech.com/" + link.get("href")
        all_links.add(linkText)
        print(linkText)

print(all_links)

# find element with particular id
carouselIntro = soup.find(id="Carousel-intro")
print(carouselIntro)
print(carouselIntro.children)


# .content - a tag's childern are available as a list ==> use memory
# .children - a tag's childern are available as a generator ==> don't use memory
for elem in carouselIntro.contents:
    print(elem)

# show text from element
for item in carouselIntro.strings:
    print(item)


# show text line by line without extra gaps from element
for item in carouselIntro.stripped_strings:
    print(item)

# parent of any element
print(carouselIntro.parent)

# show all parents from down to top
for item in carouselIntro.parents:
    print(item)
    print(item.name)

# show next sibling tag of current tag -- use space as also sibling
print(carouselIntro.next_sibling.next_sibling)

# show previous sibling tag of current tag -- use space as also sibling
print(carouselIntro.previous_sibling.previous_sibling)

# get info from css selectors by using id
elem_id = soup.select('#Carousel-intro')
print(elem_id)

# get info from css selectors by using class
elem_class = soup.select('.collapse')
print(elem_class)
