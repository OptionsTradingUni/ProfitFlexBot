"""
Test script for enhanced image generator and price simulator
"""

from image_generator_enhanced import create_ultra_realistic_mobile_trade_screenshot, save_trade_image
from price_simulator import price_sim
from traders import get_random_trader
from verification_texts import generate_txid
from datetime import datetime
import random

def test_all_features():
    """Test all enhanced features"""
    
    print("🧪 Testing Enhanced Image Generator and Price Simulator...")
    print("-" * 60)
    
    test_cases = [
        ("stock", "AAPL"),
        ("crypto", "BTC"),
        ("meme", "NIKY"),
        ("stock", "TSLA"),
        ("crypto", "ETH")
    ]
    
    for asset_type, symbol in test_cases:
        print(f"\n📊 Testing {asset_type.upper()}: {symbol}")
        
        trade_data = price_sim.generate_realistic_trade(symbol=symbol, asset_type=asset_type)
        
        print(f"   Entry Price: ${trade_data['entry_price']:,.8f}")
        print(f"   Exit Price: ${trade_data['exit_price']:,.8f}")
        print(f"   Profit: ${trade_data['profit']:,.2f}")
        print(f"   ROI: {trade_data['roi']:.2f}%")
        print(f"   Broker: {trade_data['broker']}")
        
        img = create_ultra_realistic_mobile_trade_screenshot(
            symbol=trade_data['symbol'],
            broker_name=trade_data['broker'],
            trader_name=get_random_trader(),
            direction=trade_data['direction'],
            entry_price=trade_data['entry_price'],
            exit_price=trade_data['exit_price'],
            quantity=trade_data['quantity'],
            profit=trade_data['profit'],
            roi=trade_data['roi'],
            deposit=trade_data['deposit'],
            txid=generate_txid(),
            timestamp=datetime.now(),
            portfolio_value=random.uniform(50000, 500000),
            device_type=random.choice(["ios", "android"])
        )
        
        txid = generate_txid()
        filename = save_trade_image(img, txid)
        print(f"   ✅ Image saved: {filename}")
        print(f"   📱 Device: {'iOS' if random.random() > 0.5 else 'Android'}")
        print(f"   🎨 Features: Mobile UI, Social Proof, Tech Indicators, Risk Management")
    
    print("\n" + "=" * 60)
    print("✅ All tests completed successfully!")
    print("=" * 60)
    
    print("\n🎯 Enhanced Features Included:")
    print("   • Mobile phone status bar (battery, signal, time)")
    print("   • Social proof (watching count, trending badges)")
    print("   • Market sentiment and news ticker")
    print("   • Technical indicators (RSI, MACD, Bollinger Bands)")
    print("   • Support/Resistance levels & Fibonacci retracement")
    print("   • Risk management (Stop Loss, Take Profit, R:R)")
    print("   • Portfolio context and position size")
    print("   • Leaderboard elements and win streaks")
    print("   • Trade timing and duration")
    print("   • Screenshot-style rounded corners")
    print("   • Bottom navigation bar")
    print("\n🪙 NIKY Meme Coin:")
    print(f"   Current simulated price: ${price_sim.get_niky_price():.10f}")
    
if __name__ == "__main__":
    test_all_features()
