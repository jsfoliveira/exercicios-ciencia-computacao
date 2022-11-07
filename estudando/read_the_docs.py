import requests
from parsel import Selector


url = 'https://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)

selector_css = selector.css('title::text')
print(selector_css)
#  [<Selector xpath='descendant-or-self::title/text()' data='Example website'>]

selector_getall = selector.xpath('//title/text()').getall()
['Example website']
print(selector_getall)
#  ['Example website']

