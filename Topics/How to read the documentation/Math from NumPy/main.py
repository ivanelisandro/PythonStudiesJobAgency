import math


def calculate_cosine(angle_in_degrees):
    angle = math.radians(angle_in_degrees)
    cos = math.cos(angle)
    print(round(cos, 2))
