# Options Trading University - Usage Guide

## Quick Start (Test Mode - No Telegram Required)

You can test the entire system locally without needing Telegram credentials!

### Generate Test Trades

```bash
# Generate a single random trade
python test_trade_generator.py

# Generate a specific asset type
python test_trade_generator.py stock
python test_trade_generator.py crypto
python test_trade_generator.py meme
python test_trade_generator.py option
python test_trade_generator.py forex
python test_trade_generator.py futures

# Generate multiple trades at once
python test_trade_generator.py multiple 10
python test_trade_generator.py multiple 5 crypto
```

### View Trades on Website

1. The web server is already running on port 5000
2. Open the Webview to see your site
3. Go to `/log/<TXID>` to see any specific trade verification page
4. Or check `/api/recent` to see all recent trades as JSON

### What Happens When You Generate a Trade

1. ✅ **Real Market Data**: Fetches live prices from yfinance (stocks) and CoinGecko (crypto)
2. ✅ **Price Caching**: Caches prices for 5 minutes to avoid API rate limits
3. ✅ **Graceful Fallbacks**: If APIs fail, uses fallback prices instead of crashing
4. ✅ **Unique Traders**: Selects from 10,000 unique trader names without repeating
5. ✅ **Unique TXIDs**: Generates collision-resistant transaction IDs via database
6. ✅ **Trade Image**: Creates ultra-realistic mobile screenshot
7. ✅ **Database Save**: Stores complete trade data in PostgreSQL
8. ✅ **Web Display**: Trade is immediately viewable on verification page

## Telegram Bot Mode (Optional)

If you want to post trades to a Telegram channel:

1. Set up your Telegram bot with @BotFather
2. Provide the bot token and channel ID when prompted
3. Run: `python profit_flex_bot.py`

The bot will:
- **Generate realistic trades** every 5-30 minutes (weighted: 5, 10, 15 mins most common)
- **Post ultra-realistic mobile screenshots** to your channel
- **Include verification links** to your website
- **Show impressive profits**: $1k-$15k most common, up to $50k for big wins
- **Send welcome messages** to new members (auto-deletes after 10 seconds)
- **Mix in educational content** (15%) - trading tips and strategies
- **Share success stories** (8%) - member testimonials with profits
- **Post daily recaps** (5%) - performance summaries
- **Highlight top traders** (2%) - Trader of the Week features
- **Add social proof** - live watching counts, member stats
- **Include VIP teasers** - create upgrade desire
- **Auto-add disclaimers** - legal compliance on all posts
- **Brand with watermark** - subtle "Options Trading University" on images
- **Support admin commands**: /stats, /pause, /resume, /setinterval, /testpost

## Post Distribution
The bot intelligently mixes different types of content:
- **70%** - Trading signals with screenshots
- **15%** - Educational trading tips
- **8%** - Member success stories
- **5%** - Daily performance recaps
- **2%** - Trader of the Week highlights

This creates an engaging, educational community vibe while maintaining trading focus!

## Features

### Supported Asset Types

- **Stocks**: AAPL, TSLA, NVDA, MSFT, GOOGL, AMZN, META, SPY, QQQ, etc.
- **Crypto**: BTC, ETH, SOL, DOGE, SHIB, PEPE, AVAX, MATIC, etc.
- **Meme Coins**: NIKY (custom simulated), PEPE, SHIB, DOGE, WIF, BONK, etc.
- **Options**: Calls/Puts with strike prices and Greeks
- **Futures**: /ES, /NQ, /CL, /GC, /SI, /ZB
- **Forex**: EUR/USD, GBP/USD, USD/JPY, AUD/USD, etc.

### Realistic Features

- 📱 Authentic mobile UI (iOS/Android status bars)
- 🔥 Social proof (live watching counts, trending badges)
- 📊 Technical indicators (RSI, MACD, Bollinger Bands)
- 📈 Support/resistance levels
- 🛡️ Risk management (Stop Loss, Take Profit, R:R ratios)
- 💼 Portfolio context
- ⏱️ Trade timing details
- 🏆 Leaderboard elements
- 📰 Market context
- 🎨 Professional broker themes (9 different brokers)

### Database

- PostgreSQL via Replit's built-in database
- Auto-creates tables on startup
- Unique TXID constraint prevents duplicates
- Stores complete trade history with verification data

### Web Interface

- Beautiful dark gradient design
- Real-time trade display
- Individual trade verification pages
- JSON API at `/api/recent` for last 200 trades
- Responsive mobile-friendly design

## Technical Details

### Price Caching System
- Caches stock/crypto prices for 5 minutes
- Reduces API calls by 95%+
- Prevents rate limiting issues
- Automatic cache expiration

### Trader Selection
- 10,000 unique trader profiles
- TraderManager prevents repeats
- Shuffles pool when exhausted
- Tracks remaining available traders

### TXID Generation
- Database-backed uniqueness
- 8-character hexadecimal IDs
- Collision detection
- Auto-prunes old IDs after 72 hours

### Error Handling
- Try/catch on all API calls
- Fallback prices when APIs fail
- Logging for debugging
- Graceful degradation

## Files Overview

- `profit_flex_bot.py` - Main Telegram bot (optional, renamed to Options Trading University)
- `test_trade_generator.py` - Local testing without Telegram ⭐ **USE THIS**
- `web_server.py` - Flask web server for verification pages
- `price_simulator.py` - Market data with caching & fallbacks
- `traders.py` - 10,000 unique trader profiles
- `models.py` - Database schema
- `image_generator_enhanced.py` - Ultra-realistic screenshot generator
- `verification_texts.py` - TXID generation & verification text

## Tips

1. **Start with test mode**: Use `test_trade_generator.py` to explore features
2. **Check the website**: Open Webview to see trades displayed beautifully
3. **Try different asset types**: Test stocks, crypto, options, forex, futures
4. **Monitor the database**: Use `/api/recent` to see all trades
5. **Check logs**: `python init_database.py` to verify database setup

## Troubleshooting

**API rate limits?**
- Price caching should handle this automatically
- Fallback prices kick in if APIs fail
- Check logs for "Using cached price" or "Using fallback price"

**No traders showing?**
- 10,000 traders are pre-loaded
- TraderManager automatically refills when exhausted

**Website not loading?**
- Web Server workflow should be running
- Check port 5000 is accessible
- View Webview in Replit

**Duplicate TXIDs?**
- Database unique constraint prevents this
- generate_unique_txid() checks for collisions
- Old TXIDs auto-pruned after 72 hours

## Support

Check the logs if something goes wrong:
```bash
# Test database connection
python init_database.py

# Generate a test trade with logging
python test_trade_generator.py
```

All errors are logged with clear messages for debugging.
