class Node:
    coordinate: list
    x_displacement: float = 0.0
    y_displacement: float = 0.0

    def __init__(self, coordinate: list):
        """Constructor for 2D node object in a cartesion co-ordinate system

        Args:
            coordinate list: [x, y] co-ordinate measured from global origin
        """
        self.coordinate = coordinate
        
