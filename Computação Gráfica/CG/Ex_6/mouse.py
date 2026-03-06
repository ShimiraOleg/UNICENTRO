from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

distance, azimuth, incidence, twist = 0, 0, 0, 0
last_x, last_y = 0, 0
mouse_down = False
current_button = -1
shift_down = False

def setup_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.0, 1.0, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)

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
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(0, 0, 0) 
    glTexCoord2f(0, 1); glVertex3f(0, 1, 0)
    glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
    glTexCoord2f(1, 0); glVertex3f(1, 0, 0)
    glEnd()
    glutSwapBuffers()

def mouse_click(button, state, x, y):
    global last_x, last_y, mouse_down, current_button, shift_down
    
    if state == GLUT_DOWN:
        mouse_down = True
        current_button = button
        last_x = x
        last_y = y
        shift_down = (glutGetModifiers() & GLUT_ACTIVE_SHIFT) != 0

    elif state == GLUT_UP:
        mouse_down = False
        current_button = -1
        shift_down = False

def mouse_motion(x, y):
    global distance, azimuth, incidence, twist, last_x, last_y
    if not mouse_down:
        return
    dx = x - last_x
    dy = y - last_y
    if current_button == GLUT_LEFT_BUTTON and shift_down:
        twist += dx * 0.5
    elif current_button == GLUT_LEFT_BUTTON:
        azimuth += dx * 0.5
        incidence += dy * 0.5
    elif current_button == GLUT_RIGHT_BUTTON:
        distance += dy * 0.1
    last_x = x
    last_y = y    
    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    setup_projection()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(750, 750)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Mouse")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)  
    glutMotionFunc(mouse_motion)
    
    glutMainLoop()

if __name__ == "__main__":
    main()