from element.two_dimensional_element import TrussElement2D
import numpy as np


class Truss2D:
    node_list: list
    node_connectivity_map: list
    element_list: list
    global_stiffness_matrix: np.ndarray
    global_force_vector: np.ndarray
    global_displacement_vector: np.ndarray

    def __init__(self, node_list: list, node_connectivity_map: list):
        """Constructor for a 2D truss system consisting of multiple nodes connected using a 2D truss element.

        Args:
            node_list (list): List of all the nodes in truss
            node_connectivity_map (list): List of all the connectivity mappings between any pair of nodes in the node list

        Raises:
            ValueError: Atleast 2 nodes are required
            ValueError: Nodes must contain both x and y co-ordinate
            ValueError: Node connectivity must contain 4 values of in this format -> [{node 1 of the connecting element}, {node 2 of the connecting element}, {young's modulus of the connecting element}, {cross-sectional area of the connecting element}]
            ValueError: Node connectivity contains an invalid node index
            ValueError: Young's modulus for an element is a strictly positive quantity
            ValueError: Cross-sectional area for element is a strictly positive quantity
            RuntimeError: Global Stiffness matrix is not symmetric
        """
        if len(node_list) < 2:
            raise ValueError("Atleast 2 nodes are required")
        for node in node_list:
            if len(node) != 2:
                raise ValueError(
                    f"Nodes must contain only x and y co-ordinate. The node list contains {node} which does not meet this requirement"
                )

        self.node_list = node_list

        for connectivity in node_connectivity_map:
            if len(connectivity) != 4:
                raise ValueError(
                    "Node connectivity must contain 4 values of in this format -> [{node 1 of the connecting element}, {node 2 of the connecting element}, {young's modulus of the connecting element}, {cross-sectional area of the connecting element}]"
                )

        self.element_list = []

        for idx, (node_i, node_j, young_modulus_SI, cross_section_area_SI) in enumerate(
            node_connectivity_map
        ):
            if node_i not in range(len(self.node_list)):
                raise ValueError(
                    f"Node connectivity contains invalid node index {node_i} at element {idx}. Max valid index is {len(self.node_list) - 1}"
                )
            if node_j not in range(len(node_list)):
                raise ValueError(
                    f"Node connectivity contains invalid index {node_j} at element {idx}. Max valid index is {len(self.node_list) - 1}"
                )
            if young_modulus_SI <= 0:
                raise ValueError(
                    f"Young's modulus for element {idx} is non-positive. It is a strictly positive quantity."
                )
            if cross_section_area_SI <= 0:
                raise ValueError(
                    f"Cross-sectional area for element {idx+1} is non-positive. It is a strictly positive quantity."
                )

            element = TrussElement2D(
                node_list[node_i],
                node_list[node_j],
                young_modulus_SI,
                cross_section_area_SI,
            )
            self.element_list.append(element)

        self.node_connectivity_map = node_connectivity_map

        self.assemble_global_stiffness()

        if not np.allclose(
            self.global_stiffness_matrix, self.global_stiffness_matrix.T
        ):
            raise RuntimeError("Global Stiffness matrix is not symmetric")

        self.global_force_vector = np.zeros(2 * len(self.node_list))

        self.global_displacement_vector = np.zeros(2 * len(self.node_list))

    def assemble_global_stiffness(self):
        n_nodes = len(self.node_list)
        K = np.zeros((2 * n_nodes, 2 * n_nodes))

        for idx, (node_i, node_j, young_modulus_SI, cross_section_area_SI) in enumerate(
            self.node_connectivity_map
        ):
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

    def constrain(self, nodes: list = [], global_dofs: list = []):
        for node in nodes:
            for dof in [2 * node, 2 * node + 1]:
                self._constrain_dof(dof)

        for dof in global_dofs:
            self._constrain_dof(dof)

    def _constrain_dof(self, dof: int):
        self.global_stiffness_matrix[dof, :] = 0
        self.global_stiffness_matrix[:, dof] = 0
        self.global_stiffness_matrix[dof, dof] = 1
        self.global_force_vector[dof] = 0

    def apply_load(self, applied_node_list: list, applied_force_list: list):
        if len(applied_node_list) != len(applied_force_list):
            raise ValueError(
                "All the specified nodes in the applied_node_list argument must have forces in the form [fx, fy] applied to them"
            )

        for node, (fx, fy) in zip(applied_node_list, applied_force_list):
            self.global_force_vector[2 * node] += fx
            self.global_force_vector[2 * node + 1] += fy

    def solve(self):
        self.global_displacement_vector = np.linalg.solve(
            self.global_stiffness_matrix, self.global_force_vector
        )

    def print_nodal_displacements(self):
        print(self.global_displacement_vector.reshape((-1, 2)))

    def truss_info(self):
        print(f"{self.__class__}\n".center(100))
        for idx, element in enumerate(self.element_list):
            print(f"ELEMENT {idx}\n".center(100))
            element.element_info()
            print("")
        print(f"Global Stiffness Matrix: \n")
        print(self.global_stiffness_matrix)
        print("")
        print(f"Global Force Vector: \n")
        print(self.global_force_vector.reshape((-1, 2)))
        print("")
        print(f"Global Displacement Vector: \n")
        self.print_nodal_displacements()
