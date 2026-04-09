from src.analyzer import MarketAnalyzer

def test_fetch_market_data():
    analyzer = MarketAnalyzer()
    data = analyzer.fetch_market_data()

    assert "price" in data
    assert "volume" in data
    assert "trend" in data
