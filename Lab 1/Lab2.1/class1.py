import math

class ComplexNumber:
	""" Класс комплексного числа.
	Позволяет складывать, вычитать, умножать, делить комплексное число с комплексным и действительным числом.
	Позволяет найти аргумент и модуль комплексного числа, а также преобразовать это число в строку.

	"""


	def __init__(self, realNum = 0, imNum = 0):			# Атрибуты класса:
		self.__re = realNum								#	мнимая часть числа
		self.__im = imNum								#	целая часть числа

	def getRe(self):
		return self.__re
	def getIm(self):
		return self.__im

	def setRe(self, real):
		self.__re = real
	def setIm(self, im):
		self.__im = im



	def __call__(self):
		""" Вызов объекта типа object(), вернет строку re + j * im """
		return str(self.getRe()) + " + j * " + str(self.getIm())

	# Методы сложения, вычитания, умножения, деления
	def __add__(self, y):
		""" self + y """
		if isinstance(y, ComplexNumber):
			return ComplexNumber(self.getRe() + y.getRe(), self.getIm() + y.getIm())
		elif isinstance(y, int) or isinstance(y, float):
			return ComplexNumber(self.getRe() + y, self.getIm())
	def __sub__(self, y):
		""" self - y """
		if isinstance(y, ComplexNumber):
			return ComplexNumber(self.getRe() - y.getRe(), self.getIm() - y.getIm())
		elif isinstance(y, int) or isinstance(y, float):
			return ComplexNumber(self.getRe() - y, self.getIm())
	def __mul__(self, y):
		""" self * y """
		if isinstance(y, ComplexNumber):
			return ComplexNumber(self.getRe() * y.getRe() - self.getIm() * y.getIm(), self.getRe() * y.getIm() + self.getIm() * y.getRe())
		elif isinstance(y, int) or isinstance(y, float):
			return ComplexNumber(self.getRe() * y, self.getIm() * y)
	def __truediv__(self, y):
		""" self / y """
		if isinstance(y, ComplexNumber):
			if y.getRe() ** 2 + y.getIm() ** 2 == 0:
				raise ValueError("Деление на ноль")
			else:
				return ComplexNumber((self.getRe() * y.getRe() + self.getIm() * y.getIm()) / (y.getRe() ** 2 + y.getIm() ** 2), (y.getRe() * self.getIm() - self.getRe() * y.getIm()) / (y.getRe() ** 2 + y.getIm() ** 2))
		elif isinstance(y, int) or isinstance(y, float):
			return ComplexNumber(self.getRe() / y, self.getIm() / y)


	def __radd__(self, y):
		return ComplexNumber(self.getRe() + y, self.getIm())
	def __rsub__(self, y):
		return ComplexNumber(y - self.getRe(), -self.getIm())
	def __rmul__(self, y):
		return ComplexNumber(self.getRe() * y, self.getIm() * y)
	def __rtruediv__(self, y):
		a = ComplexNumber(y, 0)
		return a / self

	def __iadd__(self, y):
		""" self += y """
		self = self + y
	def __isub__(self, y):
		""" self -= y """
		self = self - y
	def __imul__(self, y):
		""" self *= y """
		self = self * y
	def __itruediv__(self, y):
		""" self /= y """
		self = self / y





	def __abs__(self):
		""" abs(self) """
		return math.floor(math.sqrt(self.getIm() ** 2 + self.getRe() ** 2) * 100) / 100;

	def arg(self):
		""" аргумент комплексного числа """
		if self.getRe() == 0 and self.getIm() > 0:
			return 90
		elif self.getRe() == 0 and self.getIm() < 0:
			return 270
		elif self.getRe() > 0 or (self.getRe() > 0 and self.getIm() == 0):
			return math.floor(math.atan(self.getIm() / self.getRe()) * 180 / math.pi * 100) / 100
		elif self.getIm() > 0 or (self.getRe() < 0 and self.getIm() == 0):
			return math.floor(math.atan(self.getIm() / self.getRe()) * 180 / math.pi * 100) / 100 - 180
		elif self.getRe() == 0 and self.getIm() == 0:
			return 0
		else:
			return math.floor(math.atan(self.getIm() / self.getRe()) * 180 / math.pi * 100) / 100 + 180
