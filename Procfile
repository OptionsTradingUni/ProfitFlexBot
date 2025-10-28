web: gunicorn --bind=0.0.0.0:${PORT:-5000} --reuse-port --workers=2 web_server:app
worker: python profit_flex_bot.py
