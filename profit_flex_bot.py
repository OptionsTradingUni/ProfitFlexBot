"""
Options Trading University Bot - Main Bot Logic
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
from traders import get_unique_trader
from verification_texts import generate_unique_txid
from image_generator_enhanced import create_ultra_realistic_mobile_trade_screenshot, save_trade_image
from price_simulator import price_sim
from market_analyzer import market_analyzer
from content_generators import (
    get_educational_tip, get_success_story, get_social_proof,
    get_hot_alert, get_vip_teaser, get_disclaimer,
    generate_daily_recap, generate_weekly_recap, generate_trader_of_week
)

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
        ["stock", "crypto", "meme", "option", "futures", "forex", "crypto_multi"],
        weights=[30, 25, 15, 10, 10, 5, 5],
        k=1
    )[0]
    
    trade_data = price_sim.generate_realistic_trade(asset_type=asset_type)
    
    trader_name = get_unique_trader()
    strategy = random.choice(STRATEGIES)
    
    # Get market-aware reasoning
    sentiment = market_analyzer.get_market_sentiment()
    reason = market_analyzer.generate_market_reasoning(
        trade_data['symbol'], 
        trade_data['direction'],
        sentiment
    )
    
    # Get market tags
    market_tags = market_analyzer.get_market_tags()
    win_streak = market_analyzer.get_win_streak_tag()
    
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
        "asset_type": asset_type,
        "market_tags": market_tags,
        "win_streak": win_streak
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
            device_type=random.choice(["ios", "android"]),
            asset_type=trade.get("asset_type", "stock")
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
        
        # Build market tags line
        tags_line = ""
        if trade.get("market_tags"):
            tags_line = "   ".join(trade["market_tags"]) + "\n"
        
        # Build win streak line
        streak_line = ""
        if trade.get("win_streak") and trade["profit"] > 0:
            streak_line = f"{trade['win_streak']}\n"
        
        # Add hot alert for big wins
        hot_alert = ""
        if trade["profit"] > 10000:
            hot_alert = get_hot_alert(trade['symbol']) + "\n\n"
        
        # Add social proof randomly
        social_proof = ""
        if random.random() < 0.3:
            social_proof = "\n" + get_social_proof()
        
        # Add VIP teaser for high-profit trades
        vip_teaser = ""
        if trade["profit"] > 5000 and random.random() < 0.4:
            vip_teaser = "\n" + get_vip_teaser()
        
        # Get disclaimer
        disclaimer = get_disclaimer()
        
        caption = f"""{hot_alert}{profit_emoji} <b>{trade['symbol']}</b> Trade Filled

{tags_line}{streak_line}
💰 <b>Profit:</b> {profit_sign}${trade['profit']:,.2f}
📊 <b>ROI:</b> {roi_sign}{trade['roi']:.2f}%
💵 <b>Invested:</b> ${trade['deposit']:,.2f}
👤 <b>Trader:</b> {trade['trader_name']}
🏦 <b>Broker:</b> {trade['broker_name']}
{social_proof}{vip_teaser}

<a href="https://{DOMAIN}/log/{trade['txid']}">🔗 View Full Verification Report</a>

{disclaimer}"""
        
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

async def post_educational_tip():
    """Post an educational trading tip"""
    if not TELEGRAM_BOT_TOKEN or not CHANNEL_ID:
        return False
    
    try:
        tip = get_educational_tip()
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=tip,
            parse_mode='Markdown'
        )
        logger.info("✅ Educational tip posted successfully!")
        return True
    except Exception as e:
        logger.error(f"Error posting educational tip: {e}")
        return False

async def post_success_story():
    """Post a member success story"""
    if not TELEGRAM_BOT_TOKEN or not CHANNEL_ID:
        return False
    
    try:
        story = get_success_story()
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=story,
            parse_mode='Markdown'
        )
        logger.info("✅ Success story posted successfully!")
        return True
    except Exception as e:
        logger.error(f"Error posting success story: {e}")
        return False

async def post_daily_recap():
    """Post daily trading recap"""
    if not TELEGRAM_BOT_TOKEN or not CHANNEL_ID:
        return False
    
    try:
        from sqlalchemy import select, func
        with engine.connect() as conn:
            today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0)
            
            total_trades = conn.execute(
                select(func.count()).select_from(trade_logs).where(trade_logs.c.posted_at >= today_start)
            ).scalar() or 0
            
            total_profit = conn.execute(
                select(func.sum(trade_logs.c.profit)).where(trade_logs.c.posted_at >= today_start)
            ).scalar() or 0
            
            winning_trades = conn.execute(
                select(func.count()).select_from(trade_logs).where(
                    trade_logs.c.posted_at >= today_start,
                    trade_logs.c.profit > 0
                )
            ).scalar() or 0
            
            win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0
            
            best_trade = conn.execute(
                select(func.max(trade_logs.c.profit)).where(trade_logs.c.posted_at >= today_start)
            ).scalar() or 0
        
        stats = {
            'total_trades': total_trades,
            'total_profit': total_profit,
            'win_rate': win_rate,
            'best_trade': best_trade
        }
        
        recap = generate_daily_recap(stats)
        
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=recap,
            parse_mode='Markdown'
        )
        logger.info("✅ Daily recap posted successfully!")
        return True
    except Exception as e:
        logger.error(f"Error posting daily recap: {e}")
        return False

async def post_trader_of_week():
    """Post Trader of the Week feature"""
    if not TELEGRAM_BOT_TOKEN or not CHANNEL_ID:
        return False
    
    try:
        from sqlalchemy import select
        
        top_trader = get_unique_trader()
        
        trader_stats = {
            'name': top_trader,
            'trades': random.randint(15, 45),
            'profit': random.uniform(15000, 75000),
            'win_rate': random.uniform(75, 95),
            'streak': random.randint(5, 15)
        }
        
        message = generate_trader_of_week(trader_stats)
        
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode='Markdown'
        )
        logger.info("✅ Trader of the Week posted successfully!")
        return True
    except Exception as e:
        logger.error(f"Error posting Trader of the Week: {e}")
        return False

async def run_bot():
    """Main bot loop - posts trades periodically"""
    logger.info("🤖 Options Trading University Bot starting...")
    
    if not TELEGRAM_BOT_TOKEN or not CHANNEL_ID:
        logger.error("Missing TELEGRAM_BOT_TOKEN or CHANNEL_ID. Please set them in environment variables.")
        logger.info("Bot will not post to Telegram but can still generate trades for the database.")
        logger.info("Use the web interface at /api/recent to view generated trades.")
    else:
        logger.info(f"Bot configured to post to channel: {CHANNEL_ID}")
    
    post_count = 0
    
    while True:
        try:
            # Check if bot is paused
            if bot_state["paused"]:
                logger.info("Bot is paused. Waiting...")
                await asyncio.sleep(60)
                continue
            
            # Determine what type of post to make
            # 70% trades, 15% educational, 8% success stories, 5% daily recap, 2% trader of week
            post_type = random.choices(
                ['trade', 'education', 'success', 'recap', 'trader_week'],
                weights=[70, 15, 8, 5, 2],
                k=1
            )[0]
            
            success = False
            
            if post_type == 'trade':
                success = await post_trade()
            elif post_type == 'education':
                success = await post_educational_tip()
            elif post_type == 'success':
                success = await post_success_story()
            elif post_type == 'recap':
                success = await post_daily_recap()
            elif post_type == 'trader_week':
                success = await post_trader_of_week()
            
            if success:
                bot_state["total_posts"] += 1
                logger.info(f"Total trades posted: {bot_state['total_posts']}")
            
            # Wait between configured intervals with weighted selection
            # Common intervals: 5, 10, 15 mins (very common), 20 mins (common), 25-30 mins (less common)
            interval_choices = [
                (5, 0.20),
                (7, 0.10),
                (10, 0.25),
                (12, 0.10),
                (15, 0.20),
                (18, 0.05),
                (20, 0.05),
                (25, 0.03),
                (30, 0.02)
            ]
            
            wait_minutes = random.choices(
                [mins for mins, _ in interval_choices],
                weights=[weight for _, weight in interval_choices],
                k=1
            )[0]
            
            wait_time = wait_minutes * 60
            logger.info(f"Waiting {wait_minutes} minutes before next trade...")
            await asyncio.sleep(wait_time)
            
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
            break
        except Exception as e:
            logger.error(f"Error in main loop: {e}", exc_info=True)
            await asyncio.sleep(300)

# Bot control state
bot_state = {
    "paused": False,
    "post_interval_min": 5,
    "post_interval_max": 30,
    "total_posts": 0,
    "start_time": datetime.now(timezone.utc)
}

async def handle_stats_command(update, context):
    """Show bot statistics"""
    from sqlalchemy import select, func
    
    try:
        with engine.connect() as conn:
            total_trades = conn.execute(select(func.count()).select_from(trade_logs)).scalar() or 0
            total_profit = conn.execute(select(func.sum(trade_logs.c.profit))).scalar() or 0
            avg_roi = conn.execute(select(func.avg(trade_logs.c.roi))).scalar() or 0
            
            winning_trades = conn.execute(
                select(func.count()).select_from(trade_logs).where(trade_logs.c.profit > 0)
            ).scalar() or 0
            
            win_rate = (winning_trades / total_trades * 100) if total_trades and total_trades > 0 else 0
        
        uptime = datetime.now(timezone.utc) - bot_state["start_time"]
        uptime_hours = uptime.total_seconds() / 3600
        
        stats_message = f"""📊 <b>Options Trading University Statistics</b>

🔢 <b>Total Trades:</b> {total_trades}
💰 <b>Total Profit:</b> ${total_profit:,.2f}
📈 <b>Average ROI:</b> {avg_roi:.2f}%
✅ <b>Win Rate:</b> {win_rate:.1f}%
⏱️ <b>Uptime:</b> {uptime_hours:.1f} hours
📤 <b>Posts Today:</b> {bot_state['total_posts']}
⏸️ <b>Status:</b> {'Paused' if bot_state['paused'] else 'Active'}
🕐 <b>Post Interval:</b> {bot_state['post_interval_min']}-{bot_state['post_interval_max']} minutes
"""
        
        await update.message.reply_text(stats_message, parse_mode='HTML')
        logger.info("Stats command executed")
        
    except Exception as e:
        logger.error(f"Error in stats command: {e}")
        await update.message.reply_text("Error retrieving statistics")

async def handle_pause_command(update, context):
    """Pause bot posting"""
    bot_state["paused"] = True
    await update.message.reply_text("⏸️ Bot paused. Use /resume to continue posting.")
    logger.info("Bot paused via command")

async def handle_resume_command(update, context):
    """Resume bot posting"""
    bot_state["paused"] = False
    await update.message.reply_text("▶️ Bot resumed. Posting will continue.")
    logger.info("Bot resumed via command")

async def handle_setinterval_command(update, context):
    """Set posting interval in minutes"""
    try:
        if not context.args or len(context.args) != 1:
            await update.message.reply_text("Usage: /setinterval <minutes>\nExample: /setinterval 60")
            return
        
        minutes = int(context.args[0])
        
        if minutes < 5 or minutes > 1440:
            await update.message.reply_text("⚠️ Interval must be between 5 and 1440 minutes (24 hours)")
            return
        
        bot_state["post_interval_min"] = minutes
        bot_state["post_interval_max"] = minutes + 30
        
        await update.message.reply_text(f"✅ Posting interval set to {minutes}-{minutes+30} minutes")
        logger.info(f"Posting interval changed to {minutes} minutes")
        
    except ValueError:
        await update.message.reply_text("⚠️ Please provide a valid number")
    except Exception as e:
        logger.error(f"Error setting interval: {e}")
        await update.message.reply_text("Error setting interval")

async def handle_testpost_command(update, context):
    """Generate and post a test trade immediately"""
    await update.message.reply_text("🧪 Generating test trade...")
    
    success = await post_trade()
    
    if success:
        await update.message.reply_text("✅ Test trade posted successfully!")
    else:
        await update.message.reply_text("❌ Failed to post test trade. Check logs for details.")

async def handle_new_member(update, context):
    """Send welcome message to new members and delete after 10 seconds"""
    try:
        for member in update.message.new_chat_members:
            welcome_message = f"""👋 Welcome to Options Trading University, {member.first_name}!

📚 Here you'll learn from real trading examples
📊 We share authentic market analysis and trade insights
💰 Track profitable strategies from experienced traders

Get ready to elevate your trading knowledge! 🚀"""
            
            sent_message = await update.message.reply_text(welcome_message)
            
            await asyncio.sleep(10)
            
            try:
                await sent_message.delete()
                await update.message.delete()
                logger.info(f"Welcome message sent and deleted for {member.first_name}")
            except Exception as e:
                logger.warning(f"Could not delete welcome message: {e}")
                
    except Exception as e:
        logger.error(f"Error in welcome handler: {e}")

def setup_admin_handlers(application):
    """Setup admin command handlers"""
    from telegram.ext import CommandHandler, MessageHandler, filters
    
    application.add_handler(CommandHandler("stats", handle_stats_command))
    application.add_handler(CommandHandler("pause", handle_pause_command))
    application.add_handler(CommandHandler("resume", handle_resume_command))
    application.add_handler(CommandHandler("setinterval", handle_setinterval_command))
    application.add_handler(CommandHandler("testpost", handle_testpost_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_member))
    
    logger.info("Admin command handlers and welcome message registered")

def main():
    """Entry point"""
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        logger.info("Bot shutting down...")

if __name__ == "__main__":
    main()
