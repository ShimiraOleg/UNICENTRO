import pygame
from OpenGL.GL import *
import os

class OBJLoader:
    def __init__(self, filename, swapyz=False):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.gl_list = 0        
        self.mtl_data = {} 
        dirname = os.path.dirname(filename)
        material = None
        
        try:
            with open(filename, "r") as f:
                for line in f:
                    if line.startswith('#'): continue
                    values = line.split()
                    if not values: continue
                    
                    if values[0] == 'v':
                        v = list(map(float, values[1:4]))
                        if swapyz:
                            v = v[0], v[2], v[1]
                        self.vertices.append(v)
                    elif values[0] == 'vn':
                        v = list(map(float, values[1:4]))
                        if swapyz:
                            v = v[0], v[2], v[1]
                        self.normals.append(v)
                    elif values[0] == 'vt':
                        self.texcoords.append(list(map(float, values[1:3])))
                    elif values[0] == 'mtllib':
                        path_mtl = os.path.join(dirname, values[1])
                        self.load_mtl(path_mtl)
                    elif values[0] == 'usemtl':
                        material = values[1]
                    elif values[0] == 'f':
                        face = []
                        texcoords = []
                        norms = []
                        for v in values[1:]:
                            w = v.split('/')
                            face.append(int(w[0]))
                            if len(w) >= 2 and len(w[1]) > 0:
                                texcoords.append(int(w[1]))
                            else:
                                texcoords.append(0)
                            if len(w) >= 3 and len(w[2]) > 0:
                                norms.append(int(w[2]))
                            else:
                                norms.append(0)
                        self.faces.append((face, norms, texcoords, material))
        except IOError:
            print(f"Error opening {filename}")
            return

        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        
        current_material = None
        
        for face in self.faces:
            vertices, normals, texture_coords, material = face
            if material != current_material:
                current_material = material
                if material in self.mtl_data:
                    mat = self.mtl_data[material]                    
                    if 'texture_id' in mat:
                        glEnable(GL_TEXTURE_2D)
                        glBindTexture(GL_TEXTURE_2D, mat['texture_id'])
                    elif 'diffuse' in mat:
                        glDisable(GL_TEXTURE_2D) 
                        r, g, b = mat['diffuse']
                        glColor3f(r, g, b)
            
            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        
        glDisable(GL_TEXTURE_2D)
        glEndList()

    def load_mtl(self, filename):
        current_mtl = None
        try:
            with open(filename, "r") as f:
                for line in f:
                    if line.startswith('#'): continue
                    values = line.split()
                    if not values: continue
                    if values[0] == 'newmtl':
                        current_mtl = values[1]
                        self.mtl_data[current_mtl] = {}
                    elif current_mtl is None:
                        continue                        
                    if values[0] == 'Kd':
                        self.mtl_data[current_mtl]['diffuse'] = (float(values[1]), float(values[2]), float(values[3]))                        
                    elif values[0] == 'map_Kd':
                        mtl_dir = os.path.dirname(filename)
                        texture_path = os.path.join(mtl_dir, values[1])
                        try:
                            texture_surface = pygame.image.load(texture_path)
                            texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
                            width = texture_surface.get_width()
                            height = texture_surface.get_height()
                            tex_id = glGenTextures(1)
                            glBindTexture(GL_TEXTURE_2D, tex_id)
                            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
                            
                            self.mtl_data[current_mtl]['texture_id'] = tex_id
                        except:
                            print(f"Error opening texture: {texture_path}")

        except IOError:
            print(f"Error: {filename}")

    def draw(self):
        glCallList(self.gl_list)