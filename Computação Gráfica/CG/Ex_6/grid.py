from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

distance, azimuth, incidence, twist = 0, 0, 0, 0
ortho_mode = False 

def setup_projection():
    global ortho_mode
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    
    width, height = 750, 750
    aspect = width / height

    if ortho_mode:
        glOrtho(-10.0 * aspect, 10.0 * aspect, -10.0, 10.0, 1.0, 50.0)
    else:
        gluPerspective(45.0, aspect, 1.0, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)

def draw_grid():
    glColor3f(1.0, 1.0, 1.0)
    lines = 5    
    gap = 1.0    
    glBegin(GL_LINES)
    for i in range(-lines, lines + 1):
        glVertex3f(i * gap, -lines * gap, 0)
        glVertex3f(i * gap, lines * gap, 0)
        glVertex3f(-lines * gap, i * gap, 0)
        glVertex3f(lines * gap, i * gap, 0)
    glEnd()

def polarView():
    glTranslate(0.0, 0.0, -distance)
    glRotatef(-twist, 0.0, 0.0, 1.0)
    glRotatef(-incidence, 1.0, 0.0, 0.0) 
    glRotatef(-azimuth, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)
    polarView() 
    draw_grid()
    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    setup_projection()

def keyboard(key, x, y):
    global distance, incidence, twist, ortho_mode
    
    match key:
        case b'\x1b':
            os._exit(0)
        case b'w':
            incidence -= 5
        case b's': 
            incidence += 5
        case b'p': #'p' alterna entre projeções
            ortho_mode = not ortho_mode
            setup_projection()
        case b'z':
            distance -= 1
        case b'x':
            distance += 1
            
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(750, 750)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Grade e Projecoes")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()