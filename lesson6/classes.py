class dogs():

	def __init__(self, name, poroda, age, NewName):
		self.name = name
		self.poroda = poroda
		self.age = age
		self.NewName = NewName


	def sidet(self):
		print('Пёс породы {} возрастом {} года по кличке {} сел'.format(self.poroda, self.age, self.name))

	def lejat(self):
		print('Пёс породы {} возрастом {} года по кличке {} лёг'.format(self.poroda, self.age, self.name))

	def day_lapu(self):
		print('Пёс породы {} возрастом {} года по кличке {} дал лапу'.format(self.poroda, self.age, self.name))

	def rename(self):
		print('Теперь пёс по кличке {} называется {}'.format(self.name, self.NewName))
