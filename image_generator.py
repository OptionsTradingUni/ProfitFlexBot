"""
Enhanced Image Generation Module for Profit Flex Bot
Creates professional, authentic-looking trade snapshots with broker UI styling
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
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
    Create a realistic candlestick/line chart showing price movement
    """
    fig, ax = plt.subplots(figsize=(width/100, height/100), facecolor='#0B0F19')
    ax.set_facecolor('#1C1F26')
    
    # Generate realistic price data
    num_points = 50
    if profit_positive:
        prices = np.linspace(entry_price, exit_price, num_points)
        noise = np.random.normal(0, (exit_price - entry_price) * 0.02, num_points)
    else:
        prices = np.linspace(entry_price, exit_price, num_points)
        noise = np.random.normal(0, abs(exit_price - entry_price) * 0.02, num_points)
    
    prices = prices + noise
    prices[0] = entry_price
    prices[-1] = exit_price
    
    # Plot price line
    color = '#00C805' if profit_positive else '#FF6058'
    ax.plot(prices, color=color, linewidth=2.5, alpha=0.9)
    ax.fill_between(range(len(prices)), prices, alpha=0.15, color=color)
    
    # Mark entry and exit points
    ax.scatter([0], [entry_price], color='#4C9AFF', s=100, zorder=5, edgecolors='white', linewidths=1.5)
    ax.scatter([num_points-1], [exit_price], color=color, s=100, zorder=5, edgecolors='white', linewidths=1.5)
    
    # Styling
    ax.grid(True, alpha=0.1, color='#FFFFFF', linestyle='--', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#8B92A6')
    ax.spines['bottom'].set_color('#8B92A6')
    ax.tick_params(colors='#8B92A6', labelsize=8)
    
    # Format y-axis for currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.2f}'))
    
    # Remove x-axis labels
    ax.set_xticks([])
    
    plt.tight_layout()
    
    # Convert to PIL Image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='#0B0F19', dpi=100)
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
    draw.rectangle([0, 0, width, header_height], fill=theme["card_bg"])
    draw.text((40, 45), broker_name, fill=theme["text"], font=font_title)
    
    # Status badge
    status_text = "FILLED"
    status_color = theme["profit"]
    draw.rounded_rectangle([width - 200, 35, width - 40, 85], radius=25, fill=status_color)
    draw.text((width - 170, 45), status_text, fill='#FFFFFF', font=font_small)
    
    y_offset = header_height + 40
    
    # Symbol and Direction Card
    card_y = y_offset
    draw.rounded_rectangle([40, card_y, width - 40, card_y + 180], radius=20, fill=theme["card_bg"])
    
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
    draw.rounded_rectangle([40, perf_card_y, width - 40, perf_card_y + 280], radius=20, fill=theme["card_bg"])
    
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
    draw.rounded_rectangle([40, details_y, width - 40, details_y + 420], radius=20, fill=theme["card_bg"])
    
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
    draw.rounded_rectangle([40, trader_y, width - 40, trader_y + 140], radius=20, fill=theme["card_bg"])
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
    
    # Add subtle noise for realism
    img = img.filter(ImageFilter.GaussianBlur(radius=0.3))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.05)
    
    return img

def save_trade_image(img, txid):
    """Save trade image to file"""
    os.makedirs("trade_images", exist_ok=True)
    filename = f"trade_images/{txid}.png"
    img.save(filename, quality=95, optimize=True)
    return filename
