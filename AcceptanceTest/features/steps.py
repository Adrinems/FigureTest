# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append('../')
from Figura import Figura


"""  Circulo/cuadrado  """
@step(u'Given: Que la figura es un "([^"]*)" y el lado es "([^"]*)"')
def given_que_la_figura_es_un_group1_y_el_lado_es_group2(step, figura, lado):
    world.parametros= [figura, int(lado), 0, 0]
   

"""  Triangulo/Rectangulo  """
@step(u'Given: Que la figura es un "([^"]*)" con base "([^"]*)" y altura "([^"]*)"')
def given_que_la_figura_es_un_group1_con_base_group2_y_altura_group3(step, figura, base, altura):
	world.parametros=[figura, int(base), int(altura), 0]


"""  Poligono  """
@step(u'Given: Que la figura es un "([^"]*)" con longitud lado "([^"]*)", lados "([^"]*)" y apotema "([^"]*)"')
def given_que_la_figura_es_un_group1_con_longitud_lado_group2_lados_group3_y_apotema_group4(step, figura, longlados, lados, apotema):
    world.parametros = [figura, int(longlados), int(lados), int(apotema)]

@step(u'when realizo el cálculo')
def when_realizo_el_calculo(step):
    fig = Figura(world.parametros)
    world.area=fig.getArea()

@step(u'then obtengo el resultado "([^"]*)"')
def then_obtengo_el_resultado_36(step, area):
    assert world.area == int(area), "area calculada {0}, area esperada {1}".format(world.area, area)

@step(u'then obtengo el resultado con decimales es "([^"]*)"')
def then_obtengo_el_resultado_con_decimales_es_group1(step, area):
    assert float(world.area) == float(area), 'area calculada {0}, area esperada {1}'.format(world.area, area)

@step(u'then obtengo el area igual a "([^"]*)"')
def then_obtengo_el_area_igual_a(step, area):
    assert float(world.area) == float(area), 'area calculada {0}, area esperada {1}'.format(world.area, area)

