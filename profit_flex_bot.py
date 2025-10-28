"""
Profit Flex Bot - Main Bot Logic
Generates and posts realistic trading insights with professional images
"""

import os
import random
import asyncio
import logging
from datetime import datetime, timezone
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError
from sqlalchemy import text, insert

# Load environment variables
load_dotenv()

# Import modules
from models import engine, trade_logs
from traders import get_random_trader
from verification_texts import generate_txid
from image_generator_enhanced import create_ultra_realistic_mobile_trade_screenshot, save_trade_image
from price_simulator import price_sim

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Bot configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
DOMAIN = os.getenv("REPLIT_DOMAINS", "").split(",")[0] if os.getenv("REPLIT_DOMAINS") else "localhost:5000"

# Asset pools for realistic trading
STOCK_SYMBOLS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "AMD", "NFLX", "PYPL",
    "V", "MA", "DIS", "BA", "INTC", "CSCO", "PEP", "KO", "NKE", "MCD",
    "WMT", "JPM", "BAC", "WFC", "GS", "MS", "C", "USB", "PNC", "AXP"
]

CRYPTO_SYMBOLS = [
    "BTC/USD", "ETH/USD", "SOL/USD", "BNB/USD", "ADA/USD", "DOGE/USD",
    "XRP/USD", "DOT/USD", "MATIC/USD", "LINK/USD", "UNI/USD", "AVAX/USD"
]

MEME_COINS = [
    "NIKY/USD", "NIKY/USD", "NIKY/USD",
    "PEPE/USD", "SHIB/USD", "DOGE/USD", "FLOKI/USD", "BONK/USD",
    "WIF/USD", "MEME/USD", "WOJAK/USD", "SPONGE/USD"
]

# Trading strategies
STRATEGIES = [
    "Momentum Trading", "Swing Trading", "Day Trading", "Scalping",
    "Technical Analysis", "Breakout Strategy", "Gap Trading",
    "Moving Average Crossover", "RSI Strategy", "MACD Strategy"
]

# Reasoning templates
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
    "High relative strength vs market index showing sector leadership",
    "Bullish engulfing candle pattern at critical support zone",
    "Volume spike indicating strong buying interest from institutions",
    "Price action showing higher lows and higher highs pattern",
    "Stochastic oscillator showing bullish crossover in oversold territory",
    "Bollinger band squeeze indicating imminent volatility expansion"
]

def generate_trade_data():
    """Generate realistic simulated trade data using real market prices"""
    
    asset_type = random.choices(
        ["stock", "crypto", "meme"],
        weights=[40, 35, 25],
        k=1
    )[0]
    
    trade_data = price_sim.generate_realistic_trade(asset_type=asset_type)
    
    trader_name = get_random_trader()
    strategy = random.choice(STRATEGIES)
    reason = random.choice(REASONS)
    txid = generate_txid()
    
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
        "portfolio_value": random.uniform(50000, 500000)
    }

async def post_trade():
    """Generate and post a trade to Telegram"""
    
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not set. Cannot post trade.")
        return False
    
    if not CHANNEL_ID:
        logger.error("CHANNEL_ID not set. Cannot post trade.")
        return False
    
    try:
        # Generate trade data
        trade = generate_trade_data()
        logger.info(f"Generated trade for {trade['symbol']}: {trade['profit']:+.2f} USD ({trade['roi']:+.2f}%)")
        
        # Create ultra-realistic mobile app screenshot
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
            device_type=random.choice(["ios", "android"])
        )
        
        # Save image
        image_path = save_trade_image(img, trade["txid"])
        logger.info(f"Saved trade image: {image_path}")
        
        # Save to database
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
        logger.info(f"Trade saved to database with TXID: {trade['txid']}")
        
        # Prepare caption
        profit_emoji = "📈" if trade["profit"] >= 0 else "📉"
        profit_sign = "+" if trade["profit"] >= 0 else ""
        roi_sign = "+" if trade["roi"] >= 0 else ""
        
        caption = f"""{profit_emoji} <b>{trade['symbol']}</b> Trade Filled

💰 <b>Profit:</b> {profit_sign}${trade['profit']:,.2f}
📊 <b>ROI:</b> {roi_sign}{trade['roi']:.2f}%
💵 <b>Invested:</b> ${trade['deposit']:,.2f}
👤 <b>Trader:</b> {trade['trader_name']}
🏦 <b>Broker:</b> {trade['broker_name']}

<a href="https://{DOMAIN}/log/{trade['txid']}">🔗 View Full Verification Report</a>"""
        
        # Send to Telegram
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        with open(image_path, 'rb') as photo:
            await bot.send_photo(
                chat_id=CHANNEL_ID,
                photo=photo,
                caption=caption,
                parse_mode='HTML'
            )
        
        logger.info(f"✅ Trade posted successfully to Telegram!")
        return True
        
    except Exception as e:
        logger.error(f"Error posting trade: {e}", exc_info=True)
        return False

async def run_bot():
    """Main bot loop - posts trades periodically"""
    logger.info("🤖 Profit Flex Bot starting...")
    
    if not TELEGRAM_BOT_TOKEN or not CHANNEL_ID:
        logger.error("Missing TELEGRAM_BOT_TOKEN or CHANNEL_ID. Please set them in environment variables.")
        logger.info("Bot will not post to Telegram but can still generate trades for the database.")
        logger.info("Use the web interface at /api/recent to view generated trades.")
    else:
        logger.info(f"Bot configured to post to channel: {CHANNEL_ID}")
    
    post_count = 0
    while True:
        try:
            # Post a trade
            success = await post_trade()
            
            if success:
                post_count += 1
                logger.info(f"Total trades posted: {post_count}")
            
            # Wait between 30-120 minutes for realistic posting
            wait_time = random.randint(1800, 7200)
            logger.info(f"Waiting {wait_time//60} minutes before next trade...")
            await asyncio.sleep(wait_time)
            
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
            break
        except Exception as e:
            logger.error(f"Error in main loop: {e}", exc_info=True)
            await asyncio.sleep(300)

def main():
    """Entry point"""
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        logger.info("Bot shutting down...")

if __name__ == "__main__":
    main()
