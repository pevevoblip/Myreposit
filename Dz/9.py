class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def uah_to_usd(self, amount_uah):
        return amount_uah / self.exchange_rate

if __name__ == "__main__":
    exchange_rate = 41.80
    converter = CurrencyConverter(exchange_rate)

    amount_uah = float(input("Введіть суму в гривнях: "))
    amount_usd = converter.uah_to_usd(amount_uah)

    print(f"{amount_uah:.2f} грн = {amount_usd:.2f} доларів США")
