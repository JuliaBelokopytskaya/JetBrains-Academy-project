'''Разработать три класса, которые следует связать между собой, используя наследование:
класс Product, который имеет три элемент-данных — имя, цена и вес товара (базовый класс для всех классов);
класс  Buy, содержащий данные о количестве покупаемого товара в штуках(производный класс для класса Product) Данный класс должен выводить на экран информацию о товаре и о покупке ( производный класс для класса Buy);'''
class Product:
	iter=0
	def __init__(self, n,p,w):
		self.name=n
		self.price=p
		self.weight=w
		Product.iter+=1
	def get(self):
		print(f'название товара {self.name}')
		print(f" цена за штуку {self.price}")
		print(f" вес единицы товара {self.weight}")
class Buy(Product):
	def __init__(self,n,p,w,s):
		Product.__init__(self,n,p,w)
		self.count=s
	@staticmethod
	def gram_in_kg(weight_products):
		return weight_products/1000
	@classmethod
	def print_buyer_counter(cls):
		print(f" Количество просмотров товара {cls.iter}")
	def get(self):
		print(f'название товара {self.name}')
		print(f' цена за товар {self.count*self.price}')
		print(f'вес товара {self.count*self.weight}')
		return self.count*self.weight
P=Product("груша", 3.69, 2800)
P.get()
T=Buy("груша", 3.69, 2800, 15)
T.print_buyer_counter()
print("Check")
print(f" вес в кг {Buy.gram_in_kg(T.get())}")