import os
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math
from obj_loader import OBJLoader 

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
GAME_STATE = "MENU" 
SELECTED_MODE = 0 
GAME_MODE = 0     
OPTIONS = [
    "Fase 1: Coleta de Combustivel",
    "Fase 2: Desvio de Raios Solares",
    "Fase 3: Corrida Solar",
    "Como Jogar / Controles" 
]
FUEL = 100
MAX_FUEL = 100
FUEL_DECAY = 0.10
FUEL_RATE = 200
OBST_RATE = 200
FUEL_REWARD = 35
LIVES = 3
DISTANCE = 0.005
COLUMNS = [-5.0, -2.5, 0.0, 2.5, 5.0]
CURVATURE = 0.003

spawn_timer = 0
next_spawn_time = 30
current_lane_index = 2               
target_car_x = COLUMNS[current_lane_index]
car_x = COLUMNS[current_lane_index]  
car_rotation = 0.0
car_model = None
fuel_model = None      
obstacle_model = None 
speed = 0.5
sun_rotation = 0.0
track_offset = 0.0
texturas_ids = {}
font_cache = {}
skybox_rotation = 0.0
cam_azimuth = 0.0    
cam_incidence = 20.0 
cam_distance = 15.0  
mouse_is_down = False
mouse_btn_pressed = -1 

class GameItem:
    def __init__(self):
        self.x = 0.0
        self.z = 0.0
        self.type = ""
        self.active = False

POOL_SIZE = 20
item_pool = [GameItem() for _ in range(POOL_SIZE)]

def spawn_item_from_pool(lane, z_pos, item_type):
    for item in item_pool:
        if not item.active:
            item.x = lane
            item.z = z_pos
            item.type = item_type
            item.active = True
            return
    
    new_item = GameItem()
    new_item.x = lane
    new_item.z = z_pos
    new_item.type = item_type
    new_item.active = True
    item_pool.append(new_item)

def reset_items():
    for item in item_pool:
        item.active = False

def get_font(size):
    if size not in font_cache:
        font_cache[size] = pygame.font.SysFont("Arial", size, bold=True) if pygame.font.match_font("Arial") else pygame.font.Font(None, size)
    return font_cache[size]

def get_curve_y(z):
    return -0.5 + (z * z * CURVATURE)

def init_gl():
    global car_model, fuel_model, obstacle_model
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)    
    light_pos = [0.0, 10.0, 10.0, 1.0] 
    
    light_color = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (DISPLAY_WIDTH/DISPLAY_HEIGHT), 0.1, 2000.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_TEXTURE_2D)        
    car_model = OBJLoader("models/car/Deora_II.obj")
    fuel_model = OBJLoader("models/gas/jerrycan.obj")
    obstacle_model = OBJLoader("models/laser/Laser.obj") 
    load_texture('imgs/sol.jpg', 'sol')
    load_texture('imgs/space.jpg', 'espaco')

def load_texture(filename, tag_name):

    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()
        
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)        
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)        
    texturas_ids[tag_name] = tex_id


def draw_text(position, text_string, size=32, color=(255, 255, 255, 255)):
    font = get_font(size)
    
    surface_fg = font.render(text_string, True, color)
    data_fg = pygame.image.tostring(surface_fg, "RGBA", True)
    
    surface_black = font.render(text_string, True, (0, 0, 0, 255))
    data_black = pygame.image.tostring(surface_black, "RGBA", True)
    
    w, h = surface_fg.get_width(), surface_fg.get_height()

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glDisable(GL_DEPTH_TEST)  
    glDisable(GL_TEXTURE_2D)  
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)     
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)     
    
    offsets = [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    glColor4f(1.0, 1.0, 1.0, 1.0) 
    
    for dx, dy in offsets:
        glWindowPos2d(position[0] + dx, position[1] + dy)
        glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, data_black)

    glWindowPos2d(*position)
    glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, data_fg)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)

def draw_skybox():
    global skybox_rotation
    if 'espaco' not in texturas_ids: return

    glPushMatrix()
    glDepthMask(GL_FALSE) 
    glDisable(GL_LIGHTING) 
    glEnable(GL_TEXTURE_2D)
    
    glRotatef(skybox_rotation, 1.0, 0.0, 0.0)

    glBindTexture(GL_TEXTURE_2D, texturas_ids['espaco'])
    glColor3f(1.0, 1.0, 1.0)
    
    size = 1000.0 
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size); glTexCoord2f(1, 0); glVertex3f( size, -size, -size); glTexCoord2f(1, 1); glVertex3f( size,  size, -size); glTexCoord2f(0, 1); glVertex3f(-size,  size, -size)
    glTexCoord2f(0, 0); glVertex3f( size, -size,  size); glTexCoord2f(1, 0); glVertex3f(-size, -size,  size); glTexCoord2f(1, 1); glVertex3f(-size,  size,  size); glTexCoord2f(0, 1); glVertex3f( size,  size,  size)
    glTexCoord2f(0, 0); glVertex3f(-size, -size,  size); glTexCoord2f(1, 0); glVertex3f(-size, -size, -size); glTexCoord2f(1, 1); glVertex3f(-size,  size, -size); glTexCoord2f(0, 1); glVertex3f(-size,  size,  size)
    glTexCoord2f(0, 0); glVertex3f( size, -size, -size); glTexCoord2f(1, 0); glVertex3f( size, -size,  size); glTexCoord2f(1, 1); glVertex3f( size,  size,  size); glTexCoord2f(0, 1); glVertex3f( size,  size, -size)
    glTexCoord2f(0, 0); glVertex3f(-size,  size, -size); glTexCoord2f(1, 0); glVertex3f( size,  size, -size); glTexCoord2f(1, 1); glVertex3f( size,  size,  size); glTexCoord2f(0, 1); glVertex3f(-size,  size,  size)
    glTexCoord2f(0, 0); glVertex3f(-size, -size,  size); glTexCoord2f(1, 0); glVertex3f( size, -size,  size); glTexCoord2f(1, 1); glVertex3f( size, -size, -size); glTexCoord2f(0, 1); glVertex3f(-size, -size, -size)
    glEnd()
    
    glEnable(GL_LIGHTING)
    glDepthMask(GL_TRUE)
    glPopMatrix()

def draw_car():
    global car_model
    glPushMatrix()
    glTranslatef(car_x, -0.42, -5.0) 
    
    glColor3f(1.0, 1.0, 1.0) 
    glScalef(1.0, 1.0, 1.0) 
    glRotatef(180 + car_rotation, 0, 1, 0)    
    
    if car_model is not None:
        car_model.draw()
        
    glPopMatrix()

def draw_track():
    global track_offset
    glPushMatrix()
    glColor3f(0.8, 0.4, 0.0)  
      
    step = 2.0 
    start_z = 0.0
    end_z = -120.0  
    z = start_z
    while z > end_z:
        curr_z = z
        next_z = z - step
        y_curr = get_curve_y(curr_z)
        y_next = get_curve_y(next_z)
        
        glBegin(GL_QUADS)
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(-7.5, y_curr, curr_z) 
        glVertex3f( 7.5, y_curr, curr_z) 
        glVertex3f( 7.5, y_next, next_z) 
        glVertex3f(-7.5, y_next, next_z) 
        glEnd()
        
        z -= step
    glDisable(GL_TEXTURE_2D)
    glLineWidth(2.0)
    glColor3f(0.0, 0.0, 0.0)
    
    glBegin(GL_LINES)
    for x in [-7.5, -4.5, -1.5, 1.5, 4.5, 7.5]:
        z = start_z
        while z > end_z:
            curr_z = z
            next_z = z - step
            y_curr = get_curve_y(curr_z) + 0.02
            y_next = get_curve_y(next_z) + 0.02
            
            glVertex3f(x, y_curr, curr_z)
            glVertex3f(x, y_next, next_z)
            z -= step
    current_line_z = 0.0 + track_offset 
    while current_line_z > end_z:
        if current_line_z <= 0:
            y_line = get_curve_y(current_line_z) + 0.02
            glVertex3f(-7.5, y_line, current_line_z)
            glVertex3f( 7.5, y_line, current_line_z)
            
        current_line_z -= 5.0

    glEnd()
    glEnable(GL_TEXTURE_2D)
    glPopMatrix()

def draw_sun():
    global sun_rotation
    if 'sol' not in texturas_ids: return
    glPushMatrix()
    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texturas_ids['sol'])
    glTranslatef(0.0, 207.5, 25.0)
    glRotatef(sun_rotation, 1, 0, 0)
    glColor3f(1.0, 1.0, 1.0)     
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)  
    gluSphere(qobj, 200.0, 60, 60) 
    gluDeleteQuadric(qobj)
    glEnable(GL_LIGHTING)
    glPopMatrix()

def game_logic():
    global car_x, target_car_x, FUEL, LIVES, GAME_STATE, speed, car_rotation, track_offset, DISTANCE, sun_rotation, spawn_timer, next_spawn_time, GAME_MODE, skybox_rotation
    spawn_timer += 1
    
    diff = target_car_x - car_x
    car_x += diff * 0.1
    car_rotation = diff * -15.0

    speed_increase = int(DISTANCE) // 5
    speed = 0.5 + (speed_increase * 0.05)
    sun_rotation += speed * 0.05
    skybox_rotation += speed * 0.15 

    if GAME_MODE == 1: 
        pass
    else:
        FUEL -= FUEL_DECAY

    DISTANCE += (speed / 40.0) 

    if FUEL <= 0:
        GAME_STATE = "GAME_OVER"

    track_offset += speed
    if track_offset >= 5.0:
        track_offset = 0.0

    spawn_speed = int(60/speed)
    if spawn_speed < 20: spawn_speed = 20

    if spawn_timer > next_spawn_time:
        spawn_timer = 0        
        spawn_multiplier = 0.35
        if GAME_MODE == 0: 
            spawn_multiplier = 4.5
        elif GAME_MODE == 1: 
            spawn_multiplier = 0.25  

        base_interval = int((60 / speed) * spawn_multiplier)
        next_spawn_time = random.randint(int(base_interval * 0.5), int(base_interval * 1.5))        
        min_limit = 15
        if GAME_MODE == 1: min_limit = 8
        if next_spawn_time < min_limit: next_spawn_time = min_limit
        qtd_items = 2 if random.random() < 0.005 else 1
        lanes_escolhidas = random.sample(COLUMNS, qtd_items)
        
        for lane in lanes_escolhidas:
            item_type = ""
            if GAME_MODE == 0: 
                item_type = "fuel"
            elif GAME_MODE == 1: 
                item_type = "obstacle"
            else: 
                item_type = "fuel" if random.random() < 0.2 else "obstacle"

            offset_z = random.uniform(0, 20.0)
            spawn_item_from_pool(lane, -120.0 - offset_z, item_type)

    for item in item_pool:
        if not item.active: continue

        item.z += speed
        
        if item.z > -6.0 and (item.z - speed) < -4.0:
            if abs(item.x - car_x) < 0.8: 
                if item.type == "fuel":
                    FUEL += FUEL_REWARD
                    if FUEL > MAX_FUEL: FUEL = MAX_FUEL
                    item.active = False
                elif item.type == "obstacle":
                    LIVES -= 1
                    item.active = False
                    if LIVES <= 0:
                        GAME_STATE = "GAME_OVER"
        
        if item.z > 0:
            item.active = False

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    if GAME_STATE == "PAUSE":
        rad_azimuth = math.radians(cam_azimuth)
        rad_incidence = math.radians(cam_incidence)
        target_x, target_y, target_z = car_x, -0.42, -5.0
        eye_x = target_x + cam_distance * math.sin(rad_azimuth) * math.cos(rad_incidence)
        eye_y = target_y + cam_distance * math.sin(rad_incidence)
        eye_z = target_z + cam_distance * math.cos(rad_azimuth) * math.cos(rad_incidence)
        gluLookAt(eye_x, eye_y, eye_z, target_x, target_y, target_z, 0, 1, 0)
    else:
        gluLookAt(0, 4, 8,  0, 5, -20,  0, 1, 0)

    draw_skybox()

    if GAME_STATE == "MENU":
        draw_text((130, 380), "Corrida Solar", 92)
        base_y = 300
        for i, option in enumerate(OPTIONS):
            if i == SELECTED_MODE:
                color = (255, 255, 0, 255) 
                prefix = "> "
            else:
                color = (255, 255, 255, 255) 
                prefix = "  "
            draw_text((180, base_y - (i * 40)), prefix + option, 20, color)
        draw_text((220, 100), "SETAS para escolher | ENTER confirmar | ESC Sair", 18, (200, 200, 200, 255))
    elif GAME_STATE == "INSTRUCOES":
        draw_text((260, 500), "COMO JOGAR", 40, (255, 255, 0, 255))
        instrucoes = [
            "CONTROLES:",
            "- Seta Esquerda/Direita: Mover o carro",
            "- P: Pausar",
            "- MOUSE: No Pause, clique e arraste para mover a câmera",
            "- ESC: Fechar o Jogo",
            "",
            "OBJETIVOS:",
            "Fase 1 - Coletar Combustivel",
            "Fase 2 - Desviar dos Raios Solares",
            "Fase 3 - Coletar e desviar ao mesmo tempo. Boa sorte!",
            "",
            "Pressione ENTER para voltar"
        ]
        y_pos = 435
        for linha in instrucoes:
            draw_text((150, y_pos), linha, 22)
            y_pos -= 35
    elif GAME_STATE == "GAME_OVER":
        draw_text((140, 340), "Fim de Jogo", 92)
        draw_text((220, 260), f"Distancia Percorrida: {DISTANCE:.2f} Km", 25)        
        draw_text((200, 200), "Pressione ENTER para Tentar Novamente", 20)
        draw_text((240, 170), "Pressione 'M' para Voltar ao Menu", 20, (255, 255, 0, 255))        
        if GAME_MODE < 3:
            mode_name = OPTIONS[GAME_MODE].split(":")[0] 
            draw_text((340, 30), f"Modo: {mode_name}", 18, (200, 200, 200, 255))

    elif GAME_STATE == "JOGO" or GAME_STATE == "PAUSE":
        draw_sun()
        draw_track()
        draw_car()        
        for item in item_pool:
            if not item.active: continue

            glPushMatrix()
            item_z = item.z
            item_y = get_curve_y(item_z)
            
            height_offset = 0.0
            
            if item.type == "obstacle":
                height_offset = 4.0 
            elif item.type == "fuel":
                height_offset = 0.5
            
            glTranslatef(item.x, item_y + height_offset, item_z) 
            
            if item.type == "fuel":
                if GAME_STATE != "PAUSE": 
                    glRotatef(pygame.time.get_ticks() * 0.1, 0, 1, 0)                                
                glScalef(3.0, 3.0, 3.0)
                fuel_model.draw()                    
            else:
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)                
                glEnable(GL_ALPHA_TEST)
                glAlphaFunc(GL_GREATER, 0.1)
                glDisable(GL_LIGHTING)
                glColor3f(1.0, 0.7, 0.0)              
                glRotatef(90, 1, 0, 0) 
                glScalef(1.5, 1.5, 1.5)                 
                obstacle_model.draw()
                glEnable(GL_LIGHTING)
            
            glPopMatrix()
        if GAME_MODE != 0:
            draw_text((10, 560), f"Vidas: {LIVES}", 25)
        draw_text((500, 560), f"Distancia: {DISTANCE:.2f} km", 25)
        
        if GAME_MODE != 1:
            cor_texto = "Combustivel: {:.1f}%".format(FUEL)
            if FUEL < 20: 
                draw_text((10, 560 if GAME_MODE == 0 else 530), cor_texto, 25, (255, 100, 100, 255)) 
            else:
                draw_text((10, 560 if GAME_MODE == 0 else 530), cor_texto, 25)
        
        if GAME_STATE == "PAUSE":
            draw_text((300, 100), "PAUSADO", 50, (255, 255, 0, 255))
            draw_text((160, 50), "Mouse: Arraste para Girar (Esq) ou Zoom (Dir)", 25, (200, 200, 200, 255))
        
    pygame.display.flip()

def play_music_for_state(state):
    MENU_TRACK = "music/main_menu.mp3"
    PLAYLIST_FOLDER = "music/ost"
    
    pygame.mixer.music.stop()
    
    if state == "MENU":
        pygame.mixer.music.load(MENU_TRACK)
        pygame.mixer.music.play(-1)

    elif state == "JOGO" or state == "GAME_OVER":
        if os.path.exists(PLAYLIST_FOLDER):
            musicas = [m for m in os.listdir(PLAYLIST_FOLDER) if m.endswith(".mp3")]
            track_escolhida = random.choice(musicas)
            caminho_completo = os.path.join(PLAYLIST_FOLDER, track_escolhida)
            pygame.mixer.music.load(caminho_completo)
            pygame.mixer.music.play(-1)

def resize_window(width, height):
    global DISPLAY_WIDTH, DISPLAY_HEIGHT
    
    if height == 0:
        height = 1
        
    DISPLAY_WIDTH = width
    DISPLAY_HEIGHT = height
    glViewport(0, 0, width, height)    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 2000.0)    
    glMatrixMode(GL_MODELVIEW)

def main():
    global car_x, target_car_x, GAME_STATE, current_lane_index, FUEL, LIVES, DISTANCE, speed, sun_rotation, SELECTED_MODE, GAME_MODE, skybox_rotation
    global cam_azimuth, cam_incidence, cam_distance, mouse_is_down, mouse_btn_pressed

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.4)
    pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), DOUBLEBUF | OPENGL | pygame.RESIZABLE)
    pygame.display.set_caption("Corrida Solar")
    init_gl()
    play_music_for_state("MENU")

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.VIDEORESIZE:
                resize_window(event.w, event.h)
            
            if GAME_STATE == "PAUSE":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouse_is_down = True
                        mouse_btn_pressed = 1
                    elif event.button == 3: 
                        mouse_is_down = True
                        mouse_btn_pressed = 3
                    elif event.button == 4: 
                        cam_distance = max(5.0, cam_distance - 2.0)
                    elif event.button == 5: 
                        cam_distance = min(50.0, cam_distance + 2.0)
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_is_down = False
                    mouse_btn_pressed = -1
                elif event.type == pygame.MOUSEMOTION:
                    if mouse_is_down:
                        dx, dy = event.rel
                        if mouse_btn_pressed == 1: 
                            cam_azimuth += dx * 0.5
                            cam_incidence += dy * 0.5
                            if cam_incidence > 89: cam_incidence = 89
                            if cam_incidence < -89: cam_incidence = -89
                        elif mouse_btn_pressed == 3: 
                            cam_distance += dy * 0.1
                            if cam_distance < 5.0: cam_distance = 5.0
                            if cam_distance > 50.0: cam_distance = 50.0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if GAME_STATE == "JOGO":
                        GAME_STATE = "MENU"
                        play_music_for_state("MENU")
                    else:    
                        pygame.quit()
                        quit()

                if event.key == pygame.K_p:
                    if GAME_STATE == "JOGO":
                        GAME_STATE = "PAUSE"
                    elif GAME_STATE == "PAUSE":
                        GAME_STATE = "JOGO"
                        cam_azimuth = 0.0
                        cam_incidence = 20.0
                        cam_distance = 15.0

                if GAME_STATE == "MENU":
                    if event.key == pygame.K_RETURN:
                        if SELECTED_MODE == 3:
                            GAME_STATE = "INSTRUCOES"
                        else:
                            GAME_MODE = SELECTED_MODE 
                            FUEL = 100.0
                            LIVES = 3
                            DISTANCE = 0.0
                            speed = 0.5
                            sun_rotation = 0.0
                            skybox_rotation = 0.0 
                            reset_items() 
                            current_lane_index = 2
                            car_x = COLUMNS[current_lane_index]
                            target_car_x = car_x
                            GAME_STATE = "JOGO"
                            play_music_for_state("JOGO")
                    
                    elif event.key == pygame.K_UP:
                        SELECTED_MODE = (SELECTED_MODE - 1) % len(OPTIONS)
                    elif event.key == pygame.K_DOWN:
                        SELECTED_MODE = (SELECTED_MODE + 1) % len(OPTIONS)

                elif GAME_STATE == "INSTRUCOES":
                    if event.key == pygame.K_RETURN:
                        GAME_STATE = "MENU"
                
                elif GAME_STATE == "GAME_OVER":
                    if event.key == pygame.K_RETURN:
                        FUEL = 100.0
                        LIVES = 3
                        DISTANCE = 0.0
                        speed = 0.5
                        sun_rotation = 0.0 
                        skybox_rotation = 0.0
                        reset_items() 
                        current_lane_index = 2
                        car_x = COLUMNS[current_lane_index]
                        target_car_x = car_x
                        GAME_STATE = "JOGO"
                        play_music_for_state("JOGO")                    
                    elif event.key == pygame.K_m:
                        GAME_STATE = "MENU"
                        SELECTED_MODE = 0
                        play_music_for_state("MENU")
                
                elif GAME_STATE == "JOGO":
                    if event.key == pygame.K_LEFT and current_lane_index > 0:
                        current_lane_index -= 1
                    
                    if event.key == pygame.K_RIGHT and current_lane_index < 4: 
                        current_lane_index += 1
                    
                    target_car_x = COLUMNS[current_lane_index]
                
        if GAME_STATE == "JOGO":
            game_logic()
            
        draw_scene()
        clock.tick(60)

if __name__ == "__main__":
    main()