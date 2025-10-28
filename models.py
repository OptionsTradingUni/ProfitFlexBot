# models.py

import os
from datetime import datetime
from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, 
                          String, Float, DateTime, text)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise SystemExit("FATAL: DATABASE_URL environment variable is not set. Please set up the PostgreSQL database.")

# Fix Railway's DATABASE_URL if it contains unexpanded variables or placeholders
if DATABASE_URL:
    import re
    
    # Replace $VAR or ${VAR} style variables
    if "$" in DATABASE_URL:
        port = os.getenv("PORT", "5432")
        DATABASE_URL = re.sub(r'\$\{?PORT\}?', port, DATABASE_URL)
        DATABASE_URL = DATABASE_URL.replace("$PGPORT", os.getenv("PGPORT", "5432"))
        DATABASE_URL = DATABASE_URL.replace("$PGHOST", os.getenv("PGHOST", "localhost"))
        DATABASE_URL = DATABASE_URL.replace("$PGUSER", os.getenv("PGUSER", "postgres"))
        DATABASE_URL = DATABASE_URL.replace("$PGPASSWORD", os.getenv("PGPASSWORD", ""))
        DATABASE_URL = DATABASE_URL.replace("$PGDATABASE", os.getenv("PGDATABASE", "postgres"))
    
    # Fix malformed URLs with literal "port" instead of port number
    # Pattern: postgresql://user:pass@host:port/db where "port" is literal
    if ":port/" in DATABASE_URL or ":port@" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace(":port/", ":5432/").replace(":port@", ":5432@")
        print(f"⚠️ WARNING: Fixed malformed DATABASE_URL containing literal 'port' placeholder")

engine = create_engine(DATABASE_URL, future=True)
metadata = MetaData()

# All your table definitions now live here
posts = Table(
    "posts", metadata,
    Column("id", Integer, primary_key=True),
    Column("symbol", String),
    Column("content", String),
    Column("deposit", Float),
    Column("profit", Float),
    Column("posted_at", DateTime)
)

users = Table(
    "users", metadata,
    Column("user_id", String, primary_key=True),
    Column("username", String),
    Column("display_name", String),
    Column("wins", Integer, default=0),
    Column("total_trades", Integer, default=0),
    Column("total_profit", Float, default=0)
)

success_stories = Table(
    "success_stories", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("trader_name", String, unique=True),
    Column("gender", String),
    Column("story", String),
    Column("image", String)
)

rankings_cache = Table(
    "rankings_cache", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("content", String),
    Column("timestamp", DateTime)
)

# ===============================
# TRADE LOGS TABLE DEFINITION
# ===============================

trade_logs = Table(
    "trade_logs",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("txid", String(16), unique=True, nullable=False),
    Column("timestamp", DateTime, default=datetime.utcnow),
    Column("symbol", String(50)),
    Column("trader_name", String(100)),
    Column("broker_name", String(100), default="Interactive Brokers"),
    Column("direction", String(10), default="BUY"),
    Column("status", String(20), default="Filled"),
    Column("quantity", Float),
    Column("deposit", Float),
    Column("profit", Float),
    Column("roi", Float),
    Column("strategy", String(200)),
    Column("reason", String(500)),
    Column("entry_price", Float),
    Column("exit_price", Float),
    Column("total_value_exit", Float),
    Column("commission", Float),
    Column("slippage", Float),
    Column("posted_at", DateTime, default=datetime.utcnow),
)

try:
    metadata.create_all(engine, checkfirst=True)
except Exception as e:
    import logging
    logging.warning(f"Database tables may already exist: {e}")
    metadata.reflect(bind=engine)
