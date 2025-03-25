# $1 = 0.92 EUR
# EURUSD: 1.09, USDEUR: 0.92
# goals
# only convert currency pairs that we support
# return error for currency pairs that are not supported

class CurrencyConverter:
    def __init__(self):
        self.currency_dict = {
            "EURUSD": 1.09,
            "USDEUR": 0.92,
            "GBPUSD": 1,
            "USDGBP": 1,
        }

    def conversion(self, initial_currency, final_currency, amount):
        if not isinstance(initial_currency, str) or not isinstance(final_currency, str) or (not isinstance(amount, int) and not isinstance(amount, float)):
            return TypeError("Values received are not of correct type")

        currency_pair = initial_currency + final_currency
        if currency_pair in self.currency_dict:
            return amount * self.currency_dict[currency_pair]
        else:
            # Raise ValueError instead of returning it
            raise ValueError("Currency pair does not exist")
