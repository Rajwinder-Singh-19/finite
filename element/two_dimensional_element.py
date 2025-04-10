import numpy as np
from geometry.two_dimensional import Line


class TrussElement2D:
    # Geometric properties
    element: Line
    length_SI: float

    # Direction Cosines
    c: float  # cos (theta)
    s: float  # sin (theta)

    # Physical properties
    young_modulus_SI: float
    cross_section_area_SI: float

    # Characteristic matrix
    local_stiffness_matrix: np.ndarray

    def __init__(
        self,
        node_1: tuple,
        node_2: tuple,
        young_modulus_SI: float,
        cross_section_area_SI: float,
    ):
        self.element = Line(node_1, node_2)
        self.young_modulus_SI = young_modulus_SI
        self.cross_section_area_SI = cross_section_area_SI
        x0, y0 = (
            self.element.start_point.coordinate[0],
            self.element.start_point.coordinate[1],
        )
        x1, y1 = (
            self.element.end_point.coordinate[0],
            self.element.end_point.coordinate[1],
        )
        self.length_SI = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        c = self.c = (x1 - x0) / self.length_SI
        s = self.s = (y1 - y0) / self.length_SI

        self.local_stiffness_matrix = (
            np.array(
                (
                    [c * c, c * s, -c * c, -c * s],
                    [c * s, s * s, -c * s, -s * s],
                    [-c * c, -c * s, c * c, c * s],
                    [-c * s, -s * s, c * s, s * s],
                )
            )
            * (self.young_modulus_SI * self.cross_section_area_SI)
            / self.length_SI
        )

    def element_info(self):
        print("Node 1 (m): ", self.element.start_point.coordinate)
        print("Node 2 (m): ", self.element.end_point.coordinate)
        print("Element length (m): ", self.length_SI)
        print("Direction cosines c and s: ", self.c, self.s)
        print("Young's Modulus (N/m^2): ", self.young_modulus_SI)
        print("Cross-sectional Area (m^2): ", self.cross_section_area_SI)
        print("Local stiffness matrix: ", self.local_stiffness_matrix)
