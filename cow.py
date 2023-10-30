from animals import Animals


class Cow(Animals):
    def __init__(self, name, weight, species = 'cow', profit=15, name_profit='milk', measure_profit='l', voice='Moo'):
        super().__init__(name, weight)
        self.species = species
        self.profit = profit
        self.name_profit = name_profit
        self.measure_profit = measure_profit
        self.voice = voice







