class Point:
    coordinate: list

    def __init__(self, coordinate: list):
        """Constructor for 2D point object in a cartesion co-ordinate system

        Args:
            coordinate list: [x, y] co-ordinate measured from global origin
        """
        self.coordinate = coordinate
