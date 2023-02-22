import turtle 

def sierpinski(t, l, n):  # Define la función recursiva sierpinski que dibuja el triángulo de Sierpinski
    if n == 0:  # Si el nivel de recursión es cero, dibuja el triángulo base
        for i in range(3):
            t.forward(l)
            t.left(120)
    else:  # Si el nivel de recursión no es cero, llama recursivamente a la función sierpinski para dibujar triángulos más pequeños
        sierpinski(t, l / 2, n - 1) # Dibujamos el triángulo superior izquierdo, usando la recursión para reducir el tamaño del triángulo original.
        t.forward(l / 2)           # Avanzamos la tortuga a la posición donde dibujaremos el triángulo inferior.
        sierpinski(t, l / 2, n - 1) # Dibujamos el triángulo inferior, usando la recursión para reducir el tamaño del triángulo original.
        t.backward(l / 2)          # Retrocedemos la tortuga a la posición donde dibujaremos el siguiente triángulo.
        t.left(60)                 # Giramos la tortuga 60 grados a la izquierda para dibujar el triángulo superior derecho.
        t.forward(l / 2)           # Avanzamos la tortuga a la posición donde dibujaremos el triángulo superior derecho.
        t.right(60)                # Giramos la tortuga 60 grados a la derecha para dibujar el triángulo superior derecho.
        sierpinski(t, l / 2, n - 1) # Dibujamos el triángulo superior derecho, usando la recursión para reducir el tamaño del triángulo original.
        t.left(60)                 # Giramos la tortuga 60 grados a la izquierda para volver a la posición anterior.
        t.backward(l / 2)          # Retrocedemos la tortuga a la posición donde dibujaremos el siguiente triángulo.
        t.right(60)                # Giramos la tortuga 60 grados a la derecha para dibujar el siguiente triángulo.

window = turtle.Screen()  # Crea la ventana de dibujo
t = turtle.Turtle()  # Crea la tortuga que dibujará el triángulo

# Establece la velocidad de dibujo y el color de la línea de dibujo
t.speed('fastest')  
t.color('white')  

# Mueve la tortuga a la posición inicial
t.penup()  
t.goto(-300, -100)  
t.pendown()  

window.bgcolor('black')  

sierpinski(t, 300, 3)  

window.mainloop() 



'''
from random import randint
import matplotlib.pyplot as plt

# Se inicializan las listas x e y con un punto en el origen (0,0)
x , y = [0.], [0.]

# Se aplica una de tres transformaciones a cada punto en la lista, seleccionada aleatoriamente en cada iteración.
# En este caso se realizarán 100000 iteraciones
for n in range(100000):
    transformation = randint(1, 3)  # Se genera un número aleatorio entre 1 y 3
    if transformation == 1:  
        x.append((x[n]-3)/2)
        y.append(y[n]/2)
    elif transformation == 2: 
        x.append((x[n]+3)/2)
        y.append(y[n]/2)
    else:  
        x.append(x[n]/2)
        y.append((y[n]+3)/2)

# Se grafican los puntos en un plano cartesiano
plt.title('Triangulo de Sierpinski') 
plt.scatter(x, y, s=0.5, edgecolor='Blue')  
plt.scatter(x, y, s=0.001, edgecolor='White')  
plt.show()  
'''

