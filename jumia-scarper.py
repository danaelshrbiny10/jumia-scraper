from requests_html import HTMLSession



session = HTMLSession()

url = session.get('https://www.jumia.com.eg/electronics/')


url.html.render(sleep=2)


products = url.html.xpath('/html/body/div[1]/main/div[2]/div[3]/section/div[1]', first=True)


for product in products.absolute_links:
    
    # print(product.html.find('h3.names', first=True).text)
    # print(product)
    
    url = session.get(product)
    name = url.html.find('h1.-fs20', first=True).text
    Product_details = url.html.find('div.markup', first=True).text
    price = url.html.find('span.-b', first=True).text
    rate = url.html.find('div.stars', first=True).text
    image = url.html.find('img.-fw', first=True).text

    print(name)
    print(Product_details)
    print(price)
    print(rate)
    print(image)
