import numpy as np


class BaseMesh:
    def __init__(self):
        self.ctx = None   # OpenGL context
        self.program = None  # shader program
        self.vbo_format = None  # vertex buffer data type format: "3f 3f"
        # attribute names according to the format: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        self.vao = None  # vertex array object

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()