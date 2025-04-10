from system.truss import Truss2D


def main():
    node_0 = [0,0]
    node_1 = [3, 3]
    node_2 = [4, 4]
    node_3 = [1, 1]

    # List of all nodes
    node_list = [node_0, node_1, node_2, node_3]

    # Node connection list [[node_1, node_2, young's modulus, cross-sectional area], [ ... ] ...]
    node_connectivity = [[0, 1, 1, 1], [1, 2, 1, 1], [0, 2, 1, 1], [0, 3, 1, 1], [1, 3, 1, 1], [2, 3, 1, 1]]

    truss = Truss2D(node_list, node_connectivity)
    
    truss.truss_info()


if __name__ == "__main__":
    main()
