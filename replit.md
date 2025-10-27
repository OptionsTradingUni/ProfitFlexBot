# Profit Flex Bot - Professional Trading Insights Bot

## Overview
A professional Telegram bot that delivers authentic trading insights for stocks, crypto, and meme coins with realistic profit/loss scenarios. Features professional broker-style trade confirmations with enhanced image generation.

## Project Structure
```
├── profit_flex_bot.py      # Main Telegram bot logic
├── web_server.py            # Flask web server for trade logs
├── image_generator.py       # Professional image generation module
├── models.py                # Database models and tables
├── traders.py               # 10,000 authentic trader profiles
├── verification_texts.py    # TXID and verification text generation
├── stock_verification.py    # Broker/exchange verification templates
├── templates/               # HTML templates for web interface
│   ├── log_template.html   # Enhanced trade log viewer
│   └── 404.html            # Error page
├── static/                  # Static assets
│   └── images/             # Generated trade images
├── requirements.txt         # Python dependencies
└── .env                     # Environment configuration

```

## Features
- ✅ Professional broker-style trade images with authentic UI
- ✅ Real-time market data integration (yfinance, CoinGecko, Coinbase)
- ✅ Realistic candlestick charts with price movements
- ✅ 10,000+ authentic trader profiles
- ✅ Multiple broker themes (Robinhood, Webull, Schwab, Fidelity, Binance, Coinbase)
- ✅ PostgreSQL database for trade logs
- ✅ Web interface for trade verification
- ✅ Automated posting to Telegram channels

## Recent Changes
- **2025-10-27**: Enhanced image generation with professional broker UI styling
- **2025-10-27**: Added realistic chart generation with candlestick patterns
- **2025-10-27**: Implemented multi-broker theme support
- **2025-10-27**: Created responsive web interface with gradient designs
- **2025-10-27**: Added comprehensive verification text system

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
