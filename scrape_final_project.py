from bs4 import BeautifulSoup
import requests

url ='https://books.toscrape.com/catalogue/category/books_1/index.html'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

all_articles = soup.select('.nav-list li')
del all_articles[0]
data = []
id = 0
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
menu_choice = True
while menu_choice == True:
    for item in all_articles:
        link = 'https://books.toscrape.com/catalogue/category/'
        menu_item = {'category_id':'', 'category_name':'', 'url':''}
        category_name = item.getText()
        id +=1
        menu_item['category_id'] = id
        menu_item['category_name'] = category_name.replace(' ','').replace('\n','')
        category_link = item.select('a')[0]['href']
        menu_item['url'] = category_link.replace('../',link)
        # article_request = requests.get(menu_item['url'])
        # article_soup = BeautifulSoup(article_request.text, 'html.parser')
        # number_book = article_soup.select('.form-horizontal strong')
        # menu_item['num_book'] = number_book[0].getText()
        data.append(menu_item)

    x = True
    while x == True:
        for i in data:
            print(f"{i['category_id']}.{i['category_name']}")
        user_choice = input('choose your category by typing the number:')
        for i in data:
            if int(user_choice) == i['category_id']:
                article_request = requests.get(i['url'])
                article_soup = BeautifulSoup(article_request.text, 'html.parser')
                print(f'''
        Category:{i['category_name']} - Number of books:
            What do you want?
                1. View Top 3 books by rating, price
                2. View The most expensive book
                3. View the cheapest book
                4. Back''')
                user_choice2 = input('type your number:')
                articles = article_soup.select('.product_pod')
                data2 = []
                for item in articles:
                    book = {'book_name':'','price':'', 'star-rating':''}
                    book['book_name'] = item.select('h3 a')[0]['title']
                    book['price'] = item.select('.product_price p')[0].getText().replace('Â£','')
                    star_rating = item.select('.star-rating')[0]['class'][1]
                    book['star-rating'] = converStringToNumber(star_rating)
                    data2.append(book)

                if int(user_choice2) == 1:
                    new_list = sorted(data2, key=lambda d:(d['star-rating'],d['price']), reverse=True)
                    print(f'''Top 3 book: 
                    {new_list[0]['book_name']} - {new_list[0]['star-rating']} - £{new_list[0]['price']}
                    {new_list[1]['book_name']} - {new_list[1]['star-rating']} - £{new_list[1]['price']}
                    {new_list[2]['book_name']} - {new_list[2]['star-rating']} - £{new_list[2]['price']}''')
                if int(user_choice2) == 2:
                    new_list = sorted(data2, key = lambda d:d['price'], reverse=True)
                    print(f"The most expensive book: {new_list[0]['book_name']} - £{new_list[0]['price']}")

                if int(user_choice2) == 3:
                    new_list = sorted(data2, key = lambda d:d['price'])
                    print(f"The cheapest book:  {new_list[0]['book_name']} - £{new_list[0]['price']}")
                if int(user_choice2) == 4:
                    x = False













