from animals import Animals


class Duck(Animals):
    def __init__(self, name, weight, species = 'duck', profit=2, name_profit='eggs', measure_profit='pieces', voice='quack'):
        super().__init__(name, weight)
        self.species = species
        self.profit = profit
        self.name_profit = name_profit
        self.measure_profit = measure_profit
        self.voice = voice
    
