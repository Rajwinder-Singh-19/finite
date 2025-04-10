import numpy as np


class Point:
    coordinate: np.ndarray

    def __init__(self, coordinate: tuple):
        """Constructor for 2D point object in a cartesion co-ordinate system

        Args:
            coordinate (tuple): (x, y) co-ordinate measured from global origin
        """
        self.coordinate = np.zeros(2)
        self.coordinate[0] = coordinate[0]
        self.coordinate[1] = coordinate[1]


class Line:
    start_point: Point
    end_point: Point

    def __init__(self, start_point: tuple, end_point: tuple):
        """Constructor for 2D Line (for finite element approximation) object in a cartesian co-ordinate system

        Args:
            start_point (tuple): Starting co-ordinate of the line element (node 1)
            end_point (tuple): Ending Co-ordinate of the line element (node 2)
        """
        self.start_point = Point(start_point)
        self.end_point = Point(end_point)
