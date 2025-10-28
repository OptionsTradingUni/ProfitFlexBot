"""
Price Simulator for Trading Bot
- Real market prices for stocks, crypto, options
- Simulated prices for custom meme coin NIKY
"""

import random
from datetime import datetime, timedelta
import yfinance as yf
from pycoingecko import CoinGeckoAPI
import requests

class PriceSimulator:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.niky_base_price = 0.00000147
        self.niky_volatility = 0.35
        self.niky_price_history = []
        
    def get_real_stock_price(self, symbol):
        """Get real stock price from yfinance"""
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")
            if not hist.empty:
                return float(hist['Close'].iloc[-1])
            data = ticker.info
            if 'regularMarketPrice' in data:
                return float(data['regularMarketPrice'])
            elif 'currentPrice' in data:
                return float(data['currentPrice'])
            return None
        except:
            return None
    
    def get_real_crypto_price(self, symbol):
        """Get real crypto price from CoinGecko"""
        try:
            symbol_clean = symbol.replace('USD', '').replace('USDT', '').lower()
            
            coin_map = {
                'btc': 'bitcoin',
                'eth': 'ethereum',
                'bnb': 'binancecoin',
                'sol': 'solana',
                'ada': 'cardano',
                'xrp': 'ripple',
                'doge': 'dogecoin',
                'shib': 'shiba-inu',
                'avax': 'avalanche-2',
                'dot': 'polkadot',
                'matic': 'matic-network',
                'link': 'chainlink',
                'pepe': 'pepe',
                'wif': 'dogwifhat',
                'bonk': 'bonk'
            }
            
            coin_id = coin_map.get(symbol_clean, symbol_clean)
            
            data = self.cg.get_price(ids=coin_id, vs_currencies='usd')
            if coin_id in data:
                return float(data[coin_id]['usd'])
            
            return None
        except:
            return None
    
    def get_niky_price(self, simulate_movement=True):
        """Get simulated price for NIKY meme coin"""
        if not simulate_movement:
            return self.niky_base_price
        
        if not self.niky_price_history:
            self.niky_price_history.append(self.niky_base_price)
        
        last_price = self.niky_price_history[-1]
        
        trend_change = random.choice([-1, -1, 0, 1, 1, 1])
        volatility_mult = random.uniform(0.8, 1.2)
        
        price_change_pct = random.uniform(-self.niky_volatility, self.niky_volatility) * volatility_mult
        
        news_events = random.random()
        if news_events < 0.05:
            price_change_pct *= random.uniform(2, 5)
        elif news_events < 0.10:
            price_change_pct *= random.uniform(-3, -1.5)
        
        new_price = last_price * (1 + price_change_pct)
        
        min_price = self.niky_base_price * 0.001
        max_price = self.niky_base_price * 1000
        new_price = max(min_price, min(max_price, new_price))
        
        self.niky_price_history.append(new_price)
        if len(self.niky_price_history) > 1000:
            self.niky_price_history = self.niky_price_history[-500:]
        
        return new_price
    
    def get_price(self, symbol, asset_type="auto"):
        """
        Get price for any asset
        - NIKY: simulated meme coin price
        - Stocks: real prices from yfinance
        - Crypto: real prices from CoinGecko
        - Options: derived from underlying stock
        """
        symbol_upper = symbol.upper()
        
        if symbol_upper == "NIKY" or "NIKY" in symbol_upper:
            return self.get_niky_price(simulate_movement=True)
        
        if asset_type == "crypto" or any(x in symbol_upper for x in ['BTC', 'ETH', 'DOGE', 'SHIB', 'PEPE', 'USDT', 'USD']):
            price = self.get_real_crypto_price(symbol_upper)
            if price:
                return price
        
        if asset_type == "stock" or asset_type == "auto":
            price = self.get_real_stock_price(symbol_upper)
            if price:
                return price
        
        if asset_type == "option":
            underlying = symbol_upper.split()[0] if ' ' in symbol_upper else symbol_upper[:4]
            base_price = self.get_real_stock_price(underlying)
            if base_price:
                strike_offset = random.uniform(-0.1, 0.1)
                return base_price * (1 + strike_offset)
        
        fallback_prices = {
            'AAPL': 175.0,
            'TSLA': 250.0,
            'NVDA': 880.0,
            'MSFT': 420.0,
            'GOOGL': 140.0,
            'AMZN': 175.0,
            'META': 485.0,
            'SPY': 500.0,
            'QQQ': 450.0,
        }
        
        return fallback_prices.get(symbol_upper, 100.0)
    
    def generate_realistic_trade(self, symbol=None, asset_type=None):
        """Generate a realistic trade with proper entry/exit prices"""
        
        if symbol is None:
            asset_types = {
                'stock': ['AAPL', 'TSLA', 'NVDA', 'MSFT', 'GOOGL', 'AMZN', 'META', 'SPY', 'QQQ'],
                'crypto': ['BTC', 'ETH', 'SOL', 'DOGE', 'SHIB', 'PEPE', 'AVAX', 'MATIC'],
                'meme': ['NIKY', 'NIKY', 'NIKY'],
                'option': ['AAPL 180C', 'TSLA 260C', 'NVDA 900C', 'SPY 510P', 'QQQ 460C'],
                'futures': ['/ES', '/NQ', '/CL', '/GC', '/SI', '/ZB'],
                'forex': ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/USD', 'USD/CAD', 'NZD/USD'],
                'crypto_multi': ['BTC', 'ETH', 'SOL', 'AVAX']
            }
            
            if asset_type is None:
                asset_type = random.choice(list(asset_types.keys()))
            
            symbol = random.choice(asset_types.get(asset_type, asset_types['stock']))
        
        if asset_type is None:
            if 'NIKY' in symbol.upper():
                asset_type = 'meme'
            elif any(x in symbol.upper() for x in ['BTC', 'ETH', 'DOGE', 'SOL']):
                asset_type = 'crypto'
            elif 'C' in symbol or 'P' in symbol:
                asset_type = 'option'
            else:
                asset_type = 'stock'
        
        current_price = self.get_price(symbol, asset_type)
        
        profit_scenario = random.random() > 0.25
        
        if profit_scenario:
            roi = random.uniform(5, 300)
            if asset_type == 'meme':
                roi = random.uniform(20, 1000)
            elif asset_type == 'crypto':
                roi = random.uniform(10, 200)
            elif asset_type == 'option':
                roi = random.uniform(30, 500)
            
            direction = "BUY"
            entry_price = current_price / (1 + roi / 100)
            exit_price = current_price
            profit_amount = random.uniform(100, 50000)
            deposit = profit_amount / (roi / 100)
        else:
            roi = random.uniform(-5, -50)
            direction = "BUY"
            entry_price = current_price / (1 + roi / 100)
            exit_price = current_price
            loss_amount = random.uniform(50, 5000)
            deposit = loss_amount / abs(roi / 100)
            profit_amount = -loss_amount
        
        quantity = deposit / entry_price
        
        brokers = {
            'stock': ['Robinhood', 'Webull', 'Charles Schwab', 'Fidelity', 'TD Ameritrade', 'E*TRADE'],
            'crypto': ['Binance', 'Coinbase', 'Kraken', 'Crypto.com', 'eToro'],
            'meme': ['Binance', 'Uniswap', 'PancakeSwap', 'Coinbase'],
            'option': ['Robinhood', 'Webull', 'TD Ameritrade', 'Interactive Brokers', 'E*TRADE'],
            'futures': ['Interactive Brokers', 'TD Ameritrade', 'E*TRADE', 'TradeStation'],
            'forex': ['Interactive Brokers', 'eToro', 'OANDA', 'Forex.com'],
            'crypto_multi': ['Kraken', 'Binance', 'Coinbase', 'eToro']
        }
        
        broker = random.choice(brokers.get(asset_type, brokers['stock']))
        
        return {
            'symbol': symbol,
            'asset_type': asset_type,
            'broker': broker,
            'direction': direction,
            'entry_price': entry_price,
            'exit_price': exit_price,
            'quantity': quantity,
            'deposit': deposit,
            'profit': profit_amount,
            'roi': roi,
            'current_price': current_price
        }

price_sim = PriceSimulator()
