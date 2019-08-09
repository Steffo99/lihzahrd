class GeneratorInfo:
    """Information about the world generator."""

    def __init__(self, seed, version):
        self.seed = seed
        """The seed this world was generated with."""

        self.version = version
        """The version of the generator that created this world."""
