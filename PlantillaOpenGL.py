from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *


##DIBUJAR PASTO

def dibujarPasto():
    #Dibujar pasto
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.7,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()


##DIBUJAR EL SOL

def dibujarSol():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 -.6, sin(angulo) * 0.2 +0.7, 0.0)
    glEnd()

def dibujarLineasSol():
    glBegin(GL_LINES)
    #Linea de abajo
    glVertex3f(-0.6,0.5,0.0)
    glVertex3f(-0.6,0.3,0.0)
    #Linea de abajo derecha
    glVertex3f(-0.5,0.6,0.0)
    glVertex3f(-0.3,0.4,0.0)
    #Linea derecha
    glVertex3f(-0.4,0.7,0.0)
    glVertex3f(-0.2,0.7,0.0)
    #Linea de arriba derecha
    glVertex3f(-0.5,0.8,0.0)
    glVertex3f(-0.3,1,0.0)
    #Linea de arriba
    glVertex3f(-0.6,0.8,0.0)
    glVertex3f(-0.6,1,0.0)
    #Linea de arriba izquierda
    glVertex3f(-0.7,0.8,0.0)
    glVertex3f(-0.9,1,0.0)
    #Linea de izquierda
    glVertex3f(-0.8,0.7,0.0)
    glVertex3f(-1,0.7,0.0)
    #Linea de abajo derecha
    glVertex3f(-0.7,0.6,0.0)
    glVertex3f(-0.9,0.4,0.0)
    glEnd()


##DIBUJAR LA CASA

def dibujarCasa():
    glBegin(GL_QUADS)
    glColor3f(0.6392,0.3647,0.3450)
    glVertex3f(-0.2,0.1,0.0)
    glVertex3f(0.8,0.1,0.0)
    glVertex3f(0.8,-0.8,0.0)
    glVertex3f(-0.2,-0.8,0.0)
    glEnd()

def dibujarTecho():
    glBegin(GL_TRIANGLES)
    glColor3f(0.8,0,0)
    glVertex3f(-0.3,0.1,0.0)
    glVertex3f(0.3,0.5,0.0)
    glVertex3f(0.9,0.1,0.0)
    glEnd()

def dibujarPuerta():
    glBegin(GL_QUADS)
    glColor3f(0.388,0.219,0.207)
    glVertex3f(0.1,-0.4,0.0)
    glVertex3f(0.5,-0.4,0.0)
    glVertex3f(0.5,-0.8,0.0)
    glVertex3f(0.1,-0.8,0.0)
    glEnd()
    
def dibujarPerilla():
    glColor3f(.32,.32,.32)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 +.45, sin(angulo) * 0.04 -0.6, 0.0)
    glEnd()


##DIBUJAR LA VENTANA

def dibujarVentana():
    glBegin(GL_QUADS)
    glColor3f(.32,.32,.32)
    glVertex3f(0.1,-.3,0.0)
    glVertex3f(0.5,-.3,0.0)
    glVertex3f(0.5,0,0.0)
    glVertex3f(0.1,0,0.0)
    glEnd()

def dibujarVidrio1():
    #Vidrio abajo izquierda
    glBegin(GL_QUADS)
    glColor3f(0,0.9,1.0)
    glVertex3f(0.12,-.28,0.0)
    glVertex3f(0.28,-.28,0.0)
    glVertex3f(0.28,-.17,0.0)
    glVertex3f(0.12,-.17,0.0)
    glEnd()

def dibujarVidrio2():
    #vidrio abajo derecha
    glBegin(GL_QUADS)
    glColor3f(0,0.9,1.0)
    glVertex3f(0.48,-.28,0.0)
    glVertex3f(0.31,-.28,0.0)
    glVertex3f(0.31,-.17,0.0)
    glVertex3f(0.48,-.17,0.0)
    glEnd()

def dibujarVidrio3():
    #Vidrio abajo izquierda
    glBegin(GL_QUADS)
    glColor3f(0,0.9,1.0)
    glVertex3f(0.12,-0.03,0.0)
    glVertex3f(0.28,-0.03,0.0)
    glVertex3f(0.28,-.14,0.0)
    glVertex3f(0.12,-.14,0.0)
    glEnd()

def dibujarVidrio4():
    #vidrio abajo derecha
    glBegin(GL_QUADS)
    glColor3f(0,0.9,1.0)
    glVertex3f(0.48,-0.03,0.0)
    glVertex3f(0.31,-0.03,0.0)
    glVertex3f(0.31,-.14,0.0)
    glVertex3f(0.48,-.14,0.0)
    glEnd()


##DIBUJAR EL ARBOL

def dibujarTroncoArbol():
    glBegin(GL_QUADS)
    glColor3f(0.388,0.219,0.207)
    glVertex3f(-0.7,-0.4,0.0)
    glVertex3f(-0.6,-0.4,0.0)
    glVertex3f(-0.6,-0.8,0.0)
    glVertex3f(-0.7,-0.8,0.0)
    glEnd()

def dibujarArbol1():
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.22 -.6, sin(angulo) * 0.22 -.2, 0.0)
    glEnd()

def dibujarArbol2():
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 -.8, sin(angulo) * 0.15 -.4, 0.0)
    glEnd()

def dibujarArbol3():
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 -.5, sin(angulo) * 0.18 -.4, 0.0)
    glEnd()

##DIBUJAR LAS NUBES

def dibujarNube1():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 +.1, sin(angulo) * 0.05 +.7, 0.0)
    glEnd()

def dibujarNube2():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 +.2, sin(angulo) * 0.05 +.76, 0.0)
    glEnd()

def dibujarNube3():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 +.8, sin(angulo) * 0.05 +.6, 0.0)
    glEnd()

def dibujarNube4():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 +1, sin(angulo) * 0.05 +.54, 0.0)
    glEnd()

def dibujarNube5():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.13 -.78, sin(angulo) * 0.05 +.16, 0.0)
    glEnd()

def dibujarNube6():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.17 -.9, sin(angulo) * 0.05 +.1, 0.0)
    glEnd()


def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarSol()
    dibujarLineasSol()
    dibujarCasa()
    dibujarTecho()
    dibujarPuerta()
    dibujarPerilla()
    dibujarVentana()
    dibujarVidrio1()
    dibujarVidrio2()
    dibujarVidrio3()
    dibujarVidrio4()
    dibujarTroncoArbol()
    dibujarArbol1()
    dibujarArbol2()
    dibujarArbol3()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()
    dibujarNube4()
    dibujarNube5()
    dibujarNube6()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0,0.9,1.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()