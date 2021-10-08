class Star:
    def __init__(self, name, spectral_class):
        self.name = name
        self.spectral_class = spectral_class


class YellowDwarf(Star):
    def __init__(self, name, spectral_class):
        super().__init__(name, spectral_class)
