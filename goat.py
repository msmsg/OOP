from animals import Animals


class Goat(Animals):
    def __init__(self, name, weight, species = 'goat', profit=5, name_profit='sheep', measure_profit='kg', ad_profit=3,ad_name_profit='milk', ad_meas_profit='l', voice='Bleat'):
        super().__init__(name, weight)
        self.species = species
        self.profit = profit
        self.name_profit = name_profit
        self.measure_profit = measure_profit
        self.ad_profit = ad_profit
        self.ad_name_profit = ad_name_profit
        self.ad_meas_profit = ad_meas_profit
        self.voice = voice
    

    
    def take_ad_profit(self, ad_profit):
        ad_profit = ad_profit
        return f'Get {ad_profit} {self.ad_meas_profit} {self.ad_name_profit}.'

