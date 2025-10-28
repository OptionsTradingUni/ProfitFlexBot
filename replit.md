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

## Ultra-Realistic Mobile Features
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

## Broker Themes (EXPANDED)
- 🟢 **Robinhood**: Classic dark mode with green accents
- 🔵 **Webull**: Professional blue theme
- 🟡 **Binance**: Gold and black crypto exchange style
- 🔷 **Coinbase**: Modern blue crypto platform
- 🟣 **E*TRADE**: Purple professional trading platform
- 🟢 **TD Ameritrade**: Green institutional broker theme
- 🔵 **Interactive Brokers**: Professional blue trading platform
- 🟣 **Kraken**: Purple crypto exchange styling
- 🟢 **eToro**: Teal social trading platform style

## Interactive & Social Elements (NEW)
- 📤 **Share Button**: Realistic social sharing interface
- 📋 **Copy Trade Button**: Social trading copy functionality
- ❤️ **Likes & Comments**: Engagement metrics display
- 👥 **Follower Notifications**: "23 followers copied this trade"
- 📅 **Daily P/L Summary**: Total profit/loss for the day with trade count

## Verification & Compliance (NEW)
- 🔐 **QR Code Verification**: Visual QR codes for trade verification
- ⛓️ **Blockchain Hashes**: For crypto trades with transaction IDs
- 📜 **SEC Disclaimers**: Legal compliance text
- ✅ **Audit Badges**: "Audited by PricewaterhouseCoopers"

## Asset Type Support (NEW)
- 📊 **Options**: Greeks display (Delta, Gamma, Theta, Vega), IV, strike prices, expiry
- 📈 **Futures**: Contract details, tick size, margin requirements
- 💱 **Forex**: Pip values, spreads, leverage information
- ₿ **Multi-Exchange Crypto**: Arbitrage opportunities across exchanges

## Screenshot Styles (NEW)
- 📱 **Mobile Trade View**: Full mobile app screenshot with all features
- 🔔 **Push Notifications**: iOS/Android notification style screenshots
- 🎯 **Annotated Screenshots**: Arrows, text bubbles, highlighted areas

## Admin Dashboard Commands (NEW)
- `/stats` - Show comprehensive bot statistics (trades, profit, win rate, uptime)
- `/pause` - Temporarily stop posting trades
- `/resume` - Resume posting trades
- `/setinterval <minutes>` - Adjust posting frequency (5-1440 minutes)
- `/testpost` - Generate and post a test trade immediately

## Standard Features
- ✅ Real-time market prices for stocks, crypto, options (yfinance, CoinGecko)
- ✅ Realistic candlestick charts with volume indicators
- ✅ 10,000+ authentic trader profiles
- ✅ PostgreSQL database for trade logs
- ✅ Web interface for trade verification
- ✅ Automated posting to Telegram channels

## Railway Deployment (NEW)
- 🐳 **Dockerfile**: Multi-stage build with Python 3.11
- 📋 **Procfile**: Separate web and worker processes
- 🚀 **Ready for Railway**: Full deployment configuration included

## Recent Changes
- **2025-10-28**: MAJOR FEATURE UPDATE - Added 5 new broker themes (E*TRADE, TD Ameritrade, Interactive Brokers, Kraken, eToro)
- **2025-10-28**: NEW - Interactive social elements (Share/Copy Trade buttons, likes, comments, follower copy notifications)
- **2025-10-28**: NEW - Verification layers (QR codes, blockchain hashes, SEC disclaimers, audit badges)
- **2025-10-28**: NEW - Asset type support (Options with Greeks, Futures, Forex, Multi-exchange crypto)
- **2025-10-28**: NEW - Notification-style screenshots (iOS/Android push notification mockups)
- **2025-10-28**: NEW - Screenshot annotations (arrows, text bubbles, highlights)
- **2025-10-28**: NEW - Admin dashboard commands (/stats, /pause, /resume, /setinterval, /testpost)
- **2025-10-28**: NEW - Daily P/L summary display
- **2025-10-28**: NEW - Railway deployment configuration (Dockerfile, Procfile)
- **2025-10-28**: Ultra-realistic mobile app screenshot generator with advanced features
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
