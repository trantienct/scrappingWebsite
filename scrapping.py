from bs4 import BeautifulSoup
import requests
data = []
with open('website.html', encoding='utf8') as file:
    soup = BeautifulSoup(file, 'html.parser')
div_element = soup.find_all('div', {"class":"container"})
def generatePost():
    data2 = []
    for element in div_element:
        head = element.find('h2').getText()
        span = element.select('span')
        span2 = span[2].getText()
        view = span2.replace('View : ','')
        # view = span2[7:]
        post = {'title': '', 'view':''}
        post['title'] = head
        post['view'] = view
        data2.append(post)

    print(data2)



generatePost()


# for element in div_element:
#     head = element.find('h2').getText()
#     paragraph = element.find('p').getText()
#     print(head)
#     print(paragraph)
#     post = {'title':'', 'description':''}
#     post['title'] = head
#     post['description'] = paragraph
#     data.append(post)



