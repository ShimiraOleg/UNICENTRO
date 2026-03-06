from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
import math

cam_pos = [0.0, 5.0, 20.0]
cam_yaw = -90.0
cam_pitch = 0.0
last_x, last_y = 0, 0
mouse_down = False
current_button = -1
sensitivity = 0.2
speed = 0.5  

textures = {}
planet_data = {
    "mercurio": {"dist": 3, "radius": 0.3, "speed": 4.0},
    "venus":   {"dist": 5, "radius": 0.5, "speed": 3.0},
    "terra":   {"dist": 7, "radius": 0.5, "speed": 2.5},
    "marte":    {"dist": 9, "radius": 0.4, "speed": 2.0},
    "jupiter": {"dist": 13, "radius": 1.2, "speed": 1.0},
    "saturno":  {"dist": 17, "radius": 1.0, "speed": 0.8},
    "uranus":  {"dist": 21, "radius": 0.8, "speed": 0.6},
    "netuno": {"dist": 24, "radius": 0.8, "speed": 0.4}
}

texture_files = {
    "sol": "sol.jpg",
    "mercurio": "mercurio.jpg",
    "venus": "venus.webp",
    "terra": "terra.jpg",
    "moon": "lua.jpg",
    "marte": "marte.webp",
    "jupiter": "jupiter.jpg",
    "saturno": "saturno.jpg",
    "anel": "aneis.jpg",
    "urano": "urano.jpg",
    "netuno": "netuno.jpg",
    "espaco": "space.png"
}

def load_texture(name, filename):
    try:
        path = f'img/{filename}'
        img = cv2.imread(path)
        if img is None:
            print(f"Aviso: Imagem não encontrada: {path}")
            return
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.flip(img, 0)
        height, width, _ = img.shape
        img_data = img.tobytes()
        
        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        
        textures[name] = tex_id
    except Exception as e:
        print(f"Erro ao processar textura {name}: {e}")

def init_textures():
    for name, filename in texture_files.items():
        load_texture(name, filename)

def drawSphere(radius, slices, stacks, texture_name):
    if texture_name in textures:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[texture_name])
    else:
        glDisable(GL_TEXTURE_2D)
        
    quadObj = gluNewQuadric()
    gluQuadricDrawStyle(quadObj, GLU_FILL)
    gluQuadricNormals(quadObj, GLU_SMOOTH)
    gluQuadricTexture(quadObj, True)
    gluSphere(quadObj, radius, slices, stacks)

def draw_saturn_anel(radius):
    glPushMatrix()
    glScalef(1, 1, 0.1)
    if "anel" in textures:
        glBindTexture(GL_TEXTURE_2D, textures["anel"])
    glutSolidTorus(0.2, radius + 0.5, 20, 20)
    glPopMatrix()

def draw_skybox():
    glDisable(GL_LIGHTING)
    glDepthMask(GL_FALSE)    
    glPushMatrix()
    glTranslatef(cam_pos[0], cam_pos[1], cam_pos[2])    
    if "espaco" in textures:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures["espaco"])
        glColor3f(1,1,1)
    
    quadObj = gluNewQuadric()
    gluQuadricTexture(quadObj, True)
    gluQuadricOrientation(quadObj, GLU_INSIDE) 
    gluSphere(quadObj, 80.0, 40, 40)
    glPopMatrix()
    glDepthMask(GL_TRUE)
    glEnable(GL_LIGHTING)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global_time = glutGet(GLUT_ELAPSED_TIME) / 8000.0
    
    glLoadIdentity()
    rad_yaw = math.radians(cam_yaw)
    rad_pitch = math.radians(cam_pitch)
    
    front_x = math.cos(rad_yaw) * math.cos(rad_pitch)
    front_y = math.sin(rad_pitch)
    front_z = math.sin(rad_yaw) * math.cos(rad_pitch)
    
    target_x = cam_pos[0] + front_x
    target_y = cam_pos[1] + front_y
    target_z = cam_pos[2] + front_z
    
    gluLookAt(cam_pos[0], cam_pos[1], cam_pos[2],
              target_x, target_y, target_z,
              0, 1, 0)

    draw_skybox()
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])    
    glMaterialfv(GL_FRONT, GL_EMISSION, [1, 1, 0.8, 1])
    glPushMatrix()
    glRotatef(global_time * 10, 0, 1, 0)
    drawSphere(2.0, 40, 40, "sol")
    glPopMatrix()    
    glMaterialfv(GL_FRONT, GL_EMISSION, [0, 0, 0, 1])
    names = ["mercurio", "venus", "terra", "marte", "jupiter", "saturno", "uranus", "netuno"]
    for name in names:
        data = planet_data[name]
        glPushMatrix()
        angle = global_time * data["speed"]
        glTranslatef(math.cos(angle) * data["dist"], 0, math.sin(angle) * data["dist"])
        glPushMatrix()
        glRotatef(global_time * 50, 0, 1, 0)
        drawSphere(data["radius"], 20, 20, name)
        glPopMatrix()
        
        if name == "terra":
            glPushMatrix()
            moon_angle = global_time * 8.0
            glRotatef(45, 1, 0, 0)
            glTranslatef(1.0 * math.cos(moon_angle), 0, 1.0 * math.sin(moon_angle))
            drawSphere(0.15, 10, 10, "moon")
            glPopMatrix()            
        if name == "saturno":
            glPushMatrix()
            glRotatef(45, 1, 0, 0)
            draw_saturn_anel(data["radius"])
            glPopMatrix()
        glPopMatrix()
    glutSwapBuffers()

def mouse_click(button, state, x, y):
    global last_x, last_y, mouse_down, current_button
    if state == GLUT_DOWN:
        mouse_down = True
        current_button = button
        last_x = x
        last_y = y
    elif state == GLUT_UP:
        mouse_down = False
        current_button = -1

def mouse_motion(x, y):
    global cam_yaw, cam_pitch, last_x, last_y
    if not mouse_down:
        return
    dx = x - last_x
    dy = y - last_y 
    if current_button == GLUT_LEFT_BUTTON:
        cam_yaw += dx * sensitivity
        cam_pitch -= dy * sensitivity
        if cam_pitch > 89.0: cam_pitch = 89.0
        if cam_pitch < -89.0: cam_pitch = -89.0

    last_x = x
    last_y = y    
    glutPostRedisplay()

def keyboard(key, x, y):
    global cam_pos
    rad_yaw = math.radians(cam_yaw)
    rad_pitch = math.radians(cam_pitch)
    front_x = math.cos(rad_yaw) * math.cos(rad_pitch)
    front_y = math.sin(rad_pitch)
    front_z = math.sin(rad_yaw) * math.cos(rad_pitch)
    right_x = math.sin(rad_yaw - 3.1415/2)
    right_z = -math.cos(rad_yaw - 3.1415/2)
    
    match key:
        case b'\x1b': glutLeaveMainLoop()
        case b'w':
            cam_pos[0] += front_x * speed
            cam_pos[1] += front_y * speed
            cam_pos[2] += front_z * speed
        case b's':
            cam_pos[0] -= front_x * speed
            cam_pos[1] -= front_y * speed
            cam_pos[2] -= front_z * speed
        case b'a': 
            cam_pos[0] -= right_x * speed
            cam_pos[2] -= right_z * speed
        case b'd':
            cam_pos[0] += right_x * speed
            cam_pos[2] += right_z * speed
        case b'q':
            cam_pos[1] += speed
        case b'e':
            cam_pos[1] -= speed

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.0, 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_TEXTURE_2D)    
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    
    init_textures()

def idle():
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Sistema Solar")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse_click)  
    glutMotionFunc(mouse_motion)
    glutIdleFunc(idle)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()