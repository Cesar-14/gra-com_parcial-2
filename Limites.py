from OpenGL.GL import *
from glew_wish import *
import glfw
import math 
from Modelo import Modelo

class Limites(Modelo):
    posicion_pared_x = 0.0
    posicion_pared_y = 0.8
    posicion_pared_z = 0.0

    posicion_pared2_x = -0.8
    posicion_pared2_y = 0.0
    posicion_pared2_z = 0.0

    posicion_pared3_x = 0.8
    posicion_pared3_y = 0.0
    posicion_pared3_z = 0.0

    posicion_pared4_x = 0.0
    posicion_pared4_y = -0.8
    posicion_pared4_z = 0.0

    posicion_ganar_x = 0.7
    posicion_ganar_y = -0.7
    posicion_ganar_z = 0.0

    def draw_pared(self):

        glPushMatrix()
        glTranslatef(self.posicion_pared_x, self.posicion_pared_y, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(-0.8, 0.01,0.0)
        glVertex3f(0.8, 0.01,0.0)
        glVertex3f(0.8, -0.01,0.0)
        glVertex3f(-0.8, -0.01,0.0)

        glEnd()

        glPopMatrix()

    def draw_pared_2(self):

        glPushMatrix()
        glTranslatef(self.posicion_pared2_x, self.posicion_pared2_y, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(-0.01, 0.8,0.0)
        glVertex3f(0.01, 0.8,0.0)
        glVertex3f(0.01, -0.8,0.0)
        glVertex3f(-0.01, -0.8,0.0)
        glEnd()

        glPopMatrix()

    def draw_pared_3(self):

        glPushMatrix()
        glTranslatef(self.posicion_pared3_x, self.posicion_pared3_y, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(-0.01, 0.8,0.0)
        glVertex3f(0.01, 0.8,0.0)
        glVertex3f(0.01, -0.8,0.0)
        glVertex3f(-0.01, -0.8,0.0)
        glEnd()

        glPopMatrix()

    def draw_pared_4(self):

        glPushMatrix()
        glTranslatef(self.posicion_pared4_x, self.posicion_pared4_y, 0.0)
        glBegin(GL_QUADS)

        glColor3f(0,0,0)
        glVertex3f(-0.8, 0.01,0.0)
        glVertex3f(0.8, 0.01,0.0)
        glVertex3f(0.8, -0.01,0.0)
        glVertex3f(-0.8, -0.01,0.0)

        glEnd()
        glPopMatrix()
    
    def draw_ganar(self):

        glPushMatrix()
        glTranslatef(self.posicion_ganar_x, self.posicion_ganar_y, 0.0)
        glBegin(GL_QUADS)
        glColor(0.2,1.0,0.7)
        glVertex3f(0.1, -0.1, 0)
        glVertex3f(0.1, 0.1, 0)
        glVertex3f(-0.1, 0.1, 0)
        glVertex3f(-0.1, -0.1, 0)
        if self.colision_ganar():
            glfw.destroy_window(window)
        glEnd()

        glPopMatrix()
    
    def actualizar(self):

        tiempo_actual = glfw.get_time()

        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        self.colision_ganar(tiempo_delta)
        self.tiempo_anterior = tiempo_actual
    
    def colision_ganar(self):
        colision_ganar = False

        if (self.posicion_ganar_x + 0.075 >= self.posicion_x - 0.075
            and self.posicion_ganar_x - 0.075 <= self.posicion_x + 0.075
            and self.posicion_ganar_y + 0.075 >= self.posicion_y - 0.075
            and self.posicion_ganar_y - 0.075 <= self.posicion_y + 0.075):
            colision_ganar = True
        return colision_ganar
    
    def colisionando(self):
        colisionando = False
        colision_ganar = False

        if (self.posicion_pared_y + 0.43 >= self.posicion_x - 0.43
            and self.posicion_pared_x - 0.43 <= self.posicion_x + 0.43
            and self.posicion_pared_y + 0.03 >= self.posicion_y - 0.03
            and self.posicion_pared_y - 0.03 <= self.posicion_y + 0.03):
            colisionando = True
        

        if (self.posicion_pared2_x + 0.03 >= self.posicion_x - 0.03
            and self.posicion_pared2_x - 0.03 <= self.posicion_x + 0.03
            and self.posicion_pared2_y + 0.43 >= self.posicion_y - 0.43
            and self.posicion_pared2_y - 0.43 <= self.posicion_y + 0.43):
            colisionando = True
        

        if (self.posicion_pared3_x + 0.03 >= self.posicion_x - 0.03
            and self.posicion_pared3_x - 0.03 <= self.posicion_x + 0.03
            and self.posicion_pared3_y + 0.43 >= self.posicion_y - 0.43
            and self.posicion_pared3_y - 0.43 <= self.posicion_y + 0.43):
            colisionando = True


        if (self.posicion_pared4_x + 0.43 >= self.posicion_x - 0.43
            and self.posicion_pared4_x - 0.43 <= self.posicion_x + 0.43
            and self.posicion_pared4_y + 0.03 >= self.posicion_y - 0.03
            and self.posicion_pared4_y - 0.03 <= self.posicion_y + 0.03):
            colisionando = True

        return colisionando