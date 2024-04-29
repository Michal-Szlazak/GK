from ray import Ray
import numpy as np
from point import Point
from color import Color
from vector import Vector

DARK_GRAY = Color(0.2, 0.2, 0.2)

class RayTracer:
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

        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep

                ray = Ray(camera, Point(x, y) - camera)
                color = self.ray_trace(ray, scene)
                color = self.vec_to_color(color)
                # print(color)
                window.set_at((i, j), color)

    def vec_to_color(self, vec):
        r = int(255.0 * np.clip(vec.x, 0.0, 1.0))
        g = int(255.0 * np.clip(vec.y, 0.0, 1.0))
        b = int(255.0 * np.clip(vec.z, 0.0, 1.0))
        return (r, g, b)

    def ray_trace(self, ray, scene):
        color = DARK_GRAY
        # Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        # color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        # color = self.color_at_phong(obj_hit, hit_pos, hit_normal, scene)
        color = self.render_phong(obj_hit, hit_pos, hit_normal, scene)
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
    
    def color_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.material
        obj_color = material.color_at()
        to_cam = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_ints(0, 0, 0)
        # Light calculations
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # Diffuse shading (Lambert)
            color += (
                obj_color
                * material.diffuse
                * max(normal.dot_product(to_light.direction), 0)
            )
            # Specular shading (Blinn-Phong)
            half_vector = (to_light.direction + to_cam).normalize()
            color += (
                light.color
                * material.specular
                * max(normal.dot_product(half_vector), 0) ** specular_k
            )
        return color
    
    def color_at_phong(self, obj_hit, hit_pos, normal, scene):

        color = Color(0, 0, 0)

        half_vector = (scene.camera - hit_pos).normalize()
        cos_alpha = max(0, normal.dot_product(half_vector))
        specular_intensity = obj_hit.material.specular * cos_alpha ** obj_hit.material.n
        
        for light in scene.lights:
            I_a = 0.1
            I_P = light.intensity
            k_a = obj_hit.material.ambient
            k_s = obj_hit.material.specular
            k_d = obj_hit.material.diffuse
            f_att = light.attenuation_factor(self.get_distance(hit_pos, light))
            n = obj_hit.material.n

            ambient_color = I_a * k_a * obj_hit.material.color_at()
            diffuse_color = I_P * f_att * k_d * max(0, normal.dot_product(light.position - hit_pos)) * obj_hit.material.color_at()
            specular_color = I_P * f_att * k_s * max(0, normal.dot_product((light.position - hit_pos).normalize() + (hit_pos - scene.camera).normalize())) ** n

            print(ambient_color, diffuse_color, specular_color)
            color += ambient_color + diffuse_color + specular_color
            
        return color
    
    def get_distance(self, hit_pos, light):
        x = hit_pos.x - light.position.x
        y = hit_pos.y - light.position.y
        z = hit_pos.z - light.position.z
        return np.sqrt(x**2 + y**2 + z**2)
    

    def render_phong(self, obj_hit, hit_pos, normal, scene):
    # Constants

        for light in scene.lights:
            I_a = 0.1  # Ambient intensity
            I_P = 1.0  # Incident light intensity
            k_a = obj_hit.material.ambient  # Ambient reflection coefficient
            k_d = obj_hit.material.diffuse  # Diffuse reflection coefficient
            k_s = obj_hit.material.specular  # Specular reflection coefficient
            n = obj_hit.material.n  # Shininess exponent

            # Calculate the half vector (between view direction and light direction)
            half_vector = (scene.camera - hit_pos).normalize()
            # Ambient color
            ambient_color = I_a * k_a * obj_hit.material.color_at()

            # Diffuse color
            light_direction = (light.position - hit_pos).normalize()
            cos_theta = max(0, normal.dot_product(light_direction))
            diffuse_color = I_P * cos_theta * k_d * obj_hit.material.color_at()

            # Specular color
            cos_alpha = max(0, normal.dot_product(half_vector))
            specular_color = I_P * k_s * (cos_alpha ** n)

            # Combine all components
            print(ambient_color, diffuse_color, specular_color)
            final_color = ambient_color + diffuse_color + specular_color
            return final_color