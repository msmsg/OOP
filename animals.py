class Animals:
    def __init__(self,name, weight):
        pass
        self.species = ''
        self.name = name
        self.weight = weight
        self.profit = 0     
        self.name_profit = ''
        self.measure_profit = ''
        self.voice = ''

    def feed(self, weight):
        weight = round( weight * 1.02, 2)
        return f'new weights = {weight} kg.'

    def take_profit(self, profit):
        profit = profit
        return f'Get {profit} {self.measure_profit}'

    def animals_say(self, voice):
        return  voice

