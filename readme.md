# Búsqueda bidireccional (BFS) - Curso Inteligencia artificial

[![Stars](https://img.shields.io/github/stars/MrNizzy/WGuides-Angular?style=social)](https://github.com/MrNizzy/WGuides-Angular) [![YouTube](https://img.shields.io/youtube/channel/subscribers/UCFjfIk29NqqPGmrCfCV14Yg?style=social)](https://www.youtube.com/channel/UCFjfIk29NqqPGmrCfCV14Yg) [![Maintainer](https://img.shields.io/badge/Maintained%20by-MrNizzy-blue)](https://www.linkedin.com/in/mrnizzy/ "MrNizzy")

## Descripción

Esta búsqueda bidireccional intentará que un Agente encuentre un Objetivo (Meta) mediante una búsqueda doble de un árbol de búsqueda, es decir, hacer una búsqueda desde el agente, y otra desde la meta. Para ello se debe cumplir con los siguientes objetivos:

* Realizar dos búsquedas al tiempo, (agente y meta).
* Al menos una de estas búsquedas debe ser en anchura.
* Cuando llegue a un nodo que ya había sido explorado con el otro tipo de búsqueda, el algoritmo acaba, es decir, cuando ambos nodos generados de los dos árboles sean iguales.
* El camino solución es la suma de los caminos hallados por cada búsqueda desde el nodo mencionado hasta el nodo inicial y el nodo meta, en otras palabras, la suma o conteo de los nodos que fueron necesarios para hallar la solución.

## Especificaciones

Para este proyecto se usará el lenguaje de programación [Python](https://www.python.org/). Además de usar las librerias de [Turtle](https://docs.python.org/3/library/turtle.html) y [numpy](https://numpy.org/doc/stable/).
Usa el comando:

```python
pip install numpy
```

Para instalar la librería de Numpy.

## Resultados

[![Grid BD_BFS](https://i.postimg.cc/13Tf9kLc/image.png)](https://postimg.cc/cvRshb1r)

## Recomendaciones

Usar [Visual Studio Code](https://code.visualstudio.com/)

## Configurando el tablero

Para configurar el tablero puedes realizar cambios desde el archivo ``config.py`` donde puedes agregar las coordenadas de inicio del agente y la meta. Para las demás configuraciones avanzadas, como cambio de dimensiones de la ventana, el espacio entre cada caja del tablero, lo puedes realizar en el archivo ``main.py`` aunque es recomendable cambiar estos valores, ya que puede afectar en gran medida a la disposición correcta de los objetos que se verán en pantalla. Por otro lado, el cambio del tamaño de las imágenes (muro, meta, jugador y recompensa) no se puede modificar por qué son las dimensiones originales de los archivos para que no ocupen gran espacio en la pantalla y se puedan visualizar laberintos un poco más grandes.

### Ejemplos de laberinto

* Ejemplo 1.

```txt
1 1 1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1 0 1 1 1
1 0 1 0 0 0 0 0 0 0 0 1
1 0 1 0 1 1 1 1 1 1 0 1
1 0 1 0 1 0 0 0 0 0 0 1
1 0 0 0 1 1 0 1 1 1 0 1
1 0 1 0 0 0 0 1 0 1 1 1
1 0 1 1 0 1 0 0 0 0 0 1
1 0 1 0 0 1 1 1 1 1 0 1
1 0 0 0 1 1 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 1 1
```

* Ejemplo 2 (por defecto).

```txt
1 1 1 1 1 1 1 1 1
1 0 1 0 1 0 0 0 1
1 0 1 0 1 0 1 0 1
1 0 1 0 0 0 1 0 1
1 0 1 0 0 0 0 0 1
1 0 1 0 1 1 0 1 1
1 0 0 0 1 0 0 1 1
1 0 1 0 1 1 0 0 1
1 1 1 1 1 1 1 1 1
```

#### Nota

Recuerda que las matrices deben ser cuadradas, es decir, NxN y no NxM de lo contrario no se podrá dibujar bien el tablero o directamente puede ocasionar un error al generador visual.
