from animals import Animals


class Chicken(Animals):
    def __init__(self, name, weight, species = 'chicken', profit=3, name_profit='eggs', measure_profit='pieces', voice='cluck'):
        super().__init__(name, weight)
        self.species = species
        self.profit = profit
        self.name_profit = name_profit
        self.measure_profit = measure_profit
        self.voice = voice
    
