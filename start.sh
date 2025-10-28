#!/bin/bash
# Start script for Railway deployment

# Use Railway's PORT or default to 5000
export PORT=${PORT:-5000}

echo "Starting web server on port $PORT..."
gunicorn --bind=0.0.0.0:$PORT --reuse-port --workers=2 web_server:app &

echo "Starting Telegram bot..."
python profit_flex_bot.py
