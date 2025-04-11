import numpy as np
from geometry.two_dimensional import Node


class TrussElement2D:
    # Geometric properties
    node_0: Node
    node_1: Node
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
        node_0: list,
        node_1: list,
        young_modulus_SI: float,
        cross_section_area_SI: float,
    ):
        self.node_0 = Node(node_0)
        self.node_1 = Node(node_1)
        self.young_modulus_SI = young_modulus_SI
        self.cross_section_area_SI = cross_section_area_SI
        x0, y0 = (
            self.node_0.coordinate[0],
            self.node_0.coordinate[1],
        )
        x1, y1 = (
            self.node_1.coordinate[0],
            self.node_1.coordinate[1],
        )
        self.length_SI = float(np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2))

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
        print(f"{self.__class__}\n".center(100))
        print(f"Node 0 (m): {self.node_0.coordinate}\n")
        print(f"Node 1 (m): {self.node_1.coordinate}\n")
        print(f"Element length (m): {self.length_SI}\n")
        print(f"Direction cosines c and s: {[self.c, self.s]}\n")
        print(f"Young's Modulus (N/m^2): {self.young_modulus_SI}\n")
        print(f"Cross-sectional Area (m^2): {self.cross_section_area_SI}\n")
        print(f"Local stiffness matrix:\n {self.local_stiffness_matrix}\n")
