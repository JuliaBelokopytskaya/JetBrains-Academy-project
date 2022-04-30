'''Разработать три класса, которые следует связать между собой, используя наследование:
класс Product, который имеет три элемент-данных — имя, цена и вес товара (базовый класс для всех классов);
класс  Buy, содержащий данные о количестве покупаемого товара в штуках(производный класс для класса Product и базовый класс для класса Check);
класс Check, не содержащий никаких элемент-данных. Данный класс должен выводить на экран информацию о товаре и о покупке ( производный класс для класса Buy);'''
class Product:
	def __init__(self, n,p,w):
		self.name=n
		self.price=p
		self.weight=w
class Buy(Product):
	def __init__(self,n,p,w,s):
		Product.__init__(self,n,p,w)
		self.count=s
class Check(Buy):
	def __init__(self,n,p,w,s):
		Buy.__init__(self,n,p,w,s)
	def get(self):
		print(f'название товара {self.name}')
		print(f' цена за товар {self.count*self.price}')
		print(f'вес товара {self.count*self.weight}')
T=Check("груша", 3.69, 2.800, 15)
T.get()