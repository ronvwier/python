class animal():
	def __init__(self,name):
		print('a new animal',name)
		self.name = name
	def sound(self):
		print('animal noise by',self.name)
		
class haslegs():
	def __init__(self,number):
		print('haslegs',number)
		self.legs = number
	def sound(self):
		print('ttippel, trippel')
		
class dog(animal,haslegs):
	def __init__(self,name):
		animal.__init__(self,name)
		haslegs.__init__(self,4)
		print('a new dog',name)
	def sound(self):
		animal.sound(self)
		haslegs.sound(self)
		print('woof by ',self.name)
		
x = animal('anima')
x.sound()
print(type(x))
x = dog('fikkie')
x.sound()
print(type(x),x.legs,x.name)