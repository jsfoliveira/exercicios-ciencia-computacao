from parsel import Selector


text = "<html><body><h1>Hello, Parsel!</h1></body></html>"
selector = Selector(text=text)

selecionar_css = selector.css('h1')
print(selecionar_css) 
# [<Selector xpath='descendant-or-self::h1' data='<h1>Hello, Parsel!</h1>'>]

extrair_dado = selector.css('h1::text').get()
print(extrair_dado)
#  [<Selector xpath='//h1' data='<h1>Hello, Parsel!</h1>'>]

extrair_dado = selector.css('h1::text').get()
print(extrair_dado)
#  extrair_dado = selector.css('h1::text').get()
print(extrair_dado)