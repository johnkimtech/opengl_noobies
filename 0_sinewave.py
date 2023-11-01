import moderngl
import numpy as np
import moderngl_window as mglw
from pathlib import Path


class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (500, 500)
    resource_dir = (Path(__file__).parent / "resources").resolve()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog = self.ctx.program(
            vertex_shader=self.load_text("0.vert"),
            fragment_shader=self.load_text("0.frag"),
        )

    def render(self, time, frametime):
        N = 100
        x = np.linspace(-1.0, 1.0, N)
        t = np.array([time]).repeat(N)
        r = np.ones(N)
        g = np.ones(N) 
        b = np.ones(N)

        vertices = np.dstack([x, t, r, g, b])

        self.vbo = self.ctx.buffer(vertices.astype("f4").tobytes())
        self.vao = self.ctx.simple_vertex_array(
            self.prog, self.vbo, "in_xt", "in_color"
        )
        self.vao.render(moderngl.LINE_STRIP)


mglw.run_window_config(Test)
