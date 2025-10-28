import random
from datetime import datetime, timezone

EDUCATIONAL_TIPS = [
    "📖 **Trading Tip:** Always set stop losses to protect your capital. Risk management is key to long-term success.",
    "📖 **Pro Strategy:** The best traders cut losses quickly and let winners run. Don't get emotionally attached to losing positions.",
    "📖 **Market Wisdom:** Volume confirms price action. High volume on breakouts = stronger moves.",
    "📖 **Risk Management:** Never risk more than 2-3% of your portfolio on a single trade. Preserve capital first.",
    "📖 **Technical Analysis:** Support becomes resistance and resistance becomes support after a breakout.",
    "📖 **Trading Psychology:** Fear and greed are your biggest enemies. Stick to your trading plan.",
    "📖 **Options Strategy:** Time decay works against you with long options. Plan your exits accordingly.",
    "📖 **Day Trading Rule:** The first hour and last hour are typically the most volatile. Trade carefully.",
    "📖 **Chart Patterns:** Higher lows + higher highs = uptrend. Lower highs + lower lows = downtrend.",
    "📖 **Crypto Insight:** Bitcoin often leads altcoin movements. Watch BTC dominance for trend reversals.",
    "📖 **Position Sizing:** Scale into winners gradually. Don't go all-in on the first entry.",
    "📖 **Market Correlation:** SPY and QQQ often move together. Divergences can signal market shifts.",
    "📖 **Momentum Trading:** Trade in the direction of the trend. 'The trend is your friend.'",
    "📖 **Profit Taking:** Take partial profits on the way up. Nobody went broke taking profits.",
    "📖 **Scanner Strategy:** Look for unusual volume spikes. Big money moves create opportunities."
]

SUCCESS_STORIES = [
    {
        "name": "Marcus T.",
        "initial": 750,
        "profit": 8420,
        "timeframe": "3 weeks",
        "quote": "These signals changed my trading completely. Finally seeing consistent profits!"
    },
    {
        "name": "Sarah K.",
        "initial": 1200,
        "profit": 15650,
        "timeframe": "2 months",
        "quote": "I was skeptical at first but the results speak for themselves. Worth every penny."
    },
    {
        "name": "David R.",
        "initial": 500,
        "profit": 4280,
        "timeframe": "4 weeks",
        "quote": "Best trading community I've ever joined. The analysis is spot on!"
    },
    {
        "name": "Jennifer L.",
        "initial": 2000,
        "profit": 24500,
        "timeframe": "6 weeks",
        "quote": "My portfolio has never looked better. These trades are incredibly accurate."
    },
    {
        "name": "Alex M.",
        "initial": 850,
        "profit": 6730,
        "timeframe": "3 weeks",
        "quote": "Finally quit my day job thanks to these signals. Life changing!"
    },
    {
        "name": "Taylor B.",
        "initial": 1500,
        "profit": 12800,
        "timeframe": "5 weeks",
        "quote": "The win rate is insane. I've never been this confident in my trading."
    },
    {
        "name": "Chris P.",
        "initial": 600,
        "profit": 5120,
        "timeframe": "2 weeks",
        "quote": "Paid for itself in the first week. Absolute game changer!"
    },
    {
        "name": "Michelle W.",
        "initial": 3000,
        "profit": 31200,
        "timeframe": "8 weeks",
        "quote": "From break-even trader to consistently profitable. Thank you!"
    }
]

SOCIAL_PROOF_TEMPLATES = [
    "👥 **{count} traders** are watching this setup live right now",
    "🔥 **{count} members** joined in the last hour",
    "📊 **{count} people** are copying this trade",
    "⚡ **{count} notifications** sent in the last 5 minutes",
    "🎯 **{count} traders** hit their profit targets today",
    "💰 Community made **${amount:,}** in total profits this week",
    "📈 **{percent}%** of members are profitable this month",
    "🏆 Top trader this week: **+{percent}%** returns",
    "🚀 **{count} consecutive wins** by top performer today",
    "💎 VIP members accessed **{count} exclusive signals** this week"
]

HOT_ALERTS = [
    "🚨 **BREAKING:** High-probability setup detected on {symbol}",
    "⚡ **URGENT:** Major support level tested on {symbol} - Watch closely!",
    "🔥 **ALERT:** Unusual volume spike detected - {symbol} moving!",
    "💎 **OPPORTUNITY:** Golden crossover forming on {symbol}",
    "🎯 **SETUP:** Perfect risk/reward ratio developing on {symbol}",
    "⚠️ **WATCH:** {symbol} approaching key resistance level",
    "🚀 **MOMENTUM:** {symbol} breaking out with strong volume",
    "📊 **PATTERN:** Bullish flag formation confirmed on {symbol}"
]

VIP_TEASERS = [
    "💎 **VIP EXCLUSIVE:** Premium members got this signal 15 minutes early",
    "🔒 **VIP ALERT:** Advanced scanner detected this before the breakout",
    "⭐ **PREMIUM FEATURE:** VIP members received detailed entry/exit levels",
    "💼 **VIP BENEFIT:** Exclusive risk management guidance provided",
    "🎯 **ELITE ACCESS:** VIP traders got the full technical breakdown",
    "👑 **PREMIUM EDGE:** VIP members alerted at optimal entry price",
    "💎 **VIP SIGNAL:** This trade posted to premium channel first",
    "🔐 **EXCLUSIVE:** VIP members received live chart analysis"
]


def get_educational_tip():
    """Get a random educational trading tip"""
    tip = random.choice(EDUCATIONAL_TIPS)
    disclaimer = get_disclaimer()
    return f"{tip}\n\n{disclaimer}"


def get_success_story():
    """Generate a member success story post"""
    story = random.choice(SUCCESS_STORIES)
    
    roi = ((story['profit'] - story['initial']) / story['initial']) * 100
    
    message = f"""💬 **Member Success Story**

👤 {story['name']} started with ${story['initial']:,}
💰 Now at ${story['profit']:,} (+{roi:.0f}%)
⏱️ Time: {story['timeframe']}

"{story['quote']}"

📊 Results like these are why our community keeps growing!
⚠️ Past performance doesn't guarantee future results. Trade responsibly.
"""
    return message


def get_social_proof():
    """Get a random social proof message"""
    template = random.choice(SOCIAL_PROOF_TEMPLATES)
    
    count = random.randint(50, 500)
    amount = random.randint(50000, 500000)
    percent = random.randint(70, 95)
    
    return template.format(count=count, amount=amount, percent=percent)


def get_hot_alert(symbol):
    """Get a hot opportunity alert for a symbol"""
    alert = random.choice(HOT_ALERTS)
    return alert.format(symbol=symbol)


def get_vip_teaser():
    """Get a VIP membership teaser"""
    return random.choice(VIP_TEASERS)


def generate_daily_recap(stats):
    """Generate daily trading recap"""
    total_trades = stats.get('total_trades', 0)
    total_profit = stats.get('total_profit', 0)
    win_rate = stats.get('win_rate', 0)
    best_trade = stats.get('best_trade', 0)
    
    message = f"""📊 **Daily Trading Recap** - {datetime.now().strftime('%B %d, %Y')}

📈 **Trades Today:** {total_trades}
💰 **Total Profit:** ${total_profit:,.2f}
✅ **Win Rate:** {win_rate:.1f}%
🏆 **Best Trade:** +${best_trade:,.2f}

Another profitable day for the community! 🚀
"""
    disclaimer = get_disclaimer()
    return f"{message}\n{disclaimer}"


def generate_weekly_recap(stats):
    """Generate weekly trading recap"""
    total_trades = stats.get('total_trades', 0)
    total_profit = stats.get('total_profit', 0)
    win_rate = stats.get('win_rate', 0)
    avg_profit = total_profit / total_trades if total_trades > 0 else 0
    
    message = f"""📊 **Weekly Performance Summary**

This week our community achieved:

📈 **Total Trades:** {total_trades}
💰 **Combined Profit:** ${total_profit:,.2f}
✅ **Win Rate:** {win_rate:.1f}%
📊 **Avg Profit/Trade:** ${avg_profit:,.2f}

The momentum continues! Ready for next week? 🚀
"""
    disclaimer = get_disclaimer()
    return f"{message}\n{disclaimer}"


def generate_trader_of_week(trader_stats):
    """Generate Trader of the Week post"""
    name = trader_stats.get('name', 'Anonymous Trader')
    trades = trader_stats.get('trades', 0)
    profit = trader_stats.get('profit', 0)
    win_rate = trader_stats.get('win_rate', 0)
    streak = trader_stats.get('streak', 0)
    
    message = f"""🏆 **TRADER OF THE WEEK** 🏆

Congratulations to: **{name}**

📊 **Stats This Week:**
• Trades Executed: {trades}
• Total Profit: ${profit:,.2f}
• Win Rate: {win_rate:.0f}%
• Current Streak: {streak} wins

Outstanding performance! 👏

Want to be featured next week? Keep crushing it! 💪
"""
    disclaimer = get_disclaimer()
    return f"{message}\n{disclaimer}"


def get_disclaimer():
    """Get compliance disclaimer for posts"""
    disclaimers = [
        "⚠️ Educational content only. Not financial advice. Trade at your own risk.",
        "📚 For educational purposes. Past performance doesn't guarantee future results.",
        "⚠️ Risk disclaimer: Trading involves risk. Never invest more than you can afford to lose.",
        "📖 Educational analysis only. Do your own research before trading.",
    ]
    return random.choice(disclaimers)
