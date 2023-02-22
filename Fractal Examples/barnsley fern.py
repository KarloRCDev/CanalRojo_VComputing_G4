import random
import matplotlib.pyplot as plt

# Definimos las cuatro transformaciones que definen el helecho de Barnsley.
def transformation_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.85 * x + 0.04 * y
    y1 = -0.04 * x + 0.85 * y + 1.6
    return x1, y1

def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.2 * x - 0.26 * y
    y1 = 0.23 * x + 0.22 * y + 1.6
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = -0.15 * x + 0.28 * y
    y1 = 0.26 * x + 0.24 * y + 0.44
    return x1, y1

def transformation_4(p):
    x = p[0]
    y = p[1]
    x1 = 0
    y1 = 0.16 * y
    return x1, y1

# Definimos una función que elige una transformación al azar.
# La probabilidad de elegir cada transformación se define en la lista probability.
def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

# Definimos una función que aplica una transformación al punto dado.
def transform(p):
    # Lista de las transformaciones
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    probability = [0.85, 0.07, 0.07, 0.01]
    # Elegimos una transformación al azar y la llamamos
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p)
    return x, y

# Definimos una función que genera los puntos del helecho.
def draw_fern(n):
    # Empezamos en (0, 0)
    x = [0]
    y = [0]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

# Pedimos al usuario que ingrese el número de puntos que quiere generar.
n = int(input('Introduce el número de puntos: '))

# Generamos los puntos del helecho.
x, y = draw_fern(n)

# Graficamos los puntos utilizando la biblioteca Matplotlib.
plt.plot(x, y, 'o', color='green')
plt.title('Helecho de Barnsley con {0} puntos'.format(n))
plt.show()