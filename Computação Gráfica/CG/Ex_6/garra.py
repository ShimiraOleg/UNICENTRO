from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.VERSION.GL_1_0 import glVertex3f

anguloMaoGarra = 20
anguloBracoY = 0
anguloBracoX = 0
anguloBracoZ = 0

def wirebox(dx, dy, dz):
    glPushMatrix()
    glTranslatef(dx/2, 0, 0)
    glScalef(dx, dy, dz)
    glutWireCube(1)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0.0, 0.0, -8.0)
    glRotatef(anguloBracoZ, 0.0, 0.0, 1.0)
    glRotatef(anguloBracoY, 0.0, 1.0, 0.0)
    glRotatef(anguloBracoX, 1.0, 0.0, 0.0)
    wirebox(2.0, 0.4, 1.0)
    glTranslatef(2.0, 0.0, 0.0)
    glPushMatrix()
    glRotatef(anguloMaoGarra, 0.0, 0.0, 1.0)
    wirebox(2.0, 0.4, 1.0)
    glPopMatrix()
    glPushMatrix()
    glRotatef(-anguloMaoGarra, 0.0, 0.0, 1.0)
    wirebox(2.0, 0.4, 1.0)
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60.0, 1.0, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global anguloMaoGarra, anguloBracoY, anguloBracoX, anguloBracoZ
    match key:
        case b'\x1b':
            glutDestroyWindow(glutGetWindow)
        case b'a':
            if anguloMaoGarra == 40:
                anguloMaoGarra = 40
            else:
                anguloMaoGarra += 1
        case b'd':
            if anguloMaoGarra == 6:
                anguloMaoGarra = 6
            else:
                anguloMaoGarra -= 1
        case b'z':
            anguloBracoZ += 1
        case b'x':
            anguloBracoZ -= 1
        case b'q':
            anguloBracoY += 1
        case b'e':
            anguloBracoY -= 1
        case b'w':
            anguloBracoX += 1
        case b's':
            anguloBracoX -= 1
        
    if key != b'\x1b':
        glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(750, 750)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Garra")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()
