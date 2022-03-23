from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Jugador import *
from Enemigo import *
from Triangulo import *

jugador = Jugador()
enemigo = Enemigo()
triangulo = Triangulo()

velocidad = 0.4
posicion_cuadrado = [-0.7, 0.7, 0.0]
posicion_triangulo = 0.0
angulo_triangulo = 0.0
# fase = 90.0
velocidad_rotacion_triangulo = 400.0
window = None

tiempo_anterior = 0.0

# Unidades por segundo
velocidad_enemigos = 4.3

#Direcciones
direccion_enemigos = 1
direccion_triangulo = 0
direccion_enemigos_2 = 1

# Posicion
posicion_pared= [0.0, 0.8, 0.0]
posicion_pared_2= [-0.8, 0.0, 0.0]
posicion_pared_3= [0.8, 0.0, 0.0]
posicion_pared_4 = [0.0, -0.8, 0.0]

posicion_ganar = [0.7,-0.7,0]

avanzar = True

# Enemigos
posicion_enemigos = 0.0

def actualizar_triangulo(tiempo_delta):
    global direccion_triangulo
    global velocidad_enemigos
    global posicion_enemigos
    global direccion_enemigos_2
    global tiempo_anterior
    global window
    global posicion_triangulo
    global posicion_cuadrado
    global angulo_triangulo

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Revisamos estados y realizamos acciones
    cantidad_movimiento = velocidad * tiempo_delta

    cantidad_rotacion = velocidad_rotacion_triangulo * tiempo_delta
    if direccion_triangulo == 0:
        angulo_triangulo = angulo_triangulo + cantidad_rotacion
        posicion_triangulo = posicion_triangulo - cantidad_movimiento
        if angulo_triangulo > 360.0:
            angulo_triangulo = angulo_triangulo - 360.0 
    if direccion_triangulo == 1:
        angulo_triangulo = angulo_triangulo - cantidad_rotacion
        posicion_triangulo = posicion_triangulo + cantidad_movimiento
        if angulo_triangulo < 0.0:
            angulo_triangulo = angulo_triangulo + 360.0
    if posicion_triangulo <= -0.75 and direccion_triangulo == 0:
        direccion_triangulo = 1

    if posicion_triangulo >= 0.75 and direccion_triangulo == 1:
        direccion_triangulo = 0

    tiempo_anterior = tiempo_actual
    

def actualizar_cuadrado(tiempo_delta):
    global direccion_enemigos
    global velocidad_enemigos
    global posicion_enemigos
    global direccion_enemigos_2

    cantidad_movimiento = velocidad_enemigos * tiempo_delta
    
    if direccion_enemigos == 0:
        posicion_enemigos = posicion_enemigos - cantidad_movimiento
    elif direccion_enemigos == 1:
        posicion_enemigos = posicion_enemigos + cantidad_movimiento
    
    if posicion_enemigos <= -0.75 and direccion_enemigos == 0:
        direccion_enemigos = 1

    if posicion_enemigos >= 0.75 and direccion_enemigos == 1:
        direccion_enemigos = 0



def actualizar():
    global tiempo_anterior
    global window
    global posicion_pared
    global posicion_cuadrado

    global posicion_enemigos
    global posicion_enemigos_2

    tiempo_actual = glfw.get_time()
    # Cuanto tiempo paso entre la ejecucion actual
    # y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior
    
    # Revisamos estados y realizamos acciones
    cantidad_movimiento = velocidad * tiempo_delta

    # Controles jugador
    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_A)

    if estado_tecla_w == glfw.PRESS:
        if not colisionando():
            posicion_cuadrado[1] = posicion_cuadrado[1] + cantidad_movimiento
        else:
            posicion_cuadrado = [-0.7, 0.7, 0.0]
    if estado_tecla_s == glfw.PRESS:
        if not colisionando():
            posicion_cuadrado[1] = posicion_cuadrado[1] - cantidad_movimiento
        else:
            posicion_cuadrado = [-0.7, 0.7, 0.0]
    if estado_tecla_a == glfw.PRESS:
        if not colisionando():
            posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
        else:
            posicion_cuadrado = [-0.7, 0.7, 0.0]
    if estado_tecla_d == glfw.PRESS:
        if not colisionando():
            posicion_cuadrado[0] = posicion_cuadrado[0] - cantidad_movimiento
        else:
            posicion_cuadrado = [-0.7, 0.7, 0.0]


    if colision_enemigos():
        posicion_cuadrado = [-0.7, 0.7, 0.0]


    actualizar_cuadrado(tiempo_delta)
    actualizar_triangulo(tiempo_delta)
    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    colision_ganar = False

    if (posicion_pared[0] + 0.43 >= posicion_cuadrado[0] - 0.43
        and posicion_pared[0] - 0.43 <= posicion_cuadrado[0] + 0.43
        and posicion_pared[1] + 0.03 >= posicion_cuadrado[1] - 0.03
        and posicion_pared[1] - 0.03 <= posicion_cuadrado[1] + 0.03):
        colisionando = True
    

    if (posicion_pared_2[0] + 0.03 >= posicion_cuadrado[0] - 0.03
        and posicion_pared_2[0] - 0.03 <= posicion_cuadrado[0] + 0.03
        and posicion_pared_2[1] + 0.43 >= posicion_cuadrado[1] - 0.43
        and posicion_pared_2[1] - 0.43 <= posicion_cuadrado[1] + 0.43):
        colisionando = True
    

    if (posicion_pared_3[0] + 0.03 >= posicion_cuadrado[0] - 0.03
        and posicion_pared_3[0] - 0.03 <= posicion_cuadrado[0] + 0.03
        and posicion_pared_3[1] + 0.43 >= posicion_cuadrado[1] - 0.43
        and posicion_pared_3[1] - 0.43 <= posicion_cuadrado[1] + 0.43):
        colisionando = True


    if (posicion_pared_4[0] + 0.43 >= posicion_cuadrado[0] - 0.43
        and posicion_pared_4[0] - 0.43 <= posicion_cuadrado[0] + 0.43
        and posicion_pared_4[1] + 0.03 >= posicion_cuadrado[1] - 0.03
        and posicion_pared_4[1] - 0.03 <= posicion_cuadrado[1] + 0.03):
        colisionando = True

    return colisionando

def colision_ganar():
    colision_ganar = False

    if (posicion_ganar[0] + 0.075 >= posicion_cuadrado[0] - 0.075
        and posicion_ganar[0] - 0.075 <= posicion_cuadrado[0] + 0.075
        and posicion_ganar[1] + 0.075 >= posicion_cuadrado[1] - 0.075
        and posicion_ganar[1] - 0.075 <= posicion_cuadrado[1] + 0.075):
        colision_ganar = True
    return colision_ganar

def colision_enemigos():
    # Colisión enemigos
    colision_enemigos = False

    if (posicion_enemigos + 0.05 >= posicion_cuadrado[0] - 0.05
        and posicion_enemigos - 0.05 <= posicion_cuadrado[0] + 0.05
        and posicion_enemigos + 0.05 >= posicion_cuadrado[1] - 0.05
        and posicion_enemigos - 0.05 <= posicion_cuadrado[1] + 0.05):
        colision_enemigos = True
    return colision_enemigos

# def draw_triangulo():
#     global posicion_triangulo
#     glPushMatrix()
#     glTranslatef(-posicion_triangulo, 0.91,0.0)
#     glRotatef(angulo_triangulo, 0.0, 0.0, 1.0)
#     glBegin(GL_TRIANGLES)

#     glColor3f(0.8,0.8,1,5)

#     #Manda vertices a dibujar
#     glVertex3f(-0.05,-0.05,0)
#     glVertex3f(0.0,0.05,0)
#     glVertex3f(0.05,-0.05,0)

#     glEnd()

#     glPopMatrix()


def draw_pared():
    global posicion_pared

    glPushMatrix()
    glTranslatef(posicion_pared[0], posicion_pared[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(-0.8, 0.01,0.0)
    glVertex3f(0.8, 0.01,0.0)
    glVertex3f(0.8, -0.01,0.0)
    glVertex3f(-0.8, -0.01,0.0)

    glEnd()

    glPopMatrix()

def draw_pared_2():
    global posicion_pared_2

    glPushMatrix()
    glTranslatef(posicion_pared_2[0], posicion_pared_2[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(-0.01, 0.8,0.0)
    glVertex3f(0.01, 0.8,0.0)
    glVertex3f(0.01, -0.8,0.0)
    glVertex3f(-0.01, -0.8,0.0)
    glEnd()

    glPopMatrix()

def draw_pared_3():
    global posicion_pared_3

    glPushMatrix()
    glTranslatef(posicion_pared_3[0], posicion_pared_3[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(-0.01, 0.8,0.0)
    glVertex3f(0.01, 0.8,0.0)
    glVertex3f(0.01, -0.8,0.0)
    glVertex3f(-0.01, -0.8,0.0)
    glEnd()

    glPopMatrix()

def draw_pared_4():
    global posicion_pared_4

    glPushMatrix()
    glTranslatef(posicion_pared_4[0], posicion_pared_4[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0,0,0)
    glVertex3f(-0.8, 0.01,0.0)
    glVertex3f(0.8, 0.01,0.0)
    glVertex3f(0.8, -0.01,0.0)
    glVertex3f(-0.8, -0.01,0.0)

    glEnd()
    glPopMatrix()

def draw_ganar():

    global posicion_ganar

    glPushMatrix()
    glTranslatef(posicion_ganar[0], posicion_ganar[1], 0.0)
    glBegin(GL_QUADS)
    glColor(0.2,1.0,0.7)
    glVertex3f(0.1, -0.1, 0)
    glVertex3f(0.1, 0.1, 0)
    glVertex3f(-0.1, 0.1, 0)
    glVertex3f(-0.1, -0.1, 0)
    if colision_ganar():
        glfw.destroy_window(window)
    glEnd()

    glPopMatrix()

def draw_inicio():

    glBegin(GL_QUADS)
    glColor(0.2,1.0,0.7)
    glVertex3f(-0.6, 0.6, 0)
    glVertex3f(-0.6, 0.8, 0)
    glVertex3f(-0.8, 0.8, 0)
    glVertex3f(-0.8, 0.6, 0)
    glEnd()

def draw_enemigos():
    global posicion_enemigos
    glPushMatrix()
    
    glTranslatef(posicion_enemigos, posicion_enemigos, 0.0)
    glBegin(GL_POLYGON)
    glColor3f(0.2,0.2,0.9)

    glVertex3f(-0.05, 0.05,0.0)
    glVertex3f(0.05, 0.05,0.0)
    glVertex3f(0.05, -0.05,0.0)
    glVertex3f(-0.05, -0.05,0.0)
    glEnd()
    glPopMatrix()

# Juagdor
# def draw_cuadrado():

#     glPushMatrix()
#     glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
#     glBegin(GL_QUADS)
#     if colisionando():
#         glColor3f(0,0,1)
#     else:
#         glColor3f(1,0,0)
#     glVertex3f(-0.05, 0.05,0.0)
#     glVertex3f(0.05, 0.05,0.0)
#     glVertex3f(0.05, -0.05,0.0)
#     glVertex3f(-0.05, -0.05,0.0)
#     glEnd()

#     glBegin(GL_LINE_LOOP)
#     glColor(0,0,0)
#     glVertex3f(-0.05, -0.05, 0)
#     glVertex3f(-0.05, 0.05, 0)
#     glVertex3f(0.05, 0.05, 0)
#     glVertex3f(0.05, -0.05, 0)
#     glEnd()

#     glPopMatrix()

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
    draw_ganar()
    
    draw_pared()
    draw_pared_2()
    draw_pared_3()
    draw_pared_4()
    # draw_enemigos()
    # draw_triangulo()
    # draw_enemigos_2()
    # draw_cuadrado()
    jugador.dibujar()
    triangulo.dibujar()
    enemigo.dibujar()
    # triangulo.draw_triangulo()

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