class TreetopVariants:
    """(Unknown) Information about the treetop variants in the world."""

    def __init__(self, treetop_variants: list[int]):
        self.treetop_variants: list[int] = treetop_variants

    def __repr__(self):
        return f"WorldTreetopVariants({self.treetop_variants})"
