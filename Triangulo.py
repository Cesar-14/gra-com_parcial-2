#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import Modelo

class Triangulo(Modelo):
    

    def __init__(self):
        super().__init__(-0.7, 0.7, 0.0, 0.4, 0.0)
        self.velocidad = 0.4
        self.tiempo_anterior = 0.0
        self.angulo = 0.0     
        self.velocidad_rotacion = 400

    def actualizar_triangulo(self, tiempo_delta):

        tiempo_actual = glfw.get_time()
        tiempo_delta = tiempo_actual - self.tiempo_anterior

        #Revisamos estados y realizamos acciones
        cantidad_movimiento = self.velocidad * tiempo_delta
        cantidad_rotacion = self.velocidad_rotacion * tiempo_delta

        if self.direccion == 0:
            self.angulo = self.angulo + cantidad_rotacion
            self.posicion_x = self.posicion_x - cantidad_movimiento
            if self.angulo > 360.0:
                self.angulo = self.angulo - 360.0 
        if self.direccion == 1:
            self.angulo = self.angulo - cantidad_rotacion
            self.posicion_x = self.posicion_x + cantidad_movimiento
            if self.angulo < 0.0:
                self.angulo = self.angulo + 360.0
        if self.posicion_x <= -0.75 and self.direccion == 0:
            self.direccion = 1

        if self.posicion_x >= 0.75 and self.direccion == 1:
            self.direccion = 0

        self.tiempo_anterior = tiempo_actual
        


    def actualizar(self):

        tiempo_actual = glfw.get_time()
        # Cuanto tiempo paso entre la ejecucion actual
        # y la inmediata anterior de esta funcion
        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        # Revisamos estados y realizamos acciones
        self.actualizar_triangulo(tiempo_delta)
        self.tiempo_anterior = tiempo_actual



    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, 0.91,0.0)
        glRotatef(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)

        glColor3f(0.8,0.8,1,5)

        #Manda vertices a dibujar
        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0.0,0.05,0)
        glVertex3f(0.05,-0.05,0)

        glEnd()
        glPopMatrix()
