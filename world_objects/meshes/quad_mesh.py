from settings import *
from meshes.base_mesh import BaseMesh
import numpy as np

class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.quad

        self.vbo_format = '3f 3f'  # 3 floats for position, 3 for color
        self.attrs = ('in_position', 'in_color')  # ✅ match shader variable names exactly
        self.vao = self.get_vao()

    def get_vertex_data(self):
        # Define 2 triangles to form a quad
        vertices = [
            (0.5,  0.5, 0.0),  # Top Right
            (-0.5, 0.5, 0.0),  # Top Left
            (-0.5, -0.5, 0.0), # Bottom Left
            
            (0.5,  0.5, 0.0),  # Top Right
            (-0.5, -0.5, 0.0), # Bottom Left
            (0.5, -0.5, 0.0)   # Bottom Right
        ]

        colors = [
            (0, 1, 0),  # Green
            (1, 0, 0),  # Red
            (1, 1, 0),  # Yellow

            (0, 1, 0),  # Green
            (1, 1, 0),  # Yellow
            (0, 0, 1)   # Blue
        ]

        # Combine position and color
        combined = [pos + col for pos, col in zip(vertices, colors)]
        return np.array(combined, dtype='float32')
