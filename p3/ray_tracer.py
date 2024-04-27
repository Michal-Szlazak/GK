from ray import Ray
import numpy as np
from image import Image


class RayTracer:
    def render(self, window, sphere_list, image, scene):
        self.width, self.height = window.get_size()
        self.scene = scene

        for x in range(self.width):
            for y in range(self.height):
                ray = self.create_ray(x, y)
                color = self.ray_trace(ray, sphere_list)
                if color[0] != 0 or color[1] != 0 or color[2] != 0:

                    window.set_at((x, y), color)

    def ray_trace(self, ray, sphere_list):
        color = np.array([0, 0, 0], dtype=np.uint8)

        closest_sphere, closest_t = self.find_closest_intersection(ray, sphere_list)
        if closest_sphere is None:
            return color
        
        # print("Closest sphere: ", closest_sphere)
        # print("Closest t: ", closest_t)
        
        color = closest_sphere.material.color
    
        hit_position = ray.point_at_parameter(closest_t)
        hit_normal = closest_sphere.normal(hit_position)

        # if hit_normal.any() < -1 or hit_normal.any() > 1:
        #     print("Hit normal: ", hit_normal)

        result = self.color_at(hit_position, closest_sphere, sphere_list, hit_normal)
        denormalized_color = self.denormalize_color(result)
        result_int = np.array(denormalized_color, dtype=np.uint8)
        color += result_int
        color = np.clip(color, 0, 255).astype(np.uint8)
        return tuple(color)

    def find_closest_intersection(self, ray, sphere_list):
        closest_sphere = None
        closest_t = float('inf')  # Initialize closest_t to infinity
        
        for sphere in sphere_list:
            hit_position = sphere.hit_position(ray)
            
            if hit_position is not None:
                t = np.linalg.norm(hit_position - ray.origin)  # Distance along the ray
                if t < closest_t:
                    closest_t = t
                    closest_sphere = sphere
        
        return closest_sphere, closest_t
    
    def color_at(self, hit_position, sphere, sphere_list, hit_normal):
        material = sphere.material
        obj_color = material.color
        black_color = np.zeros(3)
        color = material.ambient * np.array(obj_color)
        specular_k = 100  # You can use a fixed value or get it from material properties

        for light in self.scene.lights:
            to_light = Ray(hit_position, light.position - hit_position)
            diffuse_intensity = max(0, hit_normal.dot(to_light.direction))

            # print(hit_position, hit_normal)
            # # # Diffuse shading
            if diffuse_intensity > 0:
                print("Diffuse intensity: ", diffuse_intensity)

            color += np.array(obj_color) * material.diffuse * diffuse_intensity

            # Specular shading
            # view_dir = -to_light.direction  # Direction towards the camera
            # reflect_dir = 2 * np.dot(hit_normal, to_light.direction) * hit_normal - to_light.direction
            # specular_intensity = max(0, view_dir.dot(reflect_dir)) ** specular_k
            # color += np.array(light.color) * material.specular * specular_intensity

        color = np.clip(color, 0, 1)
        # print("Color: ", color)
        return np.array(color)



    def create_ray(self, x, y):
        # Normalize pixel coordinates to [-1, 1] range
        aspect_ratio = self.width / self.height
        normalized_x = (2 * (x + 0.5) / self.width - 1) * aspect_ratio
        normalized_y = 1 - 2 * (y + 0.5) / self.height
        return Ray((0, 0, -1), (normalized_x, normalized_y, 1))
    
    def denormalize_color(self, color):
        return (color[0] * 255, color[1] * 255, color[2] * 255)

class Ray:
    def __init__(self, origin, direction):
        self.origin = np.array(origin)
        self.direction = np.array(direction) / np.linalg.norm(direction)

    def point_at_parameter(self, t):
        return self.origin + t * self.direction


