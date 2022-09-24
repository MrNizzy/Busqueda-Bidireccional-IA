# Proyecto de búsqueda bidireccional - Curso Inteligencia artificial

## Descripción

Esta búsqueda bidireccional intentará que un Agente encuentre un Objetivo (Meta) mediante una búsqueda doble de un árbol de búsqueda, es decir, hacer una búsqueda desde el agente, y otra desde la meta. Para ello se debe cumplir con los siguientes objetivos:

* Realizar dos búsquedas al tiempo, (agente y meta).
* Al menos una de estas búsquedas debe ser en anchura.
* Cuando llegue a un nodo que ya había sido explorado con el otro tipo de búsqueda, el algoritmo acaba, es decir, cuando ambos nodos generados de los dos árboles sean iguales.
* El camino solución es la suma de los caminos hallados por cada búsqueda desde el nodo mencionado hasta el nodo inicial y el nodo meta, en otras palabras, la suma o conteo de los nodos que fueron necesarios para hallar la solución.

## Especificaciones

Para este proyecto se usará el lenguaje de programación [Python](https://www.python.org/). Además de usar las librerias de [Turtle](https://docs.python.org/3/library/turtle.html) y [numpy](https://numpy.org/doc/stable/).

## Resultados

![Grid de la interfaz](https://i.postimg.cc/y809bHRc/image.png)

## Recomendaciones

Usar [Visual Studio Code](https://code.visualstudio.com/)