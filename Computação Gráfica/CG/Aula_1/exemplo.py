from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.VERSION.GL_1_0 import glVertex3f
import cv2

distance, azimuth, incidence, twist, = 0,0,0,0
textura = 0

def criaTextura():
    global textura
    img = cv2.imread("img/andre.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.flip(img,0)
    height, width, _ = img.shape
    img_data = img.tobytes()

    textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB,
    GL_UNSIGNED_BYTE, img_data)


def polarView():
    glTranslate(0.0, 0.0, -distance)
    glRotatef(-twist, 0.0, 0.0, 1.0)
    glRotatef(-incidence, 1.0, 0.0, 0.0)
    glRotatef(-azimuth, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    gluLookAt(0,0,2, 0,0,0, 0,1,0)
    polarView() 
    glBindTexture(GL_TEXTURE_2D, textura)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(0, 0, 0) 
    glTexCoord2f(0, 1); glVertex3f(0, 1, 0)
    glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
    glTexCoord2f(1, 0); glVertex3f(1, 0, 0)
    glEnd()
    glutSwapBuffers()

def init():
    # Define a cor de fundo preta
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Inicializa as matrizes do OpenGL
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    gluPerspective(45.0, 1.0, 1.0, 5.0)
    gluLookAt(0,0,2,0,0,0,0,1,0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_TEXTURE_2D)
    criaTextura()


def keyboard(key, x, y):
    global distance, azimuth, incidence, twist
    match key:
        case b'\x1b':
            glutDestroyWindow(glutGetWindow)
        case b'a':
            azimuth -= 10
        case b'd':
            azimuth += 10
        case b'w':
            incidence -= 10
        case b's':
            incidence += 10
        case b'q':
            twist -= 10
        case b'e':
            twist += 10
        case b'z':
            distance -= 1
        case b'x':
            distance += 1
    if key != b'\x1b':
        glutPostRedisplay()

def keySpecial(key, x,y):
    if key == GLUT_KEY_LEFT:
        print("Seta Esquerda")
    elif key == GLUT_KEY_RIGHT:
        print("Seta Direira")

    if glutGetModifiers == GLUT_ACTIVE_ALT:
        print("Alt")
    
    if glutGetModifiers == GLUT_ACTIVE_CTRL:
        print("Ctrl")
    
    if glutGetModifiers == GLUT_ACTIVE_SHIFT:
        print("Shift")

def mouse(b,s,x,y):
    match b:
        case GLUT_LEFT_BUTTON:
            if s == GLUT_DOWN:
                print("Botão Pressionado",x,y)
            elif s == GLUT_UP:
                print("Botão Liberado",x,y)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(750, 750)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Hello world!")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(keySpecial)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)

    glutMainLoop()
    

if __name__ == "__main__":
    main()