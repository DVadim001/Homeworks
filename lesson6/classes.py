class dogs():

	def __init__(self, name, poroda, age):
		self.name = name
		self.poroda = poroda
		self.age = age

	def sidet(self):
		print('Пёс {} сел'.format(self.name))

	def lejat(self):
		print('Пёс {} лёг'.format(self.name))

	def day_lapu(self):
		print('Пёс {} дал лапу'.format(self.name))
