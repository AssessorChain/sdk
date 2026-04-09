from analyzer import MarketAnalyzer
from signals import SignalGenerator

def main():
    analyzer = MarketAnalyzer()
    data = analyzer.fetch_market_data()

    signal = SignalGenerator(data)
    result = signal.generate()

    print("=== Assessor 200 Analysis ===")
    print(result)

if __name__ == "__main__":
    main()
