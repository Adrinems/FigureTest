#!/usr/bin/env python
import unittest
import sys
sys.path.append('../')
from Figura import Figura


class TestCase(unittest.TestCase):

    def test_cuadrado_5(self):
        parametros = ["Cuadrado", 5, 0, 0]
        fig = Figura(parametros)
        self.assertEquals(25, fig.getArea())

    def test_cuadrado_76(self):
        parametros = ["Cuadrado", 76, 0, 0]
        fig = Figura(parametros)
        self.assertEquals(5776, fig.getArea())

    def test_cuadrado_18(self):
        parametros = ["Cuadrado", 18, 0, 0]
        fig = Figura(parametros)
        self.assertEquals(324, fig.getArea())

    def test_circulo_4(self):
        parametros = ["Circulo", 4, 0, 0]
        fig = Figura(parametros)
        self.assertEquals(50.27, fig.getArea())

    def test_circulo_10(self):
        parametros = ["Circulo",10, 0, 0]
        fig = Figura(parametros)
        self.assertEquals(314.16, fig.getArea())

    def test_circulo_8_9(self):
        parametros = ["Circulo", 8.9, 0, 0]
        fig = Figura(parametros)
        self.assertEquals(248.85, fig.getArea())

    def test_rectangulo_4_3(self):
        parametros = ["Rectangulo", 4, 3, 0]
        fig = Figura(parametros)
        self.assertEquals(12, fig.getArea())

    def test_rectangulo_8_2_10(self):
        parametros = ["Rectangulo", 8.2, 10, 0]
        fig = Figura(parametros)
        self.assertEquals(82, fig.getArea())

    def test_rectangulo_15_6(self):
        parametros = ["Rectangulo", 15, 6, 0]
        fig = Figura(parametros)
        self.assertEquals(90, fig.getArea())

    def test_triangulo_3_4(self):
        parametros = ["Triangulo", 3, 4, 0]
        fig = Figura(parametros)
        self.assertEquals(6, fig.getArea())

    def test_triangulo_24_11(self):
        parametros = ["Triangulo", 24, 11, 0]
        fig = Figura(parametros)
        self.assertEquals(132, fig.getArea())

    def test_triangulo_28_33(self):
        parametros = ["Triangulo", 28, 33, 0]
        fig = Figura(parametros)
        self.assertEquals(462, fig.getArea())

    def test_octagono_4_6(self):
        parametros = ["Poligono", 4, 8, 6]
        fig = Figura(parametros)
        self.assertEquals(96, fig.getArea())

    def test_octagono_7_10(self):
        parametros = ["Poligono", 7, 8, 10]
        fig = Figura(parametros)
        self.assertEquals(280, fig.getArea())

    def test_octagono_9_15(self):
        parametros = ["Poligono", 9, 8, 15]
        fig = Figura(parametros)
        self.assertEquals(540, fig.getArea())

if __name__ == '__main__':
    unittest.main()
