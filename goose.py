from animals import Animals


class Goose(Animals):
    def __init__(self, name, weight, species = 'goose', profit=2, name_profit='eggs', measure_profit='pieces', voice='To honk'):
        super().__init__(name, weight)
        self.species = species
        self.profit = profit
        self.name_profit = name_profit
        self.measure_profit = measure_profit
        self.voice = voice

