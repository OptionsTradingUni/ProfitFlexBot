"""
Enhanced Image Generation Module for Profit Flex Bot
Creates professional, authentic-looking trade snapshots with broker UI styling
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
from datetime import datetime
import os

# Professional color schemes by broker type
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
    "charles_schwab": {
        "bg": "#00263E",
        "card_bg": "#003B5C",
        "primary": "#00A3E0",
        "accent": "#F7941D",
        "text": "#FFFFFF",
        "text_secondary": "#A0C5D9",
        "profit": "#00D084",
        "loss": "#EE4B2B"
    },
    "fidelity": {
        "bg": "#003B49",
        "card_bg": "#00506A",
        "primary": "#78BE20",
        "accent": "#FF6F00",
        "text": "#FFFFFF",
        "text_secondary": "#B0D5E3",
        "profit": "#00D676",
        "loss": "#FF4136"
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
    }
}

def get_theme_for_broker(broker_name):
    """Map broker name to theme"""
    broker_lower = broker_name.lower().replace(" ", "_").replace("*", "")
    
    if "robinhood" in broker_lower:
        return BROKER_THEMES["robinhood"]
    elif "webull" in broker_lower:
        return BROKER_THEMES["webull"]
    elif "schwab" in broker_lower or "charles" in broker_lower:
        return BROKER_THEMES["charles_schwab"]
    elif "fidelity" in broker_lower:
        return BROKER_THEMES["fidelity"]
    elif "binance" in broker_lower:
        return BROKER_THEMES["binance"]
    elif "coinbase" in broker_lower:
        return BROKER_THEMES["coinbase"]
    else:
        return BROKER_THEMES["robinhood"]

def create_price_chart(symbol, entry_price, exit_price, profit_positive=True, width=800, height=300):
    """
    Create a highly realistic candlestick chart with volume bars showing authentic price movement
    """
    fig = plt.figure(figsize=(width/100, height/100), facecolor='#0B0F19')
    
    # Create grid for candlestick and volume
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], hspace=0.05)
    ax_price = fig.add_subplot(gs[0])
    ax_volume = fig.add_subplot(gs[1], sharex=ax_price)
    
    ax_price.set_facecolor('#1C1F26')
    ax_volume.set_facecolor('#1C1F26')
    
    # Generate realistic price data with candlesticks
    num_candles = 40
    trend = 1 if profit_positive else -1
    
    # Create realistic OHLC data
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []
    
    current_price = entry_price
    volatility = abs(exit_price - entry_price) / num_candles * 0.5
    
    for i in range(num_candles):
        # Calculate target price for this candle
        target_progress = (i + 1) / num_candles
        target_price = entry_price + (exit_price - entry_price) * target_progress
        
        # Add realistic movement towards target
        price_change = (target_price - current_price) * 0.3 + random.uniform(-volatility, volatility)
        
        open_price = current_price
        close_price = current_price + price_change
        
        # Create realistic high/low with wicks
        high_price = max(open_price, close_price) + random.uniform(0, volatility * 0.5)
        low_price = min(open_price, close_price) - random.uniform(0, volatility * 0.5)
        
        opens.append(open_price)
        closes.append(close_price)
        highs.append(high_price)
        lows.append(low_price)
        volumes.append(random.uniform(10000, 50000))
        
        current_price = close_price
    
    # Ensure last candle ends at exit_price
    closes[-1] = exit_price
    if opens[-1] < closes[-1]:
        highs[-1] = max(highs[-1], exit_price + volatility * 0.2)
    else:
        lows[-1] = min(lows[-1], exit_price - volatility * 0.2)
    
    # Plot candlesticks
    color = '#00C805' if profit_positive else '#FF6058'
    for i in range(num_candles):
        candle_color = '#00C805' if closes[i] >= opens[i] else '#FF6058'
        
        # Draw wick (high-low line)
        ax_price.plot([i, i], [lows[i], highs[i]], color=candle_color, linewidth=1, alpha=0.8)
        
        # Draw candle body
        body_height = abs(closes[i] - opens[i])
        body_bottom = min(opens[i], closes[i])
        
        rect = Rectangle((i - 0.4, body_bottom), 0.8, body_height, 
                         facecolor=candle_color, edgecolor=candle_color, alpha=0.9, linewidth=0)
        ax_price.add_patch(rect)
    
    # Add moving average line for authenticity
    ma_period = 10
    if len(closes) >= ma_period:
        ma = np.convolve(closes, np.ones(ma_period)/ma_period, mode='valid')
        ma_x = range(ma_period-1, len(closes))
        ax_price.plot(ma_x, ma, color='#FFB84D', linewidth=1.5, alpha=0.6, linestyle='--', label='MA')
    
    # Plot volume bars
    for i in range(num_candles):
        volume_color = '#00C80540' if closes[i] >= opens[i] else '#FF605840'
        ax_volume.bar(i, volumes[i], color=volume_color, width=0.8, edgecolor='none')
    
    # Styling for price chart
    ax_price.grid(True, alpha=0.08, color='#FFFFFF', linestyle=':', linewidth=0.5)
    ax_price.spines['top'].set_visible(False)
    ax_price.spines['right'].set_visible(False)
    ax_price.spines['left'].set_color('#8B92A6')
    ax_price.spines['bottom'].set_color('#8B92A6')
    ax_price.tick_params(colors='#8B92A6', labelsize=7)
    ax_price.yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'${x:,.2f}'))
    ax_price.set_xticks([])
    
    # Styling for volume chart
    ax_volume.spines['top'].set_visible(False)
    ax_volume.spines['right'].set_visible(False)
    ax_volume.spines['left'].set_color('#8B92A6')
    ax_volume.spines['bottom'].set_color('#8B92A6')
    ax_volume.tick_params(colors='#8B92A6', labelsize=6)
    ax_volume.yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
    ax_volume.set_xticks([])
    ax_volume.set_ylabel('Volume', color='#8B92A6', fontsize=7)
    ax_volume.grid(True, alpha=0.05, color='#FFFFFF', linestyle=':', linewidth=0.5)
    
    plt.tight_layout()
    
    # Convert to PIL Image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='#0B0F19', dpi=120, bbox_inches='tight')
    buf.seek(0)
    chart_img = Image.open(buf)
    plt.close(fig)
    
    return chart_img

def create_professional_trade_image(
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
    timestamp=None
):
    """
    Generate a highly authentic broker-style trade confirmation image
    """
    
    # Get theme
    theme = get_theme_for_broker(broker_name)
    
    # Create base canvas
    width, height = 1080, 1920
    img = Image.new('RGB', (width, height), theme["bg"])
    draw = ImageDraw.Draw(img)
    
    # Try to load professional fonts, fallback to default
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font_title = ImageFont.load_default()
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_tiny = ImageFont.load_default()
    
    y_offset = 40
    
    # Header with broker branding
    header_height = 120
    draw.rectangle((0, 0, width, header_height), fill=theme["card_bg"])
    draw.text((40, 45), broker_name, fill=theme["text"], font=font_title)
    
    # Status badge
    status_text = "FILLED"
    status_color = theme["profit"]
    draw.rounded_rectangle((width - 200, 35, width - 40, 85), radius=25, fill=status_color)
    draw.text((width - 170, 45), status_text, fill='#FFFFFF', font=font_small)
    
    y_offset = header_height + 40
    
    # Symbol and Direction Card
    card_y = y_offset
    draw.rounded_rectangle((40, card_y, width - 40, card_y + 180), radius=20, fill=theme["card_bg"])
    
    draw.text((60, card_y + 30), symbol, fill=theme["primary"], font=font_large)
    direction_color = theme["profit"] if direction == "BUY" else theme["loss"]
    draw.text((60, card_y + 110), f"{direction} • {quantity:.6f}".rstrip('0').rstrip('.'), 
              fill=direction_color, font=font_medium)
    
    y_offset = card_y + 220
    
    # Price Chart
    profit_positive = profit >= 0
    chart = create_price_chart(symbol, entry_price, exit_price, profit_positive, 1000, 400)
    chart = chart.resize((width - 80, 400))
    img.paste(chart, (40, y_offset))
    
    y_offset += 440
    
    # Performance Card
    perf_card_y = y_offset
    draw.rounded_rectangle((40, perf_card_y, width - 40, perf_card_y + 280), radius=20, fill=theme["card_bg"])
    
    # Profit/Loss
    profit_color = theme["profit"] if profit >= 0 else theme["loss"]
    profit_sign = "+" if profit >= 0 else ""
    draw.text((60, perf_card_y + 30), "Profit / Loss", fill=theme["text_secondary"], font=font_small)
    draw.text((60, perf_card_y + 75), f"{profit_sign}${profit:,.2f}", fill=profit_color, font=font_large)
    
    # ROI
    roi_sign = "+" if roi >= 0 else ""
    draw.text((60, perf_card_y + 165), "Return", fill=theme["text_secondary"], font=font_small)
    draw.text((60, perf_card_y + 205), f"{roi_sign}{roi:.2f}%", fill=profit_color, font=font_medium)
    
    y_offset = perf_card_y + 320
    
    # Execution Details Card
    details_y = y_offset
    draw.rounded_rectangle((40, details_y, width - 40, details_y + 420), radius=20, fill=theme["card_bg"])
    
    details = [
        ("Entry Price", f"${entry_price:,.8f}".rstrip('0').rstrip('.')),
        ("Exit Price", f"${exit_price:,.8f}".rstrip('0').rstrip('.')),
        ("Quantity", f"{quantity:.6f}".rstrip('0').rstrip('.')),
        ("Total Invested", f"${deposit:,.2f}"),
        ("Transaction ID", f"TX#{txid}"),
    ]
    
    detail_y = details_y + 30
    for label, value in details:
        draw.text((60, detail_y), label, fill=theme["text_secondary"], font=font_small)
        draw.text((60, detail_y + 40), value, fill=theme["text"], font=font_medium)
        detail_y += 85
    
    y_offset = details_y + 460
    
    # Trader Info Card
    trader_y = y_offset
    draw.rounded_rectangle((40, trader_y, width - 40, trader_y + 140), radius=20, fill=theme["card_bg"])
    draw.text((60, trader_y + 30), "Trader", fill=theme["text_secondary"], font=font_small)
    draw.text((60, trader_y + 70), trader_name, fill=theme["text"], font=font_medium)
    
    y_offset = trader_y + 180
    
    # Timestamp and verification
    if timestamp:
        time_str = timestamp.strftime("%b %d, %Y • %I:%M %p UTC")
    else:
        time_str = datetime.utcnow().strftime("%b %d, %Y • %I:%M %p UTC")
    
    draw.text((40, y_offset), time_str, fill=theme["text_secondary"], font=font_tiny)
    draw.text((40, y_offset + 40), "✓ Verified & Encrypted", fill=theme["primary"], font=font_tiny)
    
    # Add security badge at bottom right
    badge_y = y_offset
    badge_w = 180
    badge_h = 70
    badge_x = width - badge_w - 40
    
    # Draw security badge background with glow effect
    for offset in range(3, 0, -1):
        alpha = 30 - (offset * 8)
        glow_color = theme["primary"] + format(alpha, '02x')
        draw.rounded_rectangle(
            (badge_x - offset, badge_y - offset, badge_x + badge_w + offset, badge_y + badge_h + offset),
            radius=15, fill=None, outline=glow_color, width=2
        )
    
    draw.rounded_rectangle((badge_x, badge_y, badge_x + badge_w, badge_y + badge_h), 
                          radius=12, fill=theme["card_bg"], outline=theme["primary"], width=2)
    
    # Add security icons and text
    draw.text((badge_x + 15, badge_y + 12), "🔒 SECURE", fill=theme["primary"], font=font_tiny)
    draw.text((badge_x + 15, badge_y + 40), "SSL Encrypted", fill=theme["text_secondary"], font=font_tiny)
    
    # Add watermark in center
    watermark_text = "AUTHENTICATED TRADE"
    watermark = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    
    try:
        watermark_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    except:
        watermark_font = font_large
    
    # Get watermark text size
    bbox = watermark_draw.textbbox((0, 0), watermark_text, font=watermark_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Position watermark diagonally across image
    watermark_draw.text(
        ((width - text_width) / 2, height / 2 - 200),
        watermark_text,
        fill=(255, 255, 255, 15),
        font=watermark_font
    )
    
    # Composite watermark
    img = Image.alpha_composite(img.convert('RGBA'), watermark).convert('RGB')
    
    # Add professional corner stamp
    stamp_size = 100
    stamp_x = width - stamp_size - 50
    stamp_y = 50
    
    # Draw circular stamp
    stamp_overlay = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    stamp_draw = ImageDraw.Draw(stamp_overlay)
    
    # Outer circle with glow
    for r in range(3):
        circle_alpha = 40 - (r * 10)
        circle_color = tuple(list(int(theme["accent"][i:i+2], 16) for i in (1, 3, 5)) + [circle_alpha])
        stamp_draw.ellipse(
            (stamp_x - r*2, stamp_y - r*2, stamp_x + stamp_size + r*2, stamp_y + stamp_size + r*2),
            outline=circle_color, width=2
        )
    
    stamp_draw.ellipse(
        (stamp_x, stamp_y, stamp_x + stamp_size, stamp_y + stamp_size),
        outline=theme["accent"], width=3
    )
    
    # Inner stamp details
    try:
        stamp_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        stamp_font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except:
        stamp_font = font_small
        stamp_font_small = font_tiny
    
    stamp_center_x = stamp_x + stamp_size // 2
    stamp_center_y = stamp_y + stamp_size // 2
    
    stamp_draw.text((stamp_center_x - 35, stamp_center_y - 15), "VERIFIED", fill=theme["accent"], font=stamp_font)
    stamp_draw.text((stamp_center_x - 25, stamp_center_y + 5), "TRADE", fill=theme["text"], font=stamp_font_small)
    
    img = Image.alpha_composite(img.convert('RGBA'), stamp_overlay).convert('RGB')
    
    # Add gradient overlay at top for depth
    gradient = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    gradient_draw = ImageDraw.Draw(gradient)
    
    for i in range(150):
        alpha = int((150 - i) / 150 * 30)
        gradient_draw.rectangle(
            (0, i, width, i+1),
            fill=(0, 0, 0, alpha)
        )
    
    img = Image.alpha_composite(img.convert('RGBA'), gradient).convert('RGB')
    
    # Add subtle noise for realism and texture
    img = img.filter(ImageFilter.GaussianBlur(radius=0.2))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.08)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.15)
    
    return img

def save_trade_image(img, txid):
    """Save trade image to file"""
    os.makedirs("trade_images", exist_ok=True)
    filename = f"trade_images/{txid}.png"
    img.save(filename, quality=95, optimize=True)
    return filename
