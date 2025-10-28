import random
from datetime import datetime, timedelta

# Bullish analysis templates
BULLISH_ANALYSES = [
    "📈 {symbol} showing strong accumulation above ${price} support level",
    "🚀 {symbol} breaking out of {timeframe} consolidation pattern with volume",
    "💹 Institutional buying detected in {symbol} - large block orders at ${price}",
    "📊 {symbol} Golden Cross forming - 50MA crossing above 200MA",
    "🎯 {symbol} reclaiming key resistance at ${price}, next target ${target:.2f}",
    "⚡ {symbol} momentum accelerating - RSI trending higher",
    "🔥 {symbol} volume surge +{volume}% - institutions accumulating",
    "💰 {symbol} earnings beat expectations by {percent}% - upgrade cycle beginning",
    "🌟 {symbol} forming cup and handle pattern - bullish breakout imminent",
    "📈 {symbol} higher lows forming - uptrend intact",
    "🎊 {symbol} breaking above {timeframe} resistance with conviction",
    "💎 {symbol} holding gains better than sector - relative strength",
    "🚀 {symbol} short squeeze potential - {percent}% short interest",
    "📊 {symbol} bullish divergence on RSI - upside reversal likely",
    "⚡ {symbol} whale wallets accumulating - on-chain data bullish",
    "🔥 {symbol} news catalyst: {news_type} - expect upside",
    "💹 {symbol} breaking multi-week resistance at ${price}",
    "🎯 {symbol} institutional upgrades to 'Strong Buy' - target ${target:.2f}",
    "📈 {symbol} forming ascending triangle - breakout zone ${price}",
    "🌊 {symbol} riding wave of sector rotation into {sector}",
]

BEARISH_ANALYSES = [
    "📉 {symbol} showing distribution at ${price} resistance level",
    "⚠️ {symbol} breaking down from {timeframe} support with volume",
    "🔴 Institutional selling detected in {symbol} - large exit orders",
    "📊 {symbol} Death Cross forming - 50MA crossing below 200MA",
    "🎯 {symbol} losing key support at ${price}, next target ${target:.2f}",
    "⚡ {symbol} momentum deteriorating - RSI trending lower",
    "🔥 {symbol} volume surge on selling - institutions distributing",
    "💰 {symbol} earnings miss expectations by {percent}% - downgrade cycle beginning",
    "🌟 {symbol} forming head and shoulders - bearish breakdown imminent",
    "📉 {symbol} lower highs forming - downtrend confirmed",
    "⚠️ {symbol} breaking below {timeframe} support with conviction",
    "💎 {symbol} underperforming sector - relative weakness",
    "🔴 {symbol} high short interest growing - bearish sentiment",
    "📊 {symbol} bearish divergence on RSI - downside reversal likely",
    "⚡ {symbol} whale wallets dumping - on-chain data bearish",
    "🔥 {symbol} negative news: {news_type} - expect downside",
    "📉 {symbol} breaking multi-week support at ${price}",
    "🎯 {symbol} institutional downgrades to 'Sell' - target ${target:.2f}",
    "📉 {symbol} forming descending triangle - breakdown zone ${price}",
    "🌊 {symbol} hurt by sector rotation out of {sector}",
]

NEUTRAL_ANALYSES = [
    "⚖️ {symbol} consolidating in range ${low}-${high}",
    "📊 {symbol} awaiting catalyst - technical setup forming",
    "💡 {symbol} at decision point - watch ${price} level closely",
    "🎯 {symbol} coiling in {timeframe} triangle pattern",
    "⏰ {symbol} in accumulation phase - patience required",
    "📈 {symbol} choppy price action - avoid for now",
    "🔍 {symbol} building base at ${price} support",
    "💰 {symbol} sideways movement - wait for breakout confirmation",
    "⚡ {symbol} low volume consolidation - big move coming",
    "📊 {symbol} testing key level ${price} - direction unclear",
]

# Sector analysis (static, no placeholders)
SECTOR_ANALYSES = [
    "🏦 Financial sector showing strength - bank stocks rallying",
    "💻 Technology leading markets higher - FAANG outperforming",
    "⚡ Energy sector surging on crude oil breakout",
    "🏥 Healthcare defensive strength - rotation from growth",
    "🏭 Industrials breaking out - economic recovery play",
    "🛒 Consumer discretionary weak - recession fears mounting",
    "🥫 Consumer staples bid - flight to safety",
    "📱 Semiconductors leading tech higher - chip shortage easing",
    "✈️ Travel sector recovering - pandemic pressures fading",
    "🏠 Real estate under pressure - rising rates headwind",
    "⚗️ Biotech volatility - FDA approval catalysts ahead",
    "🌐 Cloud computing stocks consolidating - growth premium fading",
    "🚗 EV sector momentum - regulatory tailwinds building",
    "💰 Fintech disruption continuing - traditional banks lagging",
    "🎮 Gaming sector strong - esports growth accelerating",
]

# Crypto-specific analyses
CRYPTO_ANALYSES = [
    "₿ Bitcoin dominance {direction} - {interpretation}",
    "🌐 Ethereum gas fees {status} - network activity {trend}",
    "⚡ Layer 2 solutions gaining traction - scaling narrative strong",
    "💎 DeFi TVL {direction} - {interpretation}",
    "🎨 NFT volume {trend} - digital collectibles {sentiment}",
    "🏦 Institutional crypto adoption accelerating - BTC ETF flows strong",
    "⛓️ On-chain metrics {status} - {interpretation}",
    "🐋 Whale activity {trend} - large holders {action}",
    "📊 Crypto market cap {direction} - total value {trend}",
    "🔥 Stablecoin supply {trend} - dry powder {interpretation}",
    "💹 Altcoin season index: {level} - {interpretation}",
    "🌊 Funding rates {status} - {interpretation}",
    "📈 Miner outflows {trend} - selling pressure {status}",
    "🎯 Exchange reserves {direction} - {interpretation}",
    "⚡ Lightning Network capacity {trend} - BTC payments growing",
]

# Forex analyses
FOREX_ANALYSES = [
    "💱 USD strengthening on Fed hawkish stance - DXY targeting {level:.2f}",
    "🌍 EUR under pressure - ECB dovish guidance weighing",
    "🇬🇧 GBP volatility on BoE decision - rate path uncertain",
    "🇯🇵 JPY safe-haven bid - risk-off flows intensifying",
    "🇦🇺 AUD commodity correlation strong - following copper prices",
    "🇨🇦 CAD oil correlation intact - crude prices driving",
    "🇨🇭 CHF defensive strength - geopolitical tensions rising",
    "🇳🇿 NZD rate differential supporting - carry trade appeal",
    "💹 Carry trades unwinding - volatility spike risk",
    "📊 Currency correlations shifting - diversification important",
    "🌐 Emerging market FX under pressure - dollar strength",
    "⚡ Forex volatility increasing - central bank divergence",
    "🎯 EUR/USD at key support {level:.4f} - make or break",
    "💰 GBP/USD testing resistance {level:.4f} - Brexit clarity needed",
    "📈 USD/JPY range-bound {low:.2f}-{high:.2f} - awaiting catalyst",
]

# Commodities analyses
COMMODITIES_ANALYSES = [
    "🥇 Gold testing resistance at ${level} - inflation hedge bid",
    "🥈 Silver industrial demand strong - solar panel growth",
    "🛢️ Crude oil supply concerns - OPEC+ cuts supporting",
    "⚡ Natural gas seasonal demand - winter premium building",
    "🔶 Copper China demand - economic recovery play",
    "🌾 Wheat supply disruption - weather concerns mounting",
    "☕ Coffee prices rallying - Brazil frost damage",
    "🌽 Corn ethanol demand strong - biofuel mandates",
    "🥩 Cattle prices elevated - tight supply conditions",
    "💰 Precious metals correlation weakening - diverging drivers",
    "📊 Commodity index breakout - inflation pressures building",
    "🌍 Base metals strong - infrastructure spending theme",
    "⛽ Energy complex volatile - geopolitical premium",
    "🥔 Agricultural commodities seasonal patterns - planting season",
    "💎 Industrial metals bottoming - manufacturing recovery",
]

# News-driven analyses
NEWS_ANALYSES = [
    "📰 Breaking: {symbol} announces {news_event}",
    "🗞️ {symbol} regulatory development: {news_details}",
    "📢 {symbol} partnership announced with {partner}",
    "🎤 {symbol} CEO interview: {quote}",
    "🏢 {symbol} restructuring: {details}",
    "💼 {symbol} acquisition rumors: {target}",
    "📊 {symbol} analyst day: {highlights}",
    "🔬 {symbol} product launch: {product}",
    "⚖️ {symbol} legal development: {case_details}",
    "🌍 {symbol} international expansion: {region}",
]

# Generate comprehensive analyses
def generate_symbol_analysis(symbol, price, direction="bullish"):
    """Generate detailed analysis for specific symbol"""
    templates = BULLISH_ANALYSES if direction == "bullish" else BEARISH_ANALYSES
    
    analysis = random.choice(templates).format(
        symbol=symbol,
        price=price,
        target=price * random.uniform(1.1, 1.3) if direction == "bullish" else price * random.uniform(0.7, 0.9),
        timeframe=random.choice(["daily", "weekly", "4-hour", "hourly"]),
        volume=random.randint(50, 300),
        percent=random.randint(5, 30),
        news_type=random.choice(["partnership", "earnings beat", "product launch", "upgrade", "buyback announced"]),
        sector=random.choice(["tech", "finance", "energy", "healthcare"])
    )
    
    return analysis

def generate_multi_point_analysis(symbol):
    """Generate comprehensive multi-point analysis"""
    analyses = []
    
    analyses.append(f"📊 {symbol} ANALYSIS:")
    analyses.append(f"🎯 Technical: {random.choice(['Bullish setup forming', 'Bearish pressure building', 'Neutral consolidation'])}")
    analyses.append(f"💰 Fundamental: {random.choice(['Strong earnings growth', 'Revenue pressures', 'Margin expansion'])}")
    analyses.append(f"📈 Sentiment: {random.choice(['Bullish positioning', 'Bearish sentiment', 'Mixed signals'])}")
    analyses.append(f"🔍 Recommendation: {random.choice(['BUY', 'SELL', 'HOLD'])} - Target ${random.randint(100, 500)}")
    
    return "\n".join(analyses)

# --- CORRECTED CODE STARTS HERE ---

# Lists to hold generated analyses for themed retrieval
GENERATED_STOCKS = []
GENERATED_CRYPTO = []
GENERATED_FOREX = []
GENERATED_COMMODITIES = []
GENERATED_SECTORS = SECTOR_ANALYSES  # This list is static, no generation needed
GENERATED_NEWS = []
GENERATED_NEUTRAL = []
GENERATED_PATTERNS = []
GENERATED_INDICATORS = []
GENERATED_ECONOMIC = []


# Master list to hold ALL generated analyses
ALL_ANALYSES = []

# Add static sectors
ALL_ANALYSES.extend(GENERATED_SECTORS)

# Generate Crypto Analyses
for template in CRYPTO_ANALYSES:
    analysis = template.format(
        direction=random.choice(["rising", "falling", "flat"]),
        interpretation=random.choice(["bullish signal", "bearish signal", "neutral indicator"]),
        status=random.choice(["high", "low", "normal"]),
        trend=random.choice(["increasing", "decreasing", "sideways"]),
        sentiment=random.choice(["positive", "negative", "mixed"]),
        action=random.choice(["accumulating", "distributing", "holding"]),
        level=f"{random.randint(40, 60)}%",
    )
    GENERATED_CRYPTO.append(analysis)
ALL_ANALYSES.extend(GENERATED_CRYPTO)

# Generate Forex Analyses
for template in FOREX_ANALYSES:
    analysis = template.format(
        level=random.uniform(1.05, 1.25),
        low=random.uniform(1.0, 1.1),
        high=random.uniform(1.15, 1.25),
    )
    GENERATED_FOREX.append(analysis)
ALL_ANALYSES.extend(GENERATED_FOREX)

# Generate Commodities Analyses
for template in COMMODITIES_ANALYSES:
    analysis = template.format(
        level=random.randint(1800, 2200)
    )
    GENERATED_COMMODITIES.append(analysis)
ALL_ANALYSES.extend(GENERATED_COMMODITIES)

# Generate News Analyses
for template in NEWS_ANALYSES:
    analysis = template.format(
        symbol=random.choice(["AAPL", "TSLA", "GOOG"]),
        news_event=random.choice(["new product launch", "stock split", "earnings surprise"]),
        news_details=random.choice(["positive regulatory ruling", "SEC probe", "new EU data law"]),
        partner=random.choice(["Microsoft", "NVIDIA", "OpenAI"]),
        quote=random.choice(["'We are very optimistic'", "'Headwinds remain'", "'Future is bright'"]),
        details=random.choice(["spinning off cloud division", "new cost-cutting measures"]),
        target=random.choice(["a smaller rival", "a startup in AI"]),
        highlights=random.choice(["raised guidance", "new AI strategy"]),
        product=random.choice(["new M3 chip", "next-gen EV", "AR headset"]),
        case_details=random.choice(["patent lawsuit settled", "antitrust case appeal"]),
        region=random.choice(["Asia", "Europe", "Latin America"]),
    )
    GENERATED_NEWS.append(analysis)
ALL_ANALYSES.extend(GENERATED_NEWS)

# Generate symbol-specific stock analyses
symbols = ["SPY", "QQQ", "BTC", "ETH", "AAPL", "TSLA", "NVDA", "MSFT", "AMZN", "GOOGL", 
           "EUR/USD", "GBP/USD", "USD/JPY", "GOLD", "OIL", "SOL", "ADA", "DOGE"]

for symbol in symbols:
    for _ in range(5):
        analysis = generate_symbol_analysis(symbol, random.randint(50, 500), random.choice(["bullish", "bearish"]))
        GENERATED_STOCKS.append(analysis)
ALL_ANALYSES.extend(GENERATED_STOCKS)

# Generate Neutral Analyses
for symbol in symbols:
    for template in NEUTRAL_ANALYSES:
        analysis = template.format(
            symbol=symbol,
            low=random.randint(100, 150),
            high=random.randint(160, 200),
            price=random.randint(151, 159),
            timeframe=random.choice(["daily", "weekly"]),
        )
        GENERATED_NEUTRAL.append(analysis)
ALL_ANALYSES.extend(GENERATED_NEUTRAL)


# Technical pattern analyses
patterns = [
    "head and shoulders", "cup and handle", "double bottom", "double top",
    "ascending triangle", "descending triangle", "bull flag", "bear flag",
    "inverse head and shoulders", "symmetrical triangle", "wedge", "pennant"
]

for pattern in patterns:
    analysis1 = f"📐 {pattern.title()} pattern forming - {random.choice(['bullish', 'bearish'])} implications"
    analysis2 = f"🎯 {pattern.title()} breakout target: {random.choice(['$150', '$200', '$250', '$300'])}"
    GENERATED_PATTERNS.extend([analysis1, analysis2])
ALL_ANALYSES.extend(GENERATED_PATTERNS)

# Indicator-based analyses
indicators = ["RSI", "MACD", "Stochastic", "Bollinger Bands", "Moving Averages", "Volume"]
for indicator in indicators:
    for sentiment in ["bullish", "bearish", "neutral"]:
        analysis = f"📊 {indicator} showing {sentiment} signals across multiple timeframes"
        GENERATED_INDICATORS.append(analysis)
ALL_ANALYSES.extend(GENERATED_INDICATORS)

# Add economic calendar analyses
economic_events = [
    "Fed Interest Rate Decision", "NFP Jobs Report", "CPI Inflation Data",
    "GDP Growth", "Retail Sales", "PMI Manufacturing", "Consumer Confidence",
    "Earnings Season", "FOMC Minutes", "ECB Rate Decision"
]

for event in economic_events:
    analysis1 = f"📅 Upcoming {event} - expect volatility in {random.choice(['equities', 'forex', 'commodities'])}"
    analysis2 = f"⏰ {event} ahead - positioning {random.choice(['defensive', 'aggressive', 'neutral'])}"
    GENERATED_ECONOMIC.extend([analysis1, analysis2])
ALL_ANALYSES.extend(GENERATED_ECONOMIC)

# --- FUNCTIONS ---

def get_random_analysis():
    """Get random market analysis"""
    return random.choice(ALL_ANALYSES)

def get_themed_analysis(theme="crypto"):
    """Get analysis for specific theme"""
    # This now correctly points to the lists of GENERATED analyses
    themed_analyses = {
        "crypto": GENERATED_CRYPTO,
        "forex": GENERATED_FOREX,
        "stocks": GENERATED_STOCKS,
        "commodities": GENERATED_COMMODITIES,
        "sector": GENERATED_SECTORS,
        "news": GENERATED_NEWS,
        "neutral": GENERATED_NEUTRAL,
    }
    # Fallback to ALL_ANALYSES if theme not found
    return random.choice(themed_analyses.get(theme, ALL_ANALYSES))

__all__ = ['ALL_ANALYSES', 'get_random_analysis', 'get_themed_analysis', 'generate_symbol_analysis']

print(f"✅ Loaded {len(ALL_ANALYSES)} market analyses")
