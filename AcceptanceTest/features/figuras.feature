Feature: Obtener el área de figuras geométricas básicas
	Cómo usuario del sistema
	Quiero obtener el área de distintas figuras
	para facilitar algunos cálculos.


Scenario: "Cuadrado" y el lado es "6"
	Given: Que la figura es un "Cuadrado" y el lado es "6"
	when realizo el cálculo
	then obtengo el resultado "36"

Scenario: "Cuadrado" y el lado es "8"
	Given: Que la figura es un "Cuadrado" y el lado es "8"
	when realizo el cálculo 
	then obtengo el resultado "64"

Scenario: "Cuadrado" y el lado es "8"
	Given: Que la figura es un "Cuadrado" y el lado es "8"
	when realizo el cálculo 
	then obtengo el resultado "64"

Scenario: "Cuadrado" y el lado es "10"
	Given: Que la figura es un "Cuadrado" y el lado es "10"
	when realizo el cálculo 
	then obtengo el resultado "100"

Scenario: "Circulo" y el radio es "3"
	Given: Que la figura es un "Circulo" y el lado es "3"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "28.27"

Scenario: "Circulo" y el radio es "5"
	Given: Que la figura es un "Circulo" y el lado es "5"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "78.54"

Scenario: "Circulo" y el radio es "9"
	Given: Que la figura es un "Circulo" y el lado es "9"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "254.47"

Scenario: "Triangulo" con base "8" y altura "9"
	Given: Que la figura es un "Triangulo" con base "8" y altura "9"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "36"

Scenario: "Triangulo" con base "4" y altura "7"
	Given: Que la figura es un "Triangulo" con base "4" y altura "7"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "14"

Scenario: "Triangulo" con base "11" y altura "7"
	Given: Que la figura es un "Triangulo" con base "11" y altura "7"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "38.50"

Scenario: "Rectangulo" con base "4" y altura "3"
	Given: Que la figura es un "Rectangulo" con base "4" y altura "3"
	when realizo el cálculo 
	then obtengo el resultado con decimales es "12"

Scenario: "Poligono" con longitud lado "10", lados "7" y apotema "4"
	Given: Que la figura es un "Poligono" con longitud lado "10", lados "7" y apotema "4"
	when realizo el cálculo 
	then obtengo el area igual a "140.00"
