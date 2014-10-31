class Figura:
	def __init__(self, args):
		self.figura = args[0]
		self.parametros = args[1:]

	def getArea(self):
		figuras={'Cuadrado' : self.cuadrado(),
				'Triangulo' : self.triangulo(),
				'Circulo' : self.circulo(),
				'Rectangulo' : self.rectangulo(),
				'Poligono' : self.poligono()}
		return figuras[self.figura]

	def cuadrado(self):
		return self.parametros[0]**2

	def circulo(self):
		return round(3.1416 * float(self.parametros[0]) **2, 2)

	def triangulo(self):
		return round(float(self.parametros[0] * float(self.parametros[1]))/2, 2)

	def rectangulo(self):
		return self.parametros[0]*self.parametros[1]

	def poligono(self):
		return round(((float(self.parametros[0]) * float(self.parametros[1])) * self.parametros[2]) / 2, 2)

