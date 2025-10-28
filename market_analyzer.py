"""
Market Analyzer - Generate trades based on real market conditions
Analyzes market trends and generates contextual trading signals
"""

import random
import logging
from datetime import datetime, timedelta
import yfinance as yf

logger = logging.getLogger(__name__)

class MarketAnalyzer:
    def __init__(self):
        self.market_conditions = {
            'SPY': None,
            'QQQ': None,
            'BTC': None,
            'last_update': None
        }
    
    def get_market_sentiment(self):
        """Analyze overall market sentiment based on major indices"""
        try:
            # Check if we need to update (cache for 15 minutes)
            if self.market_conditions['last_update']:
                age = datetime.now() - self.market_conditions['last_update']
                if age < timedelta(minutes=15):
                    return self._get_cached_sentiment()
            
            # Fetch SPY (S&P 500) data
            spy = yf.Ticker("SPY")
            spy_hist = spy.history(period="5d")
            
            if not spy_hist.empty:
                spy_change = ((spy_hist['Close'].iloc[-1] - spy_hist['Close'].iloc[0]) / spy_hist['Close'].iloc[0]) * 100
                self.market_conditions['SPY'] = spy_change
                logger.info(f"Market sentiment: SPY {spy_change:+.2f}% over 5 days")
            
            self.market_conditions['last_update'] = datetime.now()
            return self._get_cached_sentiment()
            
        except Exception as e:
            logger.warning(f"Failed to get market sentiment: {e}")
            return "NEUTRAL"
    
    def _get_cached_sentiment(self):
        """Determine sentiment from cached data"""
        spy_change = self.market_conditions.get('SPY', 0)
        
        if spy_change is None or spy_change == 0:
            return "NEUTRAL"
        elif spy_change > 2:
            return "VERY_BULLISH"
        elif spy_change > 0.5:
            return "BULLISH"
        elif spy_change < -2:
            return "VERY_BEARISH"
        elif spy_change < -0.5:
            return "BEARISH"
        else:
            return "NEUTRAL"
    
    def get_market_tags(self):
        """Get market-related tags based on current conditions"""
        sentiment = self.get_market_sentiment()
        
        tags = []
        
        # Sentiment-based tags
        if sentiment == "VERY_BULLISH":
            tags.extend(["🚀 Market Rip", "Bulls Running", "ATH Watch", "Momentum Play"])
        elif sentiment == "BULLISH":
            tags.extend(["📈 Trending Up", "Bullish Setup", "Green Day", "Following Market"])
        elif sentiment == "VERY_BEARISH":
            tags.extend(["📉 Market Dump", "Bears Active", "Correction Play", "Short Setup"])
        elif sentiment == "BEARISH":
            tags.extend(["⚠️ Pullback", "Cautious Entry", "Dip Buy", "Counter-trend"])
        else:
            tags.extend(["⚖️ Sideways", "Range Trade", "Neutral Market", "Scalp Setup"])
        
        # Time-based tags
        hour = datetime.now().hour
        if 9 <= hour < 10:
            tags.append("🔔 Market Open")
        elif 15 <= hour < 16:
            tags.append("⏰ Power Hour")
        elif hour < 9 or hour >= 16:
            tags.append("🌙 After Hours")
        
        # Random event tags (simulate market news)
        events = [
            "Earnings Beat", "Fed Day", "CPI Release", "Tech Sector Lead",
            "Energy Rally", "Volatility Spike", "High Volume", "Breakout Alert",
            "Support Hold", "Resistance Break", "Gap Fill", "Reversal Pattern",
            "Institution Buy", "Whale Activity", "Smart Money", "Retail Fomo"
        ]
        
        if random.random() < 0.3:  # 30% chance of event tag
            tags.append(f"⚡ {random.choice(events)}")
        
        return tags[:3]  # Return top 3 tags
    
    def get_win_streak_tag(self, last_n_trades=None):
        """Generate win streak tags"""
        streak_tags = [
            "🔥 3-Trade Win Streak",
            "💪 5 Wins in a Row",
            "🏆 Hot Streak Active",
            "⭐ Perfect Day",
            "💎 Diamond Hands",
            "🎯 Precision Entry",
            "🧠 Smart Setup",
            "📊 Technical Win"
        ]
        
        # Randomly assign win streak tags (70% of trades get a tag)
        if random.random() < 0.7:
            return random.choice(streak_tags)
        return None
    
    def generate_market_reasoning(self, symbol, direction, sentiment=None):
        """Generate context-aware trade reasoning based on market conditions"""
        if sentiment is None:
            sentiment = self.get_market_sentiment()
        
        bullish_reasons = [
            f"{symbol} breaking above key resistance with strong market momentum",
            f"Institutional accumulation detected in {symbol} during market uptrend",
            f"{symbol} following broader market rally with increased volume",
            f"Technical breakout in {symbol} aligning with bullish market sentiment",
            f"{symbol} showing relative strength vs market - leadership play",
            f"Strong support hold at key level in {symbol} during market pullback recovery",
            f"{symbol} momentum trade following S&P 500 uptrend confirmation"
        ]
        
        bearish_reasons = [
            f"{symbol} showing weakness below support during market correction",
            f"Market downturn providing short opportunity in {symbol}",
            f"{symbol} technical breakdown aligning with broader market weakness",
            f"Profit-taking signal in {symbol} as market shows exhaustion",
            f"{symbol} failing to hold key level despite market attempts to recover"
        ]
        
        neutral_reasons = [
            f"{symbol} range-bound trade in sideways market conditions",
            f"Scalping opportunity in {symbol} during low-volatility session",
            f"{symbol} mean reversion play in choppy market",
            f"Quick profit on {symbol} intraday momentum independent of market"
        ]
        
        if direction == "BUY":
            if sentiment in ["VERY_BULLISH", "BULLISH"]:
                return random.choice(bullish_reasons)
            elif sentiment in ["VERY_BEARISH", "BEARISH"]:
                return random.choice(neutral_reasons)  # Counter-trend buy
            else:
                return random.choice(bullish_reasons + neutral_reasons)
        else:  # SELL/SHORT
            if sentiment in ["VERY_BEARISH", "BEARISH"]:
                return random.choice(bearish_reasons)
            else:
                return random.choice(neutral_reasons + bearish_reasons)

market_analyzer = MarketAnalyzer()
