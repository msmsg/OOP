class Animals:

    species = ''
    name = ''
    weight = 0
    profit = 0
    ad_profit = 0
    name_profit = ''
    ad_name_profit = 0
    measure_profit = ''
    ad_meas_profit = ''
    voice = ''

    def feed(self, weight):
        weight = round( weight * 1.02, 2)
        return f'new weight = {weight} kg.'

    def take_profit(self, profit):
        profit = profit
        return f'Get {profit} {self.measure_profit}.'

    def take_ad_profit(self, ad_profit):
        ad_profit = ad_profit
        return f'Get {ad_profit} {self.ad_meas_profit}.'

    def animals_say(self, voice):
        return  voice

