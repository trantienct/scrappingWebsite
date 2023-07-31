from bs4 import BeautifulSoup
import requests
def converStringToNumber(string):
    res = 0
    if string == 'One':
        res = 1
    if string == 'Two':
        res = 2
    if string == 'Three':
        res = 3
    if string == 'Four':
        res = 4
    if string == 'Five':
        res = 5
    return  res

url ='https://books.toscrape.com/catalogue/category/books_1/index.html'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
div_element = soup.find_all('article', {"class":"product_pod"})
list_item =[]
for element in div_element:
    dictionaryItem = {'title':'', 'image':'', 'star-rating':''}
    title = element.select('a')[1]['title']
    image = element.select('a')[0]['href']
    star_rating = element.select('.star-rating')[0]['class'][1]
    link = 'https://books.toscrape.com/'
    dictionaryItem['title'] = title
    dictionaryItem['image'] = image.replace('../../',link)
    dictionaryItem['star-rating'] = converStringToNumber(star_rating)
    list_item.append(dictionaryItem)

three_star = []
four_star = []
five_star = []




for i in list_item:
    if i['star-rating'] == 3:
        three_star.append(i)
    if i['star-rating'] == 4:
        four_star.append(i)
    if i['star-rating'] == 5:
        five_star.append(i)

new_three_star = sorted(three_star, key=lambda d: d['title'])
new_four_star = sorted(four_star, key=lambda d: d['title'])
new_five_star = sorted(five_star, key=lambda d: d['title'])
new_list = []
new_list.append(new_five_star)
new_list.append(new_four_star)
new_list.append(new_three_star)
print(new_list)


