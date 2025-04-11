from system.truss import Truss2D


def main():
    node_0 = [0, 0]
    node_1 = [1, 1]
    node_2 = [2, 0]
    node_3 = [3, 0]

    node_list = [node_0, node_1, node_2, node_3]

    node_connectivity = [
        [0, 1, 1, 1],  
        [1, 2, 1, 1],  
        [0, 2, 1, 1],  
        [1, 3, 1, 1],
        [2, 3, 1, 1]
    ]

    truss = Truss2D(node_list, node_connectivity)

    truss.constrain(nodes=[0, 3])  

    truss.apply_load([2], [[10, 0]])  
    truss.solve()
    truss.truss_info()


if __name__ == "__main__":
    main()
