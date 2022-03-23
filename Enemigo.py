#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from OpenGL.GL import *
from glew_wish import *
import glfw
import math 
# from Principal import *

class Enemigo:
    velocidad = 0.4
    posicion_triangulo = 0.0
    tiempo_anterior = 0.0
    direccion = 1
    posicion_cuadrado = [-0.7, 0.7, 0.0]
    posicion = 0.0

    def actualizar_cuadrado(self, tiempo_delta):

        cantidad_movimiento = self.velocidad * tiempo_delta
        
        if self.direccion == 0:
            self.posicion = self.posicion - cantidad_movimiento
        elif self.direccion == 1:
            self.posicion = self.posicion + cantidad_movimiento
        
        if self.posicion <= -0.75 and self.direccion == 0:
            self.direccion = 1

        if self.posicion >= 0.75 and self.direccion == 1:
            self.direccion = 0



    def actualizar(self):

        tiempo_actual = glfw.get_time()
        # Cuanto tiempo paso entre la ejecucion actual
        # y la inmediata anterior de esta funcion
        tiempo_delta = tiempo_actual - tiempo_anterior
        
        # Revisamos estados y realizamos acciones
        self.cantidad_movimiento = self.velocidad * tiempo_delta

        if self.colision_enemigos():
            self.posicion_cuadrado = [-0.7, 0.7, 0.0]

        self.actualizar_cuadrado(tiempo_delta)
        tiempo_anterior = tiempo_actual


    def colision_enemigos(self):
        # Colisión enemigos
        colision_enemigos = False

        if (self.posicion + 0.05 >= self.posicion_cuadrado[0] - 0.05
            and self.posicion - 0.05 <= self.posicion_cuadrado[0] + 0.05
            and self.posicion + 0.05 >= self.posicion_cuadrado[1] - 0.05
            and self.posicion - 0.05 <= self.posicion_cuadrado[1] + 0.05):
            colision_enemigos = True
        return colision_enemigos    


    def dibujar(self):
        glPushMatrix()
        
        glTranslatef(self.posicion, self.posicion, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.2,0.2,0.9)

        glVertex3f(-0.05, 0.05,0.0)
        glVertex3f(0.05, 0.05,0.0)
        glVertex3f(0.05, -0.05,0.0)
        glVertex3f(-0.05, -0.05,0.0)
        glEnd()
        glPopMatrix()
