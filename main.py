from system.truss import Truss2D



def main():
    node_0 = [0, 0]
    node_1 = [1, 1]
    node_2 = [2, 0]
    node_3 = [3, 0]

    node_list = [node_0, node_1, node_2, node_3]

    node_connectivity = [
        [0, 1, 100, .1],  
        [1, 2, 100, .1],  
        [0, 2, 100, .1],  
        [1, 3, 100, .1],
        [2, 3, 100, .1]
    ]

    truss = Truss2D(node_list, node_connectivity)

    truss.constrain(nodes=[0, 1, 3], constrained_direction=[0, 2, 2])  

    truss.apply_load([2], [[100, 100]])  
    truss.solve()


if __name__ == "__main__":
    main()
