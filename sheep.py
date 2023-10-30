from animals import Animals


class Sheep(Animals):
    def __init__(self, name, weight, species = 'sheep', profit=5, name_profit='wool', measure_profit='kg', voice='Baa'):
        super().__init__(name, weight)
        self.species = species
        self.profit = profit
        self.name_profit = name_profit
        self.measure_profit = measure_profit
        self.voice = voice

