from system.truss import Truss2D


def main():
    node_1 = [2, 0]
    node_2 = [3, 0]
    node_3 = [4, 0]

    # List of all nodes
    node_list = [node_1, node_2, node_3]

    # Node connection list [(node_1, node_2, young's modulus, cros-sectional area),(...)...]
    node_connectivity = [[0, 1, 1, 1], [1, 2, 1, 1]]

    truss = Truss2D(node_list, node_connectivity)

    print(truss.global_stiffness_matrix)


if __name__ == "__main__":
    main()
