"""
    Pygame's simple obj loader loading without texture loading
"""

class OBJSimple:
    def __init__(self, filename, swapyz=False):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = [values[1],values[2],values[3]]
                if swapyz:
                    values[1], values[2] = values[2], values[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = [values[1],values[2],values[3]]
                if swapyz:
                    values[1], values[2] = values[2], values[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append([values[1],values[2]])
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
                self.faces.append((face, norms, texcoords))
