import typing


class FourPartSplit:
    """A world property split in four parts, separated by three vertical lines at a certain x coordinate."""

    def __init__(self, separators: typing.List[int], properties: typing.List):
        self.separators: typing.List[int] = separators
        """The three x coordinates of the vertical separators, in increasing order."""

        self.properties: typing.List = properties
        """The four properties, in order:

        - The far left property, the one between the left world edge and the first separator.
        - The nearby left property, between the first and the second separator.
        - The nearby right property, between the second and the third separator.
        - The far right property, between the third separator and the right world edge."""

    def __repr__(self):
        return f"FourPartSplit({repr(self.separators)}, {repr(self.properties)})"

    def get_property_at_x(self, x: int):
        if x < self.separators[0]:
            return self.properties[0]
        elif x < self.separators[1]:
            return self.properties[1]
        elif x < self.separators[2]:
            return self.properties[2]
        else:
            return self.properties[3]

    @property
    def far_left(self):
        return self.properties[0]

    @far_left.setter
    def far_left(self, value):
        self.properties[0] = value

    @property
    def nearby_left(self):
        return self.properties[1]

    @nearby_left.setter
    def nearby_left(self, value):
        self.properties[1] = value

    @property
    def nearby_right(self):
        return self.properties[2]

    @nearby_right.setter
    def nearby_right(self, value):
        self.properties[2] = value

    @property
    def far_right(self):
        return self.properties[2]

    @far_right.setter
    def far_right(self, value):
        self.properties[2] = value
