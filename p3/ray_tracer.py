from ray import Ray
import numpy as np
from multiprocessing import Pool
from point import Point
from color import Color
from vector import Vector

DARK_GRAY = Color(0.4, 0.4, 0.4)
BLACK = Color(0.0, 0.0, 0.0)
WHITE_SMOKE = Color(0.96078431372, 0.96078431372, 0.96078431372)

class RayTracer:
    def render_pixel(self, i, j, x0, xstep, y0, ystep, camera, scene):
        x = x0 + i * xstep
        y = y0 + j * ystep

        ray = Ray(camera, Point(x, y) - camera)
        color = self.ray_trace(ray, scene)
        color = self.vec_to_color(color)
        
        return i, j, color

    def render(self, scene, window):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)
        camera = scene.camera

        # Create a pool of worker processes
        pool = Pool()

        # Map the rendering function to each pixel coordinate
        pixel_results = pool.starmap(self.render_pixel, [(i, j, x0, xstep, y0, ystep, camera, scene) for j in range(height) for i in range(width)])

        # Update the window with the rendered colors
        for i, j, color in pixel_results:
            window.set_at((i, j), color)

        # Close the pool of worker processes
        pool.close()
        pool.join()

    def vec_to_color(self, vec):
        r = int(255.0 * np.clip(vec.x, 0.0, 1.0))
        g = int(255.0 * np.clip(vec.y, 0.0, 1.0))
        b = int(255.0 * np.clip(vec.z, 0.0, 1.0))
        return (r, g, b)

    def ray_trace(self, ray, scene):
        color = WHITE_SMOKE

        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        # color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        color = self.color_at_phong(obj_hit, hit_pos, hit_normal, scene)
        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)
    
    def color_at_phong(self, obj_hit, hit_pos, normal, scene):

        color = Color(0, 0, 0)

        for light in scene.lights:
            I_a = 1
            I_P = 1
            k_a = obj_hit.material.ambient
            k_d = obj_hit.material.diffuse
            k_s = obj_hit.material.specular
            n = obj_hit.material.n
            f_att = light.attenuation_factor(self.get_distance(hit_pos, light))

            normalized_light = (light.position - hit_pos).normalize()

            ambient_color = I_a * k_a
            diffuse_color = f_att * I_P * k_d * max(normal.dot_product(normalized_light), 0)
            specular_color = f_att * I_P * k_s * max(normal.dot_product((normalized_light + scene.camera).normalize()), 0) ** n

            color += ambient_color * obj_hit.material.color_at() 
            color += diffuse_color * obj_hit.material.color_at()
            color += specular_color * obj_hit.material.color_at()

        return color
    
    def get_distance(self, hit_pos, light):
        x = hit_pos.x - light.position.x
        y = hit_pos.y - light.position.y
        z = hit_pos.z - light.position.z
        return np.sqrt(x**2 + y**2 + z**2)