from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPiso():
    glColor3f(0.584,0.9294,0.682)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.65,0.0)
    glVertex3f(1.0,-0.65,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarTecho():
    glBegin(GL_TRIANGLES)
    glColor3f(1,0.3607,0.5215)
    glVertex3f(-0.2,-0.1,0.0)
    glVertex3f(0.3,0.2,0.0)
    glVertex3f(0.8,-0.1,0.0)
    glEnd()

def dibujarCasa():
    glBegin(GL_QUADS)
    glColor3f(1,0.4784,0.7647)
    glVertex3f(-0.2,-.1,0.0)
    glVertex3f(0.8,-.1,0.0)
    glVertex3f(0.8,-0.7,0.0)
    glVertex3f(-0.2,-0.7,0.0)
    glEnd()

def dibujarSol():
    glColor3f(1,0.9725,0.4784)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 -.55, sin(angulo) * 0.15 +0.65, 0.0)
    glEnd()

def dibujarSol2():
    glColor3f(1,0.792,0.4784)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5,0.9,0.0)
    glVertex3f(-0.8,0.55,0.0)
    glVertex3f(-0.3,0.5,0.0)
    glEnd()

def dibujarSol3():
    glColor3f(1,0.792,0.4784)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.7,0.85,0.0)
    glVertex3f(-0.68,0.4,0.0)
    glVertex3f(-0.25,0.7,0.0)
    glEnd()
    
def dibujarSol4():
    glColor3f(1,0.792,0.4784)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.8,0.72,0.0)
    glVertex3f(-0.48,0.4,0.0)
    glVertex3f(-0.33,0.85,0.0)
    glEnd()

def dibujarPuerta():
    glBegin(GL_QUADS)
    glColor3f(1,0.3607,0.5215)
    glVertex3f(0.4,-0.4,0.0)
    glVertex3f(0.6,-0.4,0.0)
    glVertex3f(0.6,-0.7,0.0)
    glVertex3f(0.4,-0.7,0.0)
    glEnd()
    
def dibujarPerilla():
    glColor3f(1,0.4784,0.7647)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.03 +.55, sin(angulo) * 0.03 -0.55, 0.0)
    glEnd()

def dibujarVentana1():
    glBegin(GL_QUADS)
    glColor3f(1,0.3607,0.5215)
    glVertex3f(-.1,-.5,0.0)
    glVertex3f(0.3,-.5,0.0)
    glVertex3f(0.3,-0.3,0.0)
    glVertex3f(-0.1,-0.3,0.0)
    glEnd()

def dibujarVentana2():
    glBegin(GL_QUADS)
    glColor3f(0.584,0.917,0.9294)
    glVertex3f(-.08,-.48,0.0)
    glVertex3f(0.28,-.48,0.0)
    glVertex3f(0.28,-0.32,0.0)
    glVertex3f(-0.08,-0.32,0.0)
    glEnd()


def dibujarArbol1():
    glBegin(GL_QUADS)
    glColor3f(0.4705,0.349,0.207)
    glVertex3f(-0.6,-0.4,0.0)
    glVertex3f(-0.5,-0.4,0.0)
    glVertex3f(-0.5,-0.7,0.0)
    glVertex3f(-0.6,-0.7,0.0)
    glEnd()

def dibujarArbol2():
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.28 -.55, sin(angulo) * 0.28 -.2, 0.0)
    glEnd()

def dibujarNube1():
    glColor3f(0.89,1,0.99)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 +.1, sin(angulo) * 0.1 +.7, 0.0)
    glEnd()


def dibujarNube2():
    glColor3f(0.89,1,0.99)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 +.8, sin(angulo) * 0.1 +.3, 0.0)
    glEnd()

def dibujarNube3():
    glColor3f(0.89,1,0.99)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.13 -.25, sin(angulo) * 0.08 +.2, 0.0)
    glEnd()



def dibujar():
    dibujarPiso()
    dibujarSol2()
    dibujarSol3()
    dibujarSol4()
    dibujarSol()
    dibujarCasa()
    dibujarTecho()
    dibujarPuerta()
    dibujarPerilla()
    dibujarVentana1()
    dibujarVentana2()
    dibujarArbol1()
    dibujarArbol2()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()


def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(900,900,"Mi ventana", None, None)

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
        glViewport(0,0,900,900)
        #Establece color de borrado
        glClearColor(0.584,0.917,0.9294,1)
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