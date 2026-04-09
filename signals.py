class SignalGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        trend = self.data["trend"]

        if trend == "bullish":
            return "BUY SIGNAL 📈"
        elif trend == "bearish":
            return "SELL SIGNAL 📉"
        else:
            return "HOLD ⚖️"
