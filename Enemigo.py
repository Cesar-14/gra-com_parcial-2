
from OpenGL.GL import *
from glew_wish import *
import glfw
import math 
from Modelo import Modelo
from Jugador import *

class Enemigo(Modelo):
    direccion = 1
    posicion = 0.0

    def __init__(self):
        super().__init__(-0.7, 0.7, 0.0, 3, 0)
        self.velocidad = 3
        self.angulo = 0.0     
        self.velocidad_rotacion = 400
        self.posicion = 0.0

    def actualizar_enemigo(self, tiempo_delta):

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
        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        # Revisamos estados y realizamos acciones
        self.actualizar_enemigo(tiempo_delta)
        self.tiempo_anterior = tiempo_actual

        # if colision_enemigos():
        # posicion_x = -0.7
        # posicion_y = 0.7
        # pisicion_z = 0.0


    def colision_enemigos(self):
        # Colisión enemigos
        colision_enemigos = False

        if (self.posicion + 0.05 >= Jugador.posicion_x - 0.05
            and self.posicion - 0.05 <= Jugador.posicion_x + 0.05
            and self.posicion + 0.05 >= Jugador.posicion_y - 0.05
            and self.posicion - 0.05 <= Jugador.posicion_y + 0.05):
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
