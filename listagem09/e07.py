class bichoVirt:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		self.__hunger = 100
		self.__health = 100

	def get_name(self):
		return self.__name

	def set_name(self, new_name):
		self.__name = new_name

	def get_age(self):
		return self.__age

	def set_age(self, new_age):
		self.__age = new_age

	def get_hunger(self):
		return self.__hunger

	def set_hunger(self, new_hunger):
		self.__hunger = new_hunger

	def get_health(self):
		return self.__health

	def set_health(self, new_health):
		self.__health = new_health

	def get_humor(self):
		if self.get_hunger() >= 70 and self.get_health() >= 70:
			return "I'm happy!"

		elif self.get_hunger() >= 50 and self.get_health() >= 50:
			return "I'm not so good!"

		elif self.get_hunger() >= 30 and self.get_health() >= 30:
			return "I'm very angry!"

		else:
			return "I'm so weak that I can't answer!"

bichinho = bichoVirt("Bolinha", 2)

print( bichinho.get_name() )
print( bichinho.get_age() )
print( bichinho.get_humor() )

bichinho.set_health(30)
bichinho.set_hunger(70)

print( bichinho.get_humor() )


class bichoVirt:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		self.__hunger = 100
		self.__health = 100

	def get_name(self):
		return self.__name

	def set_name(self, new_name):
		self.__name = new_name

	def get_age(self):
		return self.__age

	def set_age(self, new_age):
		self.__age = new_age

	def get_hunger(self):
		return self.__hunger

	def set_hunger(self, new_hunger):
		self.__hunger = new_hunger

	def get_health(self):
		return self.__health

	def set_health(self, new_health):
		self.__health = new_health

	def get_humor(self):
		if self.get_hunger() >= 70 and self.get_health() >= 70:
			return "I'm happy!"

		elif self.get_hunger() >= 50 and self.get_health() >= 50:
			return "I'm not so good!"

		elif self.get_hunger() >= 30 and self.get_health() >= 30:
			return "I'm very angry!"

		else:
			return "I'm so weak that I can't answer!"

bichinho = bichoVirt("Bolinha", 2)

print( bichinho.get_name() )
print( bichinho.get_age() )
print( bichinho.get_humor() )

bichinho.set_health(30)
bichinho.set_hunger(70)

print( bichinho.get_humor() )


