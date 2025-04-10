from system.truss import Truss


def main():
    node_1 = (2, 0)
    node_2 = (3, 0)
    node_3 = (4, 0)

    node_list = [node_1, node_2, node_3]
    node_connectivity = [(0, 1), (1, 2) ]

    truss = Truss(node_list, node_connectivity)
    truss.assemble_global_stiffness(1, 1)

    print(truss.global_stiffness_matrix)


if __name__ == "__main__":
    main()
