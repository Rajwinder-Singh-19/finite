import numpy as np
class Point:
    coordinate: np.ndarray
    def __init__(self, coordinate: tuple):
        self.coordinate = np.zeros(2)
        self.coordinate[0] = coordinate[0]
        self.coordinate[1] = coordinate[1]

class Line:
    start_point: Point
    end_point: Point
    
    def __init__(self, start_point: tuple, end_point: tuple):
        self.start_point = Point(start_point)
        self.end_point = Point(end_point)