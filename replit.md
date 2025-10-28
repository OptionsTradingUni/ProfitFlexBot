# Profit Flex Bot - Ultra-Realistic Mobile Trading App Screenshot Generator

## Overview
A professional Telegram bot that delivers highly authentic trading insights for stocks, crypto, and meme coins. Features ultra-realistic mobile app-style screenshots that look like actual phone captures from Robinhood, Coinbase, Webull, and other trading platforms. Includes custom meme coin NIKY with simulated price action.

## Project Structure
```
├── profit_flex_bot.py           # Main Telegram bot logic
├── web_server.py                # Flask web server for trade logs
├── image_generator_enhanced.py  # Ultra-realistic mobile screenshot generator
├── image_generator.py           # Original professional image generation (legacy)
├── price_simulator.py           # Real market prices + NIKY custom coin simulator
├── models.py                    # Database models and tables
├── traders.py                   # 10,000 authentic trader profiles
├── verification_texts.py        # TXID and verification text generation
├── stock_verification.py        # Broker/exchange verification templates
├── test_enhanced_features.py    # Test script for all enhanced features
├── templates/                   # HTML templates for web interface
│   ├── log_template.html       # Enhanced trade log viewer
│   └── 404.html                # Error page
├── trade_images/                # Generated mobile screenshot images
├── requirements.txt             # Python dependencies
└── .env                         # Environment configuration
```

## Ultra-Realistic Mobile Features (NEW)
- 📱 **Authentic Mobile UI**: iOS/Android status bars with battery, signal strength, time
- 🔥 **Social Proof**: Live watching counts (20k watching), trending badges, community followers, win streaks
- 📊 **Advanced Technical Indicators**: RSI, MACD histogram, Bollinger Bands, Fibonacci retracement
- 📈 **Support/Resistance Levels**: Realistic chart markings with price levels
- 🛡️ **Risk Management Display**: Stop Loss, Take Profit targets (TP1, TP2), Risk:Reward ratios
- 💼 **Portfolio Context**: Total portfolio value, position size percentage
- ⏱️ **Trade Timing**: Position hold duration, entry/exit timestamps
- 🏆 **Leaderboard Elements**: Rank badges (Top 3%), win rates, profit streaks
- 📰 **Market Context**: Live news ticker, market sentiment, volatility indicators
- 🎨 **Screenshot Style**: Rounded corners, mobile navigation bar, authentic app design
- 🪙 **NIKY Custom Meme Coin**: Simulated price movements with realistic volatility

## Standard Features
- ✅ Real-time market prices for stocks, crypto, options (yfinance, CoinGecko)
- ✅ Realistic candlestick charts with volume indicators
- ✅ 10,000+ authentic trader profiles
- ✅ Multiple broker themes (Robinhood, Webull, Binance, Coinbase, Schwab, Fidelity)
- ✅ PostgreSQL database for trade logs
- ✅ Web interface for trade verification
- ✅ Automated posting to Telegram channels

## Recent Changes
- **2025-10-28**: MAJOR UPDATE - Ultra-realistic mobile app screenshot generator
- **2025-10-28**: Added NIKY custom meme coin with price simulator
- **2025-10-28**: Integrated real market prices for stocks/crypto via yfinance & CoinGecko
- **2025-10-28**: Implemented RSI, MACD, Bollinger Bands technical indicators
- **2025-10-28**: Added social proof elements (engagement, trending, streaks)
- **2025-10-28**: Created risk management displays (SL, TP, R:R)
- **2025-10-28**: Added portfolio context and leaderboard elements
- **2025-10-28**: Mobile status bars, navigation, screenshot-style rounded corners
- **2025-10-27**: Enhanced image generation with professional broker UI styling
- **2025-10-27**: Added realistic chart generation with candlestick patterns

## Technology Stack
- **Backend**: Python 3.12, Flask, Gunicorn
- **Bot Framework**: python-telegram-bot 21.4
- **Database**: PostgreSQL (via SQLAlchemy)
- **Image Generation**: Matplotlib, Pillow
- **Market Data**: yfinance, pycoingecko, yahoo_fin, beautifulsoup4
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## Environment Variables
Required in `.env`:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
CHANNEL_ID=@your_channel_username
DATABASE_URL=postgresql://user:password@host:port/database
PORT=5000
SESSION_SECRET=your_secret_key_here
```

## User Preferences
- Professional, authentic-looking trade confirmations
- No mock data or placeholders in production
- Clean, modern UI design with dark themes
- Realistic market data and price movements
- Broker-specific branding and styling

## Deployment Notes
- Web server runs on port 5000
- Telegram bot runs as background worker
- Database migrations handled automatically via SQLAlchemy
- Trade images stored in `trade_images/` directory
