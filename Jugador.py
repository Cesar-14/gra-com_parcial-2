from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import Modelo
from Limites import *

limites = Limites()

class Jugador(Modelo):
    avanzar = True
    window = None

    def __init__(self):
        super().__init__(-0.7, 0.7, 0.0, 0.003, 0.0)
        self._velocidad = 0.003

    def dibujar(self):

        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)
        glBegin(GL_QUADS)
        
        glColor3f(1,0,0)
        glVertex3f(-0.05, 0.05,0.0)
        glVertex3f(0.05, 0.05,0.0)
        glVertex3f(0.05, -0.05,0.0)
        glVertex3f(-0.05, -0.05,0.0)
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor(0,0,0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(-0.05, 0.05, 0)
        glVertex3f(0.05, 0.05, 0)
        glVertex3f(0.05, -0.05, 0)
        glEnd()

        glPopMatrix()

    def actualizar(self, tiempo_delta, window):

        tiempo_actual = glfw.get_time()
        
        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        cantidad_movimiento = self.velocidad * tiempo_delta

        # Controles jugador
        estado_tecla_w = glfw.get_key(window, glfw.KEY_UP)
        estado_tecla_s = glfw.get_key(window, glfw.KEY_DOWN)
        estado_tecla_a = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_tecla_d = glfw.get_key(window, glfw.KEY_LEFT)

        if estado_tecla_w == glfw.PRESS:
            self.posicion_y = self.posicion_y + cantidad_movimiento
        if estado_tecla_s == glfw.PRESS:
            self.posicion_y = self.posicion_y - cantidad_movimiento
        if estado_tecla_a == glfw.PRESS:
            self.posicion_x = self.posicion_x + cantidad_movimiento
        if estado_tecla_d == glfw.PRESS:
            self.posicion_x = self.posicion_x - cantidad_movimiento

        # if estado_tecla_w == glfw.PRESS:
        #     if limites.colisionando():
        #         self.posicion_x = -0.7
        #         self.posicion_y = 0.7
        #         self.posicion_z = 0.0
        #     else:
        #         self.posicion_x = self.posicion_x - cantidad_movimiento

        # if estado_tecla_s == glfw.PRESS:
        #     if limites.colisionando():
        #         self.posicion_x = -0.7
        #         self.posicion_y = 0.7
        #         self.posicion_z = 0.0
        #     else:
        #         self.posicion_x = self.posicion_x - cantidad_movimiento

        # if estado_tecla_a == glfw.PRESS:
        #     if limites.colisionando():
        #         self.posicion_x = -0.7
        #         self.posicion_y = 0.7
        #         self.posicion_z = 0.0
        #     else:
        #         self.posicion_x = self.posicion_x - cantidad_movimiento

        # if estado_tecla_d == glfw.PRESS:
        #     if limites.colisionando():
        #         self.posicion_x = -0.7
        #         self.posicion_y = 0.7
        #         self.posicion_z = 0.0
        #     else:
        #         self.posicion_x = self.posicion_x - cantidad_movimiento
