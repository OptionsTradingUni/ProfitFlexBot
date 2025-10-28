"""
Test Trade Generator - Generate and view trades locally without Telegram
This allows you to test the full system: generate trades, save to database, view on website
"""

import os
import logging
import asyncio
from datetime import datetime, timezone
from dotenv import load_dotenv
from sqlalchemy import insert, select, func

# Load environment
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import modules
from models import engine, trade_logs, metadata
from traders import get_unique_trader, trader_manager
from verification_texts import generate_unique_txid
from price_simulator import price_sim
from image_generator_enhanced import create_ultra_realistic_mobile_trade_screenshot, save_trade_image
import random

STRATEGIES = [
    "Momentum Trading", "Swing Trading", "Day Trading", "Scalping",
    "Technical Analysis", "Breakout Strategy", "Gap Trading",
    "Moving Average Crossover", "RSI Strategy", "MACD Strategy"
]

REASONS = [
    "Strong technical breakout above resistance level with high volume confirmation",
    "Bullish divergence on RSI indicator combined with oversold conditions",
    "Positive earnings report exceeded analyst expectations significantly",
    "Major institutional accumulation detected on high timeframe charts",
    "Bullish flag pattern formation with tight consolidation near resistance",
    "Strong support hold at key fibonacci retracement level",
    "Unusual options activity indicating bullish sentiment from smart money",
    "Breaking above 200-day moving average with momentum",
    "Golden cross formation on daily chart signaling trend reversal",
    "High relative strength vs market index showing sector leadership"
]

def generate_trade_data(asset_type=None):
    """Generate realistic trade data"""
    if asset_type is None:
        asset_type = random.choices(
            ["stock", "crypto", "meme", "option", "futures", "forex"],
            weights=[30, 25, 15, 10, 10, 10],
            k=1
        )[0]
    
    trade_data = price_sim.generate_realistic_trade(asset_type=asset_type)
    
    trader_name = get_unique_trader()
    strategy = random.choice(STRATEGIES)
    reason = random.choice(REASONS)
    txid = generate_unique_txid(engine)
    
    commission = trade_data['deposit'] * random.uniform(0.0001, 0.002)
    slippage = random.uniform(0.001, 0.05)
    
    return {
        "symbol": trade_data['symbol'],
        "broker_name": trade_data['broker'],
        "trader_name": trader_name,
        "direction": trade_data['direction'],
        "entry_price": trade_data['entry_price'],
        "exit_price": trade_data['exit_price'],
        "quantity": trade_data['quantity'],
        "deposit": trade_data['deposit'],
        "profit": trade_data['profit'],
        "roi": trade_data['roi'],
        "commission": commission,
        "slippage": slippage,
        "strategy": strategy,
        "reason": reason,
        "txid": txid,
        "status": "FILLED",
        "timestamp": datetime.now(timezone.utc),
        "portfolio_value": random.uniform(50000, 500000),
        "asset_type": asset_type
    }

def save_trade_to_database(trade):
    """Save trade to database"""
    try:
        with engine.connect() as conn:
            stmt = insert(trade_logs).values(
                txid=trade["txid"],
                timestamp=trade["timestamp"],
                symbol=trade["symbol"],
                trader_name=trade["trader_name"],
                broker_name=trade["broker_name"],
                direction=trade["direction"],
                status=trade["status"],
                quantity=trade["quantity"],
                deposit=trade["deposit"],
                profit=trade["profit"],
                roi=trade["roi"],
                strategy=trade["strategy"],
                reason=trade["reason"],
                entry_price=trade["entry_price"],
                exit_price=trade["exit_price"],
                commission=trade["commission"],
                slippage=trade["slippage"],
                posted_at=trade["timestamp"]
            )
            conn.execute(stmt)
            conn.commit()
        logger.info(f"✅ Trade saved to database with TXID: {trade['txid']}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to save trade to database: {e}")
        return False

def create_trade_image(trade):
    """Generate trade image"""
    try:
        img = create_ultra_realistic_mobile_trade_screenshot(
            symbol=trade["symbol"],
            broker_name=trade["broker_name"],
            trader_name=trade["trader_name"],
            direction=trade["direction"],
            entry_price=trade["entry_price"],
            exit_price=trade["exit_price"],
            quantity=trade["quantity"],
            profit=trade["profit"],
            roi=trade["roi"],
            deposit=trade["deposit"],
            txid=trade["txid"],
            timestamp=trade["timestamp"],
            portfolio_value=trade.get("portfolio_value"),
            device_type=random.choice(["ios", "android"]),
            asset_type=trade.get("asset_type", "stock")
        )
        
        image_path = save_trade_image(img, trade["txid"])
        logger.info(f"✅ Trade image saved: {image_path}")
        return image_path
    except Exception as e:
        logger.error(f"❌ Failed to create trade image: {e}")
        return None

def get_database_stats():
    """Get statistics from database"""
    try:
        with engine.connect() as conn:
            total = conn.execute(select(func.count()).select_from(trade_logs)).scalar() or 0
            total_profit = conn.execute(select(func.sum(trade_logs.c.profit))).scalar() or 0
            avg_roi = conn.execute(select(func.avg(trade_logs.c.roi))).scalar() or 0
            winning = conn.execute(
                select(func.count()).select_from(trade_logs).where(trade_logs.c.profit > 0)
            ).scalar() or 0
            
            win_rate = (winning / total * 100) if total > 0 else 0
            
            return {
                "total_trades": total,
                "total_profit": total_profit,
                "avg_roi": avg_roi,
                "win_rate": win_rate
            }
    except Exception as e:
        logger.error(f"Failed to get stats: {e}")
        return None

def test_single_trade(asset_type=None):
    """Generate and save a single test trade"""
    logger.info("=" * 60)
    logger.info("🧪 GENERATING TEST TRADE")
    logger.info("=" * 60)
    
    # Initialize database
    try:
        metadata.create_all(engine, checkfirst=True)
        logger.info("✅ Database tables ready")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        return False
    
    # Generate trade
    logger.info("📊 Generating trade data...")
    trade = generate_trade_data(asset_type=asset_type)
    
    logger.info(f"Symbol: {trade['symbol']}")
    logger.info(f"Broker: {trade['broker_name']}")
    logger.info(f"Trader: {trade['trader_name']}")
    logger.info(f"Profit: ${trade['profit']:+,.2f} ({trade['roi']:+.2f}%)")
    logger.info(f"TXID: {trade['txid']}")
    
    # Create image
    logger.info("🎨 Creating trade screenshot...")
    image_path = create_trade_image(trade)
    
    # Save to database
    logger.info("💾 Saving to database...")
    success = save_trade_to_database(trade)
    
    if success:
        logger.info("=" * 60)
        logger.info("✅ TEST TRADE COMPLETED SUCCESSFULLY!")
        logger.info("=" * 60)
        logger.info(f"📷 Image: {image_path}")
        logger.info(f"🔗 View verification: /log/{trade['txid']}")
        logger.info(f"📊 Remaining unique traders: {trader_manager.get_remaining_count()}")
        
        # Show stats
        stats = get_database_stats()
        if stats:
            logger.info("")
            logger.info("📈 DATABASE STATISTICS:")
            logger.info(f"   Total Trades: {stats['total_trades']}")
            logger.info(f"   Total Profit: ${stats['total_profit']:,.2f}")
            logger.info(f"   Average ROI: {stats['avg_roi']:.2f}%")
            logger.info(f"   Win Rate: {stats['win_rate']:.1f}%")
        
        return True
    else:
        logger.error("❌ Test failed")
        return False

def test_multiple_trades(count=5, asset_type=None):
    """Generate multiple test trades"""
    logger.info(f"🧪 Generating {count} test trades...")
    
    successes = 0
    for i in range(count):
        logger.info(f"\n--- Trade {i+1}/{count} ---")
        if test_single_trade(asset_type=asset_type):
            successes += 1
    
    logger.info(f"\n✅ Completed {successes}/{count} trades successfully")
    
    stats = get_database_stats()
    if stats:
        logger.info("")
        logger.info("📈 FINAL DATABASE STATISTICS:")
        logger.info(f"   Total Trades: {stats['total_trades']}")
        logger.info(f"   Total Profit: ${stats['total_profit']:,.2f}")
        logger.info(f"   Average ROI: {stats['avg_roi']:.2f}%")
        logger.info(f"   Win Rate: {stats['win_rate']:.1f}%")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "multiple":
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            asset_type = sys.argv[3] if len(sys.argv) > 3 else None
            test_multiple_trades(count, asset_type)
        else:
            asset_type = sys.argv[1] if sys.argv[1] in ["stock", "crypto", "meme", "option", "futures", "forex"] else None
            test_single_trade(asset_type)
    else:
        test_single_trade()
