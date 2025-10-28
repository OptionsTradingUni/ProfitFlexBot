# Options Trading University - Ultra-Realistic Mobile Trading App Screenshot Generator

## Overview
The "Options Trading University" project is a professional Telegram bot designed to deliver highly authentic trading insights across stocks, crypto, and meme coins. Its core purpose is to generate ultra-realistic mobile app-style screenshots that mimic popular trading platforms like Robinhood, Coinbase, and Webull. This includes a custom meme coin, NIKY, with simulated price action. The project aims to provide an engaging and educational experience, coupled with robust social proof and compliance features, positioning itself as a leader in simulated trading content generation.

## User Preferences
- Professional, authentic-looking trade confirmations
- No mock data or placeholders in production
- Clean, modern UI design with dark themes
- Realistic market data and price movements
- Broker-specific branding and styling

## System Architecture
The project is built around a Python-based Telegram bot (`profit_flex_bot.py`) and a Flask web server (`web_server.py`) for displaying trade logs. A crucial component is the `image_generator_enhanced.py`, responsible for creating ultra-realistic mobile trading app screenshots. These screenshots feature authentic mobile UI elements (status bars, battery, signal), social proof (watching counts, trending badges), advanced technical indicators (RSI, MACD, Bollinger Bands), risk management displays (Stop Loss, Take Profit), and portfolio context.

The system supports various broker themes (Robinhood, Webull, Binance, Coinbase, E*TRADE, TD Ameritrade, Interactive Brokers, Kraken, eToro) and includes interactive elements like share buttons, copy trade functionality, and engagement metrics. Verification features such as QR codes, blockchain hashes, and SEC disclaimers are integrated. The system handles multiple asset types, including Options (with Greeks display), Futures, and Forex. It also generates different screenshot styles, including full mobile trade views, push notifications, and annotated screenshots.

A PostgreSQL database, managed via SQLAlchemy (`models.py`), stores trade logs and a library of 10,000 authentic trader profiles (`traders.py`). The web interface for trade verification is fully featured with dark/light themes, search functionality, asset filters, performance charts (Chart.js), a top traders leaderboard, live tickers, trade modals, and CSV export. The bot also incorporates extensive content libraries for educational tips, market analysis, success stories, risk warnings, community posts, and trader testimonials, which are integrated into a dynamic posting schedule. Admin commands are available for bot management.

The application is designed for deployment on Railway, utilizing a multi-stage Dockerfile and a Procfile to manage web and worker processes.

## External Dependencies
- **Telegram Bot API**: For bot interaction (`python-telegram-bot`)
- **PostgreSQL**: Primary database for data storage
- **yfinance**: For real-time stock market data
- **pycoingecko**: For real-time cryptocurrency data
- **Flask**: Web framework for the administrative interface
- **Gunicorn**: WSGI HTTP Server for Flask
- **SQLAlchemy**: ORM for database interactions
- **Matplotlib**: For chart generation within images
- **Pillow**: For image manipulation
- **yahoo_fin**: Market data fetching
- **beautifulsoup4**: For web scraping (implied for market data)
- **Chart.js**: For interactive charts in the web interface