"""
Ultra-Authentic Mobile Trading App Screenshot Generator
Creates highly realistic mobile trading app screenshots with:
- iOS/Android status bars
- Social proof elements
- Technical indicators (RSI, MACD, Bollinger Bands, Fibonacci)
- Risk management displays
- Portfolio context
- Market sentiment and news
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.ticker import FuncFormatter
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import io
import random
from datetime import datetime, timedelta
import os

BROKER_THEMES = {
    "robinhood": {
        "bg": "#0B0F19",
        "card_bg": "#1C1F26",
        "primary": "#00C805",
        "accent": "#FF8A00",
        "text": "#FFFFFF",
        "text_secondary": "#8B92A6",
        "profit": "#00C805",
        "loss": "#FF6058"
    },
    "webull": {
        "bg": "#0A0E27",
        "card_bg": "#151932",
        "primary": "#4C9AFF",
        "accent": "#FFB84D",
        "text": "#FFFFFF",
        "text_secondary": "#7A84A2",
        "profit": "#4ADE80",
        "loss": "#F87171"
    },
    "binance": {
        "bg": "#0B0E11",
        "card_bg": "#1E2329",
        "primary": "#F0B90B",
        "accent": "#F3BA2F",
        "text": "#EAECEF",
        "text_secondary": "#848E9C",
        "profit": "#0ECB81",
        "loss": "#F6465D"
    },
    "coinbase": {
        "bg": "#0A0B0D",
        "card_bg": "#17181B",
        "primary": "#0052FF",
        "accent": "#1652F0",
        "text": "#FFFFFF",
        "text_secondary": "#8A919E",
        "profit": "#05B169",
        "loss": "#DF5F67"
    },
    "etrade": {
        "bg": "#1A1D28",
        "card_bg": "#252932",
        "primary": "#7C3AED",
        "accent": "#A78BFA",
        "text": "#FFFFFF",
        "text_secondary": "#9CA3AF",
        "profit": "#10B981",
        "loss": "#EF4444"
    },
    "td_ameritrade": {
        "bg": "#0D1B2A",
        "card_bg": "#1B263B",
        "primary": "#43B02A",
        "accent": "#5CDB3A",
        "text": "#FFFFFF",
        "text_secondary": "#9DB4C6",
        "profit": "#43B02A",
        "loss": "#DC2626"
    },
    "interactive_brokers": {
        "bg": "#0F1419",
        "card_bg": "#1A2028",
        "primary": "#0095FF",
        "accent": "#00C3FF",
        "text": "#FFFFFF",
        "text_secondary": "#7A8896",
        "profit": "#00A86B",
        "loss": "#DC143C"
    },
    "kraken": {
        "bg": "#0A0D14",
        "card_bg": "#151822",
        "primary": "#5741D9",
        "accent": "#7B68EE",
        "text": "#F8F8FF",
        "text_secondary": "#8E92A5",
        "profit": "#26A69A",
        "loss": "#F44336"
    },
    "etoro": {
        "bg": "#1B2126",
        "card_bg": "#2A2F36",
        "primary": "#39D0B0",
        "accent": "#5FEDD3",
        "text": "#FFFFFF",
        "text_secondary": "#A8ADB5",
        "profit": "#39D0B0",
        "loss": "#FF5B5B"
    }
}

def get_theme_for_broker(broker_name):
    broker_lower = broker_name.lower().replace(" ", "_").replace("*", "")
    if "robinhood" in broker_lower:
        return BROKER_THEMES["robinhood"]
    elif "webull" in broker_lower:
        return BROKER_THEMES["webull"]
    elif "binance" in broker_lower:
        return BROKER_THEMES["binance"]
    elif "coinbase" in broker_lower:
        return BROKER_THEMES["coinbase"]
    elif "etrade" in broker_lower or "e*trade" in broker_lower or "e_trade" in broker_lower:
        return BROKER_THEMES["etrade"]
    elif "td" in broker_lower and "ameritrade" in broker_lower:
        return BROKER_THEMES["td_ameritrade"]
    elif "interactive" in broker_lower and "broker" in broker_lower:
        return BROKER_THEMES["interactive_brokers"]
    elif "kraken" in broker_lower:
        return BROKER_THEMES["kraken"]
    elif "etoro" in broker_lower:
        return BROKER_THEMES["etoro"]
    else:
        return BROKER_THEMES["robinhood"]

def draw_mobile_status_bar(draw, width, device_type="ios", theme=None):
    """Draw realistic mobile status bar with time, signal, battery"""
    if theme is None:
        theme = BROKER_THEMES["robinhood"]
    
    status_height = 50
    
    try:
        status_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        status_font = ImageFont.load_default()
    
    current_time = datetime.now().strftime("%I:%M")
    
    if device_type == "ios":
        draw.text((20, 15), current_time, fill=theme["text"], font=status_font)
        draw.text((width - 120, 15), "5G", fill=theme["text"], font=status_font)
        draw.text((width - 90, 15), "▮▮▮▮", fill=theme["text"], font=status_font)
        
        battery_x = width - 50
        battery_y = 12
        draw.rounded_rectangle((battery_x, battery_y, battery_x + 35, battery_y + 20), 
                              radius=3, outline=theme["text"], width=2)
        draw.rectangle((battery_x + 36, battery_y + 6, battery_x + 39, battery_y + 14), 
                      fill=theme["text"])
        draw.rectangle((battery_x + 3, battery_y + 3, battery_x + 30, battery_y + 17), 
                      fill=theme["profit"])
    else:
        draw.text((20, 15), current_time, fill=theme["text"], font=status_font)
        draw.text((width - 140, 15), "5G", fill=theme["text"], font=status_font)
        draw.text((width - 110, 15), "▮▮▮▮", fill=theme["text"], font=status_font)
        draw.text((width - 70, 15), "95%", fill=theme["text"], font=status_font)
        draw.text((width - 35, 15), "🔋", fill=theme["text"], font=status_font)
    
    return status_height

def draw_bottom_nav_bar(draw, width, height, theme):
    """Draw bottom navigation bar like mobile apps"""
    nav_height = 80
    nav_y = height - nav_height
    
    draw.rectangle((0, nav_y, width, height), fill=theme["card_bg"])
    
    try:
        nav_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        nav_font = ImageFont.load_default()
    
    nav_items = ["🏠", "📊", "💼", "⚙️"]
    nav_labels = ["Home", "Trade", "Portfolio", "Settings"]
    
    section_width = width // len(nav_items)
    
    for i, (icon, label) in enumerate(zip(nav_items, nav_labels)):
        x_pos = i * section_width + section_width // 2
        draw.text((x_pos - 10, nav_y + 15), icon, fill=theme["text"], font=nav_font)
        draw.text((x_pos - 15, nav_y + 45), label, fill=theme["text_secondary"], font=nav_font)
    
    return nav_height

def generate_social_proof_data():
    """Generate random social proof metrics"""
    watching = random.randint(5000, 50000)
    trending_rank = random.randint(1, 10)
    followers = random.randint(50, 500)
    win_streak = random.randint(3, 15)
    
    return {
        "watching": f"{watching//1000}k watching",
        "trending": f"#️⃣ Trending #{trending_rank} in Crypto",
        "followers": f"👥 {followers} traders following",
        "streak": f"🔥 {win_streak} wins in a row"
    }

def generate_market_sentiment():
    """Generate market sentiment data"""
    sentiment_value = random.randint(40, 90)
    sentiment = "Bullish" if sentiment_value > 60 else "Bearish" if sentiment_value < 45 else "Neutral"
    
    volatility_levels = ["Low", "Medium", "High", "Extreme"]
    volatility = random.choice(volatility_levels)
    
    news_items = [
        "Fed announces rate decision",
        "Earnings report today",
        "Market hits new highs",
        "Economic data released",
        "Tech sector rallies",
        "Crypto regulation news"
    ]
    
    events = ["📊 Earnings Today", "💵 Ex-Dividend", "📈 New ATH", "🔔 News Alert"]
    
    return {
        "sentiment": sentiment,
        "sentiment_value": sentiment_value,
        "volatility": volatility,
        "news": random.choice(news_items),
        "event": random.choice(events) if random.random() > 0.5 else None
    }

def generate_leaderboard_data():
    """Generate leaderboard/ranking data"""
    rank_percentile = random.randint(1, 20)
    win_rate = random.randint(70, 95)
    profit_streak_days = random.randint(5, 30)
    
    return {
        "rank": f"🏆 Top {rank_percentile}% this month",
        "win_rate": f"✅ Win rate: {win_rate}% (Last 30 days)",
        "profit_streak": f"📈 {profit_streak_days}-day profit streak"
    }

def draw_interactive_buttons(draw, width, y_pos, theme, font_small):
    """Draw Share and Copy Trade buttons with social stats"""
    button_width = (width - 120) // 2
    button_height = 55
    
    draw.rounded_rectangle((40, y_pos, 40 + button_width, y_pos + button_height), 
                          radius=12, fill=theme["primary"] + "40", outline=theme["primary"], width=2)
    draw.text((40 + button_width//2 - 30, y_pos + 18), "📤 Share", fill=theme["primary"], font=font_small)
    
    copy_x = 40 + button_width + 40
    draw.rounded_rectangle((copy_x, y_pos, copy_x + button_width, y_pos + button_height), 
                          radius=12, fill=theme["accent"] + "40", outline=theme["accent"], width=2)
    draw.text((copy_x + button_width//2 - 60, y_pos + 18), "📋 Copy Trade", fill=theme["accent"], font=font_small)
    
    likes = random.randint(100, 5000)
    comments = random.randint(10, 500)
    social_y = y_pos + button_height + 15
    draw.text((40, social_y), f"❤️ {likes} likes  💬 {comments} comments", 
              fill=theme["text_secondary"], font=font_small)
    
    copy_count = random.randint(5, 200)
    draw.text((40, social_y + 30), f"👥 {copy_count} followers copied this trade", 
              fill=theme["profit"], font=font_small)
    
    return social_y + 60

def generate_qr_code_placeholder(draw, x, y, size, theme):
    """Draw a simple QR code placeholder"""
    draw.rounded_rectangle((x, y, x + size, y + size), radius=5, fill="#FFFFFF", outline=theme["text_secondary"], width=2)
    cell_size = size // 10
    for i in range(2, 8):
        for j in range(2, 8):
            if random.random() > 0.5:
                draw.rectangle((x + i * cell_size, y + j * cell_size, 
                              x + (i+1) * cell_size, y + (j+1) * cell_size), fill="#000000")

def draw_verification_layer(draw, width, y_pos, symbol, txid, theme, font_small, font_tiny):
    """Draw verification elements: QR code, blockchain hash, SEC disclaimer"""
    draw.rounded_rectangle((40, y_pos, width - 40, y_pos + 180), radius=15, fill=theme["card_bg"])
    
    draw.text((60, y_pos + 15), "🔐 Trade Verification", fill=theme["primary"], font=font_small)
    
    qr_size = 80
    qr_x = width - 40 - qr_size - 20
    generate_qr_code_placeholder(draw, qr_x, y_pos + 50, qr_size, theme)
    draw.text((qr_x + 10, y_pos + qr_size + 55), "Scan to verify", fill=theme["text_secondary"], font=font_tiny)
    
    if "BTC" in symbol or "ETH" in symbol or any(crypto in symbol for crypto in ["DOGE", "SOL", "ADA", "NIKY"]):
        blockchain_hash = f"0x{''.join(random.choices('0123456789abcdef', k=40))}"
        draw.text((60, y_pos + 50), "Blockchain Hash:", fill=theme["text_secondary"], font=font_tiny)
        draw.text((60, y_pos + 70), blockchain_hash[:20] + "...", fill=theme["accent"], font=font_tiny)
    
    draw.text((60, y_pos + 100), "✅ Audited by PricewaterhouseCoopers", fill=theme["profit"], font=font_tiny)
    
    draw.text((60, y_pos + 135), "SEC Disclaimer: Trading involves risk. Past performance does not", 
              fill=theme["text_secondary"], font=font_tiny)
    draw.text((60, y_pos + 152), "guarantee future results. Not financial advice.", 
              fill=theme["text_secondary"], font=font_tiny)
    
    return y_pos + 200

def generate_options_greeks():
    """Generate realistic options Greeks"""
    return {
        "delta": round(random.uniform(0.3, 0.9), 3),
        "gamma": round(random.uniform(0.001, 0.05), 4),
        "theta": round(random.uniform(-0.5, -0.05), 3),
        "vega": round(random.uniform(0.05, 0.3), 3),
        "iv": round(random.uniform(20, 80), 1),
        "strike": None,
        "expiry": None
    }

def draw_asset_type_specific_info(draw, y_pos, width, asset_type, symbol, theme, font_small, font_tiny):
    """Draw asset-specific information (Options Greeks, Futures specs, Forex pips)"""
    draw.rounded_rectangle((40, y_pos, width - 40, y_pos + 140), radius=15, fill=theme["card_bg"])
    
    if asset_type == "option":
        greeks = generate_options_greeks()
        strike = random.randint(100, 500)
        expiry = (datetime.now() + timedelta(days=random.randint(7, 90))).strftime("%b %d, %Y")
        
        draw.text((60, y_pos + 15), f"📊 Options Contract: {symbol} ${strike} Call", 
                  fill=theme["primary"], font=font_small)
        draw.text((60, y_pos + 45), f"Expiry: {expiry}", fill=theme["text_secondary"], font=font_tiny)
        draw.text((60, y_pos + 70), f"Delta: {greeks['delta']}  Gamma: {greeks['gamma']}", 
                  fill=theme["text"], font=font_tiny)
        draw.text((60, y_pos + 90), f"Theta: {greeks['theta']}  Vega: {greeks['vega']}", 
                  fill=theme["text"], font=font_tiny)
        draw.text((60, y_pos + 110), f"IV: {greeks['iv']}%", fill=theme["accent"], font=font_tiny)
        
    elif asset_type == "futures":
        contract_month = (datetime.now() + timedelta(days=random.randint(30, 180))).strftime("%b %Y")
        tick_size = random.choice([0.25, 0.5, 1.0, 5.0])
        
        draw.text((60, y_pos + 15), f"📈 Futures Contract: {symbol} {contract_month}", 
                  fill=theme["primary"], font=font_small)
        draw.text((60, y_pos + 45), f"Contract Size: 1 contract", fill=theme["text_secondary"], font=font_tiny)
        draw.text((60, y_pos + 70), f"Tick Size: ${tick_size}", fill=theme["text"], font=font_tiny)
        draw.text((60, y_pos + 90), f"Margin Required: ${random.randint(2000, 10000):,}", 
                  fill=theme["text"], font=font_tiny)
        
    elif asset_type == "forex":
        pip_value = round(random.uniform(5, 15), 2)
        spread = round(random.uniform(0.5, 3.0), 1)
        
        draw.text((60, y_pos + 15), f"💱 Forex Pair: {symbol}", fill=theme["primary"], font=font_small)
        draw.text((60, y_pos + 45), f"Pip Value: ${pip_value}", fill=theme["text"], font=font_tiny)
        draw.text((60, y_pos + 70), f"Spread: {spread} pips", fill=theme["text_secondary"], font=font_tiny)
        draw.text((60, y_pos + 90), f"Leverage: 1:{random.choice([50, 100, 200])}", 
                  fill=theme["accent"], font=font_tiny)
    
    elif asset_type == "crypto_multi":
        exchanges = ["Binance", "Coinbase Pro", "Kraken", "FTX"]
        selected_exchanges = random.sample(exchanges, 2)
        
        draw.text((60, y_pos + 15), f"₿ Multi-Exchange: {symbol}", fill=theme["primary"], font=font_small)
        draw.text((60, y_pos + 45), f"Exchanges: {', '.join(selected_exchanges)}", 
                  fill=theme["text_secondary"], font=font_tiny)
        draw.text((60, y_pos + 70), "Arbitrage opportunity detected", fill=theme["profit"], font=font_tiny)
    
    return y_pos + 160

def calculate_technical_indicators(entry_price, exit_price, num_candles=40):
    """Calculate RSI, MACD, Bollinger Bands for realistic display"""
    trend = 1 if exit_price > entry_price else -1
    volatility = abs(exit_price - entry_price) / num_candles * 0.5
    
    closes = []
    current_price = entry_price
    
    for i in range(num_candles):
        target_progress = (i + 1) / num_candles
        target_price = entry_price + (exit_price - entry_price) * target_progress
        price_change = (target_price - current_price) * 0.3 + random.uniform(-volatility, volatility)
        close_price = current_price + price_change
        closes.append(close_price)
        current_price = close_price
    
    closes[-1] = exit_price
    
    rsi = 70 + random.randint(-15, 15) if trend > 0 else 30 + random.randint(-15, 15)
    rsi = max(0, min(100, rsi))
    
    macd = (exit_price - entry_price) / entry_price * 100
    signal_line = macd * 0.9
    
    bb_middle = sum(closes[-20:]) / 20
    std = np.std(closes[-20:])
    bb_upper = bb_middle + 2 * std
    bb_lower = bb_middle - 2 * std
    
    support = min(closes) * 0.98
    resistance = max(closes) * 1.02
    
    return {
        "rsi": rsi,
        "macd": macd,
        "signal": signal_line,
        "bb_upper": bb_upper,
        "bb_middle": bb_middle,
        "bb_lower": bb_lower,
        "support": support,
        "resistance": resistance,
        "closes": closes
    }

def create_advanced_chart(symbol, entry_price, exit_price, profit_positive=True, width=800, height=500):
    """Create chart with RSI, MACD, Bollinger Bands, Support/Resistance"""
    fig = plt.figure(figsize=(width/100, height/100), facecolor='#0B0F19')
    
    gs = fig.add_gridspec(3, 1, height_ratios=[3, 1, 1], hspace=0.1)
    ax_price = fig.add_subplot(gs[0])
    ax_rsi = fig.add_subplot(gs[1], sharex=ax_price)
    ax_macd = fig.add_subplot(gs[2], sharex=ax_price)
    
    for ax in [ax_price, ax_rsi, ax_macd]:
        ax.set_facecolor('#1C1F26')
    
    num_candles = 40
    indicators = calculate_technical_indicators(entry_price, exit_price, num_candles)
    
    opens = []
    highs = []
    lows = []
    closes = indicators["closes"]
    volumes = []
    
    current_price = entry_price
    volatility = abs(exit_price - entry_price) / num_candles * 0.5
    
    for i in range(num_candles):
        open_price = closes[i-1] if i > 0 else entry_price
        close_price = closes[i]
        
        high_price = max(open_price, close_price) + random.uniform(0, volatility * 0.5)
        low_price = min(open_price, close_price) - random.uniform(0, volatility * 0.5)
        
        opens.append(open_price)
        highs.append(high_price)
        lows.append(low_price)
        volumes.append(random.uniform(10000, 50000))
    
    for i in range(num_candles):
        candle_color = '#00C805' if closes[i] >= opens[i] else '#FF6058'
        ax_price.plot([i, i], [lows[i], highs[i]], color=candle_color, linewidth=1, alpha=0.8)
        body_height = abs(closes[i] - opens[i])
        body_bottom = min(opens[i], closes[i])
        rect = Rectangle((i - 0.4, body_bottom), 0.8, body_height, 
                         facecolor=candle_color, edgecolor=candle_color, alpha=0.9)
        ax_price.add_patch(rect)
    
    if len(closes) >= 20:
        bb_middle = []
        bb_upper = []
        bb_lower = []
        for i in range(20, len(closes) + 1):
            window = closes[i-20:i]
            mid = sum(window) / 20
            std = np.std(window)
            bb_middle.append(mid)
            bb_upper.append(mid + 2 * std)
            bb_lower.append(mid - 2 * std)
        
        x_bb = range(19, len(closes))
        ax_price.plot(x_bb, bb_upper, color='#FFB84D', linewidth=1, alpha=0.5, linestyle='--')
        ax_price.plot(x_bb, bb_middle, color='#4C9AFF', linewidth=1, alpha=0.6)
        ax_price.plot(x_bb, bb_lower, color='#FFB84D', linewidth=1, alpha=0.5, linestyle='--')
    
    ax_price.axhline(y=indicators["support"], color='#00C805', linestyle=':', linewidth=1.5, alpha=0.7)
    ax_price.text(2, indicators["support"], 'Support', color='#00C805', fontsize=8)
    
    ax_price.axhline(y=indicators["resistance"], color='#FF6058', linestyle=':', linewidth=1.5, alpha=0.7)
    ax_price.text(2, indicators["resistance"], 'Resistance', color='#FF6058', fontsize=8)
    
    fib_levels = [0.236, 0.382, 0.5, 0.618, 0.786]
    for fib in fib_levels:
        fib_price = entry_price + (exit_price - entry_price) * fib
        ax_price.axhline(y=fib_price, color='#8B92A6', linestyle=':', linewidth=0.8, alpha=0.3)
    
    rsi_values = [indicators["rsi"] + random.uniform(-10, 10) for _ in range(num_candles)]
    rsi_values = [max(0, min(100, r)) for r in rsi_values]
    ax_rsi.plot(range(num_candles), rsi_values, color='#F0B90B', linewidth=1.5)
    ax_rsi.axhline(y=70, color='#FF6058', linestyle='--', linewidth=1, alpha=0.5)
    ax_rsi.axhline(y=30, color='#00C805', linestyle='--', linewidth=1, alpha=0.5)
    ax_rsi.fill_between(range(num_candles), 30, 70, alpha=0.1, color='#8B92A6')
    ax_rsi.set_ylim(0, 100)
    ax_rsi.text(1, 85, 'RSI', color='#F0B90B', fontsize=8, weight='bold')
    
    macd_values = [indicators["macd"] * (0.5 + i/num_candles) + random.uniform(-0.5, 0.5) for i in range(num_candles)]
    signal_values = [m * 0.9 for m in macd_values]
    histogram = [m - s for m, s in zip(macd_values, signal_values)]
    
    colors = ['#00C805' if h > 0 else '#FF6058' for h in histogram]
    ax_macd.bar(range(num_candles), histogram, color=colors, alpha=0.7, width=0.8)
    ax_macd.plot(range(num_candles), macd_values, color='#4C9AFF', linewidth=1.5, label='MACD')
    ax_macd.plot(range(num_candles), signal_values, color='#FFB84D', linewidth=1.5, label='Signal')
    ax_macd.axhline(y=0, color='#8B92A6', linestyle='-', linewidth=0.8, alpha=0.5)
    ax_macd.text(1, max(histogram) * 0.8, 'MACD', color='#4C9AFF', fontsize=8, weight='bold')
    
    for ax in [ax_price, ax_rsi, ax_macd]:
        ax.grid(True, alpha=0.08, color='#FFFFFF', linestyle=':', linewidth=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#8B92A6')
        ax.spines['bottom'].set_color('#8B92A6')
        ax.tick_params(colors='#8B92A6', labelsize=7)
        ax.set_xticks([])
    
    ax_price.yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'${x:,.2f}'))
    ax_rsi.set_ylabel('RSI', color='#8B92A6', fontsize=7)
    ax_macd.set_ylabel('MACD', color='#8B92A6', fontsize=7)
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='#0B0F19', dpi=120, bbox_inches='tight')
    buf.seek(0)
    chart_img = Image.open(buf)
    plt.close(fig)
    
    return chart_img

def create_ultra_realistic_mobile_trade_screenshot(
    symbol,
    broker_name,
    trader_name,
    direction,
    entry_price,
    exit_price,
    quantity,
    profit,
    roi,
    deposit,
    txid,
    timestamp=None,
    portfolio_value=None,
    device_type="ios",
    asset_type="stock"
):
    """
    Generate ultra-realistic mobile app screenshot with all enhancements
    """
    theme = get_theme_for_broker(broker_name)
    
    width, height = 1080, 2340
    img = Image.new('RGB', (width, height), theme["bg"])
    draw = ImageDraw.Draw(img)
    
    try:
        font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        font_header = font_title = font_large = font_medium = font_small = font_tiny = ImageFont.load_default()
    
    y_offset = 0
    status_height = draw_mobile_status_bar(draw, width, device_type, theme)
    y_offset += status_height + 10
    
    social_proof = generate_social_proof_data()
    market_data = generate_market_sentiment()
    leaderboard = generate_leaderboard_data()
    
    draw.text((40, y_offset), broker_name, fill=theme["text"], font=font_header)
    y_offset += 50
    
    draw.rounded_rectangle((40, y_offset, width - 40, y_offset + 120), radius=15, fill=theme["card_bg"])
    draw.text((60, y_offset + 20), symbol, fill=theme["primary"], font=font_large)
    direction_color = theme["profit"] if direction == "BUY" else theme["loss"]
    draw.text((60, y_offset + 75), f"{direction} • {quantity:.4f}".rstrip('0').rstrip('.'), 
              fill=direction_color, font=font_medium)
    
    badge_x = width - 250
    draw.rounded_rectangle((badge_x, y_offset + 20, badge_x + 200, y_offset + 50), 
                          radius=12, fill=theme["profit"] + "30")
    draw.text((badge_x + 15, y_offset + 25), social_proof["streak"], fill=theme["profit"], font=font_tiny)
    
    if market_data["event"]:
        draw.rounded_rectangle((badge_x, y_offset + 60, badge_x + 200, y_offset + 90), 
                              radius=12, fill=theme["accent"] + "30")
        draw.text((badge_x + 15, y_offset + 65), market_data["event"], fill=theme["accent"], font=font_tiny)
    
    y_offset += 140
    
    social_y = y_offset
    draw.text((40, social_y), social_proof["watching"], fill=theme["text_secondary"], font=font_small)
    draw.text((40, social_y + 30), social_proof["trending"], fill=theme["accent"], font=font_small)
    draw.text((40, social_y + 60), social_proof["followers"], fill=theme["text_secondary"], font=font_small)
    
    y_offset += 100
    
    chart = create_advanced_chart(symbol, entry_price, exit_price, profit >= 0, 1040, 600)
    chart = chart.resize((width - 80, 600))
    img.paste(chart, (40, y_offset))
    
    y_offset += 630
    
    draw.rounded_rectangle((40, y_offset, width - 40, y_offset + 180), radius=15, fill=theme["card_bg"])
    
    profit_color = theme["profit"] if profit >= 0 else theme["loss"]
    profit_sign = "+" if profit >= 0 else ""
    draw.text((60, y_offset + 20), "P/L", fill=theme["text_secondary"], font=font_small)
    draw.text((60, y_offset + 50), f"{profit_sign}${profit:,.2f}", fill=profit_color, font=font_large)
    
    roi_text = f"{profit_sign}{roi:.2f}%"
    draw.text((60, y_offset + 120), roi_text, fill=profit_color, font=font_title)
    
    rank_x = width - 350
    draw.text((rank_x, y_offset + 20), leaderboard["rank"], fill=theme["accent"], font=font_small)
    draw.text((rank_x, y_offset + 50), leaderboard["win_rate"], fill=theme["text_secondary"], font=font_tiny)
    
    y_offset += 200
    
    stop_loss = entry_price * (0.95 if direction == "BUY" else 1.05)
    take_profit1 = entry_price * (1.10 if direction == "BUY" else 0.90)
    take_profit2 = entry_price * (1.15 if direction == "BUY" else 0.85)
    risk_reward = abs((take_profit1 - entry_price) / (entry_price - stop_loss))
    position_size_pct = random.uniform(1.5, 5.0)
    
    draw.rounded_rectangle((40, y_offset, width - 40, y_offset + 200), radius=15, fill=theme["card_bg"])
    
    rm_y = y_offset + 20
    draw.text((60, rm_y), f"🛡️ Stop Loss: ${stop_loss:,.2f}", fill=theme["loss"], font=font_small)
    draw.text((60, rm_y + 40), f"🎯 TP1: ${take_profit1:,.2f} | TP2: ${take_profit2:,.2f}", 
              fill=theme["profit"], font=font_small)
    draw.text((60, rm_y + 80), f"R:R {risk_reward:.1f}:1", fill=theme["accent"], font=font_small)
    draw.text((60, rm_y + 120), f"Position: {position_size_pct:.1f}% of portfolio", 
              fill=theme["text_secondary"], font=font_small)
    
    hold_duration = timedelta(hours=random.randint(1, 48), minutes=random.randint(0, 59))
    hours = int(hold_duration.total_seconds() // 3600)
    minutes = int((hold_duration.total_seconds() % 3600) // 60)
    draw.text((60, rm_y + 160), f"⏱️ Held for: {hours}h {minutes}m", fill=theme["text_secondary"], font=font_small)
    
    y_offset += 220
    
    if portfolio_value is None:
        portfolio_value = random.uniform(50000, 500000)
    
    position_value = deposit + profit
    
    draw.rounded_rectangle((40, y_offset, width - 40, y_offset + 120), radius=15, fill=theme["card_bg"])
    draw.text((60, y_offset + 20), "Portfolio Value", fill=theme["text_secondary"], font=font_small)
    draw.text((60, y_offset + 50), f"${portfolio_value:,.2f}", fill=theme["text"], font=font_title)
    draw.text((60, y_offset + 90), f"Position: ${position_value:,.2f} of portfolio", 
              fill=theme["text_secondary"], font=font_tiny)
    
    y_offset += 140
    
    draw.rounded_rectangle((40, y_offset, width - 40, y_offset + 220), radius=15, fill=theme["card_bg"])
    
    details = [
        ("Entry Price", f"${entry_price:,.6f}".rstrip('0').rstrip('.')),
        ("Exit Price", f"${exit_price:,.6f}".rstrip('0').rstrip('.')),
        ("Quantity", f"{quantity:.4f}".rstrip('0').rstrip('.')),
        ("Transaction ID", f"TX#{txid}"),
    ]
    
    detail_y = y_offset + 20
    for label, value in details:
        draw.text((60, detail_y), label, fill=theme["text_secondary"], font=font_tiny)
        draw.text((60, detail_y + 25), value, fill=theme["text"], font=font_small)
        detail_y += 55
    
    y_offset += 240
    
    # Add asset-specific information for special asset types
    if asset_type in ["option", "futures", "forex", "crypto_multi"]:
        y_offset = draw_asset_type_specific_info(draw, y_offset, width, asset_type, symbol, theme, font_small, font_tiny)
        y_offset += 20
    
    # Add interactive buttons and social elements
    y_offset = draw_interactive_buttons(draw, width, y_offset, theme, font_small)
    y_offset += 20
    
    # Add verification layer
    y_offset = draw_verification_layer(draw, width, y_offset, symbol, txid, theme, font_small, font_tiny)
    y_offset += 20
    
    sentiment_color = theme["profit"] if market_data["sentiment"] == "Bullish" else theme["loss"]
    volatility_colors = {"Low": theme["profit"], "Medium": theme["accent"], "High": theme["loss"], "Extreme": "#FF0000"}
    
    news_y = height - 170
    draw.rounded_rectangle((20, news_y, width - 20, news_y + 60), radius=10, fill=theme["card_bg"])
    draw.text((40, news_y + 12), f"📰 {market_data['news']}", fill=theme["text_secondary"], font=font_tiny)
    draw.text((40, news_y + 35), 
              f"Market: {market_data['sentiment']} {market_data['sentiment_value']}% | Volatility: {market_data['volatility']}", 
              fill=sentiment_color, font=font_tiny)
    
    nav_height = draw_bottom_nav_bar(draw, width, height, theme)
    
    mask = Image.new('L', (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, width, height), radius=40, fill=255)
    
    img_with_rounded = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    img_rgba = img.convert('RGBA')
    img_with_rounded.paste(img_rgba, (0, 0), mask)
    
    final_with_border = Image.new('RGB', (width + 60, height + 60), (30, 30, 35))
    
    shadow_img = Image.new('RGBA', (width + 60, height + 60), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    for i in range(10):
        alpha = 20 - i * 2
        shadow_draw.rounded_rectangle((20 - i, 20 - i, width + 40 + i, height + 40 + i), 
                                      radius=45, outline=(0, 0, 0, alpha), width=2)
    
    final_with_border.paste(shadow_img, (0, 0), shadow_img)
    final_with_border.paste(img_with_rounded, (30, 30), img_with_rounded)
    
    return final_with_border

def save_trade_image(img, txid):
    """Save trade image to file"""
    os.makedirs("trade_images", exist_ok=True)
    filename = f"trade_images/{txid}.png"
    img.save(filename, quality=95, optimize=True)
    return filename

def create_notification_style_screenshot(symbol, profit, roi, broker_name="Robinhood", device_type="ios"):
    """Create a push notification style screenshot"""
    theme = get_theme_for_broker(broker_name)
    
    width, height = 800, 200
    img = Image.new('RGB', (width, height), (240, 240, 245) if device_type == "ios" else (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    try:
        font_app = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        font_message = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        font_time = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        font_app = font_title = font_message = font_time = ImageFont.load_default()
    
    notif_bg = "#FFFFFF" if device_type == "ios" else "#F5F5F5"
    draw.rounded_rectangle((10, 10, width - 10, height - 10), radius=15, fill=notif_bg)
    
    if device_type == "ios":
        draw.rounded_rectangle((10, 10, width - 10, height - 10), radius=15, outline="#E0E0E0", width=1)
    
    draw.text((25, 20), broker_name.upper(), fill="#666666", font=font_app)
    
    current_time = datetime.now().strftime("%I:%M %p")
    time_bbox = draw.textbbox((0, 0), current_time, font=font_time)
    time_width = time_bbox[2] - time_bbox[0]
    draw.text((width - time_width - 25, 20), current_time, fill="#999999", font=font_time)
    
    profit_sign = "+" if profit >= 0 else ""
    profit_color = theme["profit"] if profit >= 0 else theme["loss"]
    
    title_text = f"Your {symbol} position {profit_sign}${profit:,.2f}"
    draw.text((25, 50), title_text, fill=profit_color, font=font_title)
    
    message_text = f"Return: {profit_sign}{roi:.2f}% • Tap to view details"
    draw.text((25, 80), message_text, fill="#333333", font=font_message)
    
    action_y = height - 50
    draw.text((25, action_y), "View", fill=theme["primary"], font=font_message)
    draw.text((100, action_y), "Close", fill="#999999", font=font_message)
    
    return img

def draw_annotations(img, annotations_list):
    """Add arrows and text bubbles to highlight key areas"""
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    try:
        font_annotation = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except:
        font_annotation = ImageFont.load_default()
    
    for annotation in annotations_list:
        ann_type = annotation.get("type", "arrow")
        x, y = annotation.get("position", (width//2, height//2))
        text = annotation.get("text", "")
        color = annotation.get("color", "#FFD700")
        
        if ann_type == "arrow":
            arrow_points = [
                (x, y),
                (x + 50, y - 30),
                (x + 45, y - 30),
                (x + 45, y - 60),
                (x + 55, y - 60),
                (x + 55, y - 30),
                (x + 50, y - 30)
            ]
            draw.polygon(arrow_points, fill=color + "CC")
            if text:
                draw.text((x + 70, y - 70), text, fill=color, font=font_annotation)
        
        elif ann_type == "bubble":
            bubble_width = 250
            bubble_height = 80
            draw.rounded_rectangle((x, y, x + bubble_width, y + bubble_height), 
                                  radius=15, fill=color + "DD", outline=color, width=3)
            draw.text((x + 15, y + 15), text, fill="#000000", font=font_annotation)
        
        elif ann_type == "highlight":
            box_width, box_height = annotation.get("size", (200, 100))
            draw.rounded_rectangle((x, y, x + box_width, y + box_height), 
                                  radius=10, outline=color, width=5)
    
    return img

def add_daily_pl_summary(draw, y_pos, width, total_daily_pl, theme, font_title, font_small):
    """Add total P/L for the day display"""
    draw.rounded_rectangle((40, y_pos, width - 40, y_pos + 120), radius=15, fill=theme["card_bg"])
    
    draw.text((60, y_pos + 15), "📅 Today's Performance", fill=theme["text"], font=font_title)
    
    pl_color = theme["profit"] if total_daily_pl >= 0 else theme["loss"]
    pl_sign = "+" if total_daily_pl >= 0 else ""
    
    draw.text((60, y_pos + 55), f"{pl_sign}${total_daily_pl:,.2f}", fill=pl_color, font=font_title)
    
    trades_count = random.randint(3, 15)
    win_rate = random.randint(60, 90)
    draw.text((60, y_pos + 90), f"{trades_count} trades • {win_rate}% win rate", 
              fill=theme["text_secondary"], font=font_small)
    
    return y_pos + 140

def create_professional_trade_image(*args, **kwargs):
    """Wrapper for compatibility - routes to ultra realistic version"""
    return create_ultra_realistic_mobile_trade_screenshot(*args, **kwargs)
