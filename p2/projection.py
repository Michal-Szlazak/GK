import math
import numpy as np

def perspective_projection_matrix(fov, aspect_ratio, near, far):
    f = 1 / math.tan(fov / 2)

    return np.array([
        [f / aspect_ratio, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, far / (far - near), (far * near) / (near - far)],
        [0, 0, 1, 0]
    ])

def perspective_divide(perspective_projection_matrix, v):
    v = np.dot(perspective_projection_matrix, v)

    w = math.fabs(v[3])

    if v[3] == 0:
        return v

    v = np.array(v)
    return [v[0] / w, v[1] / w, v[2] / w, w]

def map_to_screen_space(v, WIDTH, HEIGHT):

    v[0] = int(v[0] * WIDTH / 2 + WIDTH / 2)
    v[1] = int(v[1] * HEIGHT / 2 + HEIGHT / 2)
    v[2] = int(v[2])
    v[3] = int(v[3])

    return v