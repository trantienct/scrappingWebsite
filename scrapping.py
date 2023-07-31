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

    # temp = 0
    # for i in range(0, len(data2)):
    #     for j in range(i + 1, len(data2)):
    #         if data2[i]['view'] < data2[j]['view']:
    #             temp = data2[i]
    #             data2[i] = data2[j]
    #             data2[j] = temp
    # print(data2)
    newlist = sorted(data2, key=lambda d: d['view'], reverse=True)
    print(newlist)




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



