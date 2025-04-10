from element.two_dimensional_element import TrussElement2D
import numpy as np


class Truss:
    node_list: list
    node_connectivity: list
    global_stiffness_matrix: np.ndarray

    def __init__(self, node_list: list, node_connectivity: list):
        self.node_list = node_list
        self.node_connectivity = node_connectivity

    def assemble_global_stiffness(
        self, young_modulus_SI: float, cross_section_area_SI: float
    ):
        n_nodes = len(self.node_list)
        K = np.zeros((2 * n_nodes, 2 * n_nodes))

        for node_i, node_j in self.node_connectivity:
            element = TrussElement2D(
                self.node_list[node_i],
                self.node_list[node_j],
                young_modulus_SI,
                cross_section_area_SI,
            )

            k = element.local_stiffness_matrix

            dofs = np.array([2 * node_i, 2 * node_i + 1, 2 * node_j, 2 * node_j + 1])

            rows = dofs.reshape(-1, 1)
            cols = dofs.reshape(1, -1)

            K[rows, cols] += k

        self.global_stiffness_matrix = K
