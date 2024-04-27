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
                    # Adjust window offset based on window size
                    # if color[0] > 50 or color[1] > 50 or color[2] > 50:
                    #     print("Color printed for x, y: ", color, x, y)
                    window.set_at((x, y), color)

    def ray_trace(self, ray, sphere_list):
        color = np.array([0, 0, 0], dtype=np.uint8)

        closest_sphere, closest_t = self.find_closest_intersection(ray, sphere_list)
        if closest_sphere is None:
            return color
        
        color = closest_sphere.material.color
    
        hit_position = ray.point_at_parameter(closest_t)
        hit_normal = closest_sphere.normal(hit_position)

        result = self.color_at(hit_position, closest_sphere, sphere_list, hit_normal)
        denormalized_color = self.denormalize_color(result)
        result_int = np.array(denormalized_color, dtype=np.uint8)
        color += result_int
        # color = np.clip(color, 0, 255).astype(np.uint8)
        # print("Color: ", color)
        return tuple(color)

    def find_closest_intersection(self, ray, sphere_list):
        closest_sphere = None
        closest_t = None
        
        for sphere in sphere_list:
            hit_position = sphere.hit_position(ray)
            
            if hit_position is not None:
                distance = np.linalg.norm(hit_position - ray.origin)
                
                if closest_t is None or distance < closest_t:
                    closest_t = distance
                    closest_sphere = sphere
    
        return closest_sphere, closest_t
    
    def color_at(self, hit_position, sphere, sphere_listm, hit_normal):

        material = sphere.material
        obj_color = sphere.material.color
        to_camera = -hit_position - 1
        black_color = np.zeros(3)
        # color = material.ambient * black_color
        color = material.ambient * np.array(obj_color)

        specular_k = 50

        for light in self.scene.lights:
            
            to_light = Ray(hit_position, light.position - hit_position)

            # Diffuse shading
            color += np.array(obj_color) * material.diffuse * max(0, hit_normal.dot(to_light.direction))

            # Specular shading
            half_vector = (to_light.direction + to_camera) / np.linalg.norm(to_light.direction + to_camera) 
            # if max(0, hit_normal.dot(to_light.direction)) > 0:
            #     print("Max: ", max(0, hit_normal.dot(to_light.direction)))
            color += np.array(light.color) * material.specular * max(0, hit_normal.dot(half_vector)) ** specular_k

            # addition = np.array(light.color) * material.specular * max(0, hit_normal.dot(half_vector)) ** specular_k
            # if addition[0] > 0 or addition[1] > 0 or addition[2] > 0:
            #     print("Light addition: ", np.array(light.color) * material.specular * max(0, hit_normal.dot(half_vector)) ** specular_k)

        return np.array(color)



    def create_ray(self, x, y):
        # Normalize pixel coordinates to [-1, 1] range
        aspect_ratio = self.width / self.height
        normalized_x = (2 * (x + 0.5) / self.width - 1) * aspect_ratio
        normalized_y = 1 - 2 * (y + 0.5) / self.height
        return Ray((0, 0, 0), (normalized_x, normalized_y, 1))
    
    def denormalize_color(self, color):
        return (color[0] * 255, color[1] * 255, color[2] * 255)

class Ray:
    def __init__(self, origin, direction):
        self.origin = np.array(origin)
        self.direction = np.array(direction) / np.linalg.norm(direction)

    def point_at_parameter(self, t):
        return self.origin + t * self.direction


