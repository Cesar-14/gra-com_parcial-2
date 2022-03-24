from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Jugador import *
from Enemigo import *
from Triangulo import *
from Limites import *
# from Modelo import Modelo

jugador = Jugador()
enemigo = Enemigo()
triangulo = Triangulo()
limites = Limites()


tiempo_anterior = 0.0
velocidad_rotacion_triangulo = 400.0
window = None

#Direcciones
direccion_enemigos = 1
direccion_triangulo = 0
direccion_enemigos_2 = 1

avanzar = True


def actualizar():
    global tiempo_anterior
    global window

    tiempo_actual = glfw.get_time()

    tiempo_delta = tiempo_actual - tiempo_anterior

    jugador.actualizar(tiempo_delta, window)
    triangulo.actualizar()
    enemigo.actualizar()

    tiempo_anterior = tiempo_actual


def draw_inicio():

    glBegin(GL_QUADS)
    glColor(0.2,1.0,0.7)
    glVertex3f(-0.6, 0.6, 0)
    glVertex3f(-0.6, 0.8, 0)
    glVertex3f(-0.8, 0.8, 0)
    glVertex3f(-0.8, 0.6, 0)
    glEnd()

def draw_fondo():
    glBegin(GL_QUADS)
    glColor3f(0.9,1,0.9)

    glVertex3f(-0.8, 0.8,0.0)
    glVertex3f(0.8, 0.8,0.0)
    glVertex3f(0.8, -0.8,0.0)
    glVertex3f(-0.8, -0.8,0.0)
    glEnd()

def decoracion():
    glPushMatrix()
    glTranslatef(-0.9, 0.83, 0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.8,1,5)

    glVertex3f(-0.05, 0.05,0.0)
    glVertex3f(0.05, 0.05,0.0)
    glVertex3f(0.05, -0.05,0.0)
    glVertex3f(-0.05, -0.05,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.8, 0.33, 0)
    glBegin(GL_QUADS)
    glColor3f(0.8,0.8,1,5)

    glVertex3f(-0.1, 0.1,0.0)
    glVertex3f(0.1, 0.1,0.0)
    glVertex3f(0.1, -0.1,0.0)
    glVertex3f(-0.1, -0.1,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1, -0.33, 0)
    glBegin(GL_QUADS)
    glColor3f(0.7,0.9,1,5)

    glVertex3f(-0.08, 0.08,0.0)
    glVertex3f(0.08, 0.08,0.0)
    glVertex3f(0.08, -0.08,0.0)
    glVertex3f(-0.08, -0.08,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, -0.53, 0)
    glBegin(GL_QUADS)
    glColor3f(0.7,0.4,1,5)

    glVertex3f(-0.09, 0.09,0.0)
    glVertex3f(0.09, 0.09,0.0)
    glVertex3f(0.09, -0.09,0.0)
    glVertex3f(-0.09, -0.09,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.9, -0.13, 0)
    glBegin(GL_QUADS)
    glColor3f(0.3,0.7,1,5)

    glVertex3f(-0.03, 0.03,0.0)
    glVertex3f(0.03, 0.03,0.0)
    glVertex3f(0.03, -0.03,0.0)
    glVertex3f(-0.03, -0.03,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 0.5, 0)
    glBegin(GL_QUADS)
    glColor3f(0.9,0.9,1,5)

    glVertex3f(-0.15, 0.15,0.0)
    glVertex3f(0.15, 0.15,0.0)
    glVertex3f(0.15, -0.15,0.0)
    glVertex3f(-0.15, -0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, -1, 0)
    glBegin(GL_QUADS)
    glColor3f(0.4,0.6,1,5)

    glVertex3f(-0.15, 0.15,0.0)
    glVertex3f(0.15, 0.15,0.0)
    glVertex3f(0.15, -0.15,0.0)
    glVertex3f(-0.15, -0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.9, -0.95, 0)
    glBegin(GL_QUADS)
    glColor3f(0.1,0.9,1,5)

    glVertex3f(-0.02, 0.02,0.0)
    glVertex3f(0.02, 0.02,0.0)
    glVertex3f(0.02, -0.02,0.0)
    glVertex3f(-0.02, -0.02,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.5, -0.95, 0)
    glBegin(GL_QUADS)
    glColor3f(0.9,0.8,1,5)

    glVertex3f(-0.05, 0.05,0.0)
    glVertex3f(0.05, 0.05,0.0)
    glVertex3f(0.05, -0.05,0.0)
    glVertex3f(-0.05, -0.05,0.0)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.3, -0.85, 0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.6,4,5)

    glVertex3f(-0.1, 0.1,0.0)
    glVertex3f(0.1, 0.1,0.0)
    glVertex3f(0.1, -0.1,0.0)
    glVertex3f(-0.1, -0.1,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 0.9, 0)
    glBegin(GL_QUADS)
    glColor3f(0.9,0.4,1,5)

    glVertex3f(-0.04, 0.04,0.0)
    glVertex3f(0.04, 0.04,0.0)
    glVertex3f(0.04, -0.04,0.0)
    glVertex3f(-0.04, -0.04,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.4, 0.9, 0)
    glBegin(GL_QUADS)
    glColor3f(0.8,0.7,1,5)

    glVertex3f(-0.07, 0.07,0.0)
    glVertex3f(0.07, 0.07,0.0)
    glVertex3f(0.07, -0.07,0.0)
    glVertex3f(-0.07, -0.07,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.2, 0.95, 0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.6,1,5)

    glVertex3f(-0.03, 0.03,0.0)
    glVertex3f(0.03, 0.03,0.0)
    glVertex3f(0.03, -0.03,0.0)
    glVertex3f(-0.03, -0.03,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.65, 1, 0)
    glBegin(GL_QUADS)
    glColor3f(0.6,0.85,1,5)

    glVertex3f(-0.08, 0.08,0.0)
    glVertex3f(0.08, 0.08,0.0)
    glVertex3f(0.08, -0.08,0.0)
    glVertex3f(-0.08, -0.08,0.0)
    glEnd()
    glPopMatrix()


def draw():
    decoracion()
    draw_fondo()
    draw_inicio()
    limites.draw_ganar()
    
    limites.draw_pared()
    limites.draw_pared_2()
    limites. draw_pared_3()
    limites.draw_pared_4()
    # draw_enemigos()
    # draw_triangulo()
    # draw_enemigos_2()
    # draw_cuadrado()
    jugador.dibujar()
    triangulo.dibujar()
    enemigo.dibujar()

def main():
    global window

    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.6,0.7,1,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        actualizar()
        draw()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()