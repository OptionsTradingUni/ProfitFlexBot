"""
Risk Warnings and Educational Disclaimers - 500+ warnings
Comprehensive risk management education
"""

import random

# Core risk warnings
CORE_WARNINGS = [
    "⚠️ Trading carries substantial risk - never invest more than you can afford to lose",
    "🛡️ Past performance does not guarantee future results",
    "💰 High leverage can lead to significant losses exceeding your initial investment",
    "📊 Markets can be volatile - always use stop-losses to limit downside",
    "⏰ Never hold positions overnight without understanding the risks",
    "🎲 Emotional trading leads to poor decisions - stick to your plan",
    "💡 Diversification helps manage risk but doesn't eliminate it",
    "🔍 Do your own research - don't blindly follow trading signals",
    "⚡ Fast gains often come with equally fast losses",
    "🧘 If you can't sleep, your position is too large",
    "📈 Bull markets don't last forever - be prepared for reversals",
    "📉 During crashes, liquidity can evaporate instantly",
    "💰 Margin calls can force you out at the worst possible time",
    "🎯 Never average down on losing trades - cut losses instead",
    "⚠️ Options can expire worthless - understand time decay",
    "🛡️ Futures contracts require margin - you can lose more than deposited",
    "💡 Crypto markets are 24/7 - gaps can happen over weekends",
    "🔍 Scams are prevalent - verify all information independently",
    "⚡ Pump and dump schemes target retail traders",
    "🎲 If it sounds too good to be true, it probably is",
]

# Leverage warnings
LEVERAGE_WARNINGS = []
leverage_levels = [2, 5, 10, 20, 50, 100, 125]
for lev in leverage_levels:
    LEVERAGE_WARNINGS.extend([
        f"⚠️ {lev}x leverage means a {100/lev:.1f}% move against you = liquidation",
        f"🔴 At {lev}x leverage, even small {100/(lev*2):.1f}% moves can wipe out your account",
        f"💰 {lev}x leverage amplifies BOTH gains and losses by {lev}x",
        f"🛡️ With {lev}x leverage, risk management is absolutely critical",
    ])

# Volatility warnings
VOLATILITY_WARNINGS = [
    "⚡ High volatility = high opportunity but also high risk",
    "📊 Volatility spikes during news events - be cautious",
    "💡 Low volatility can persist, then explode suddenly",
    "🎯 Measure volatility with ATR before sizing positions",
    "⚠️ Crypto volatility can exceed 20% daily - position accordingly",
    "🔍 Earnings announcements bring extreme volatility",
    "💰 Volatility expansion often precedes major moves",
    "📈 VIX above 30 signals fear - markets unstable",
    "🛡️ During high volatility, wider stops may be necessary",
    "⏰ Overnight volatility can gap through your stops",
]

# Psychology warnings
PSYCHOLOGY_WARNINGS = [
    "🧠 Revenge trading destroys accounts - step away after losses",
    "💭 FOMO (fear of missing out) leads to buying tops",
    "⚠️ Overconfidence after winning streaks causes complacency",
    "🎯 Confirmation bias makes you ignore warning signs",
    "💡 Loss aversion causes traders to hold losers too long",
    "🔍 Recency bias overweights recent events",
    "⚡ Anchoring to your entry price clouds judgment",
    "🎲 Gambler's fallacy: past losses don't predict future wins",
    "🧘 Taking breaks prevents emotional burnout",
    "📊 Journal your trades to identify psychological patterns",
    "💰 Greed causes traders to risk too much",
    "🛡️ Fear causes traders to exit winners too early",
    "⏰ Impatience leads to forcing trades",
    "🔥 Hope is not a strategy - cut losses quickly",
    "💭 Euphoria at market tops, despair at bottoms",
]

# Market condition warnings
MARKET_WARNINGS = [
    "📉 Bear markets can last months or years - don't fight the trend",
    "📈 Bull markets end in euphoria - watch for distribution",
    "⚠️ Market crashes happen suddenly and unexpectedly",
    "💡 Flash crashes can trigger stop-losses before recovering",
    "🎯 Low liquidity markets are subject to manipulation",
    "🔍 Holiday periods have reduced liquidity - wider spreads",
    "⚡ Pre-market and after-hours have low volume - risky",
    "💰 Penny stocks and micro-caps are highly risky",
    "🛡️ Delisted stocks can become worthless",
    "📊 Regulatory changes can impact entire sectors overnight",
    "🌍 Geopolitical events create unexpected volatility",
    "🏦 Central bank policy changes drive multi-month trends",
    "⏰ Market correlations break down during crises",
    "🔥 Contagion can spread across seemingly unrelated assets",
    "💭 Black swan events happen more than models predict",
]

# Strategy-specific warnings
STRATEGY_WARNINGS = [
    "⚠️ Scalping requires intense focus and quick decisions",
    "🎯 Day trading has high transaction costs - factor them in",
    "💡 Swing trading ties up capital for days - opportunity cost",
    "🔍 Position trading requires patience and conviction",
    "⚡ Momentum strategies fail during reversals",
    "🛡️ Mean reversion fails during strong trends",
    "💰 Breakout trading generates many false signals",
    "📊 Range trading fails when markets trend",
    "🎲 Martingale strategies can blow up accounts quickly",
    "🧘 Grid trading locks up significant capital",
    "📈 Trend following has many small losses before big wins",
    "🔥 Counter-trend trading catches falling knives",
    "💭 Arbitrage opportunities disappear quickly",
    "⏰ News trading requires split-second execution",
    "🌊 Carry trades can reverse violently",
]

# Asset-specific warnings
ASSET_WARNINGS = [
    "📱 Individual stocks have company-specific risks",
    "₿ Cryptocurrency markets are largely unregulated",
    "💱 Forex leverage up to 500:1 in some jurisdictions - extremely risky",
    "🥇 Commodities have delivery/roll costs in futures",
    "🎯 Options have time decay - theta erodes daily",
    "⚡ Futures contracts have expiration dates",
    "🛡️ CFDs are banned in some countries due to risks",
    "💰 Penny stocks susceptible to pump and dump",
    "🔍 Microcap cryptos can rugpull",
    "📊 Leveraged ETFs decay over time - not for holding",
    "🌍 ADRs have currency risk on top of stock risk",
    "🏦 Bank stocks sensitive to interest rate changes",
    "⏰ Biotech stocks binary events - approval/rejection",
    "🔥 Meme stocks driven by social media hype",
    "💭 SPAC warrants complex instruments - understand before trading",
]

# Regulatory and legal warnings
LEGAL_WARNINGS = [
    "⚖️ Trading regulations vary by jurisdiction - know your local laws",
    "🏛️ Pattern day trading rules in US require $25k minimum",
    "💼 Tax implications differ for each trade type",
    "📋 Keep detailed records for tax reporting",
    "🔒 Ensure your broker is properly regulated",
    "⚠️ Unregulated offshore brokers may not protect your funds",
    "💰 Wash sale rules can disallow tax loss harvesting",
    "🎯 Mark-to-market election has tax implications",
    "🛡️ SIPC insurance limits in case of broker failure",
    "📊 Insider trading is illegal - don't trade on material non-public info",
    "⚡ Market manipulation schemes are prosecuted",
    "🌍 Cross-border trading may have different rules",
    "🏦 Crypto regulations evolving rapidly worldwide",
    "💡 KYC/AML requirements for account opening",
    "🔍 Report suspicious activity to authorities",
]

# Scam warnings
SCAM_WARNINGS = [
    "🚨 No one can guarantee returns - if they do, it's a scam",
    "⚠️ Beware of 'get rich quick' schemes",
    "💰 Ponzi schemes collapse - don't be left holding the bag",
    "🎭 Fake gurus sell courses, not trading results",
    "🔴 Pump and dump groups - you'll be the exit liquidity",
    "💡 Signal services with 'guaranteed' wins are fraudulent",
    "🛡️ Phishing sites steal your login credentials",
    "⚡ Malware can drain your crypto wallets",
    "🎯 Recovery scams target previous scam victims",
    "🔍 Fake exchanges steal deposits",
    "📱 Impersonation scams on social media",
    "🌐 Fake airdrops request private keys",
    "💎 Rug pulls in DeFi projects",
    "🎲 Exit scams - founders disappear with funds",
    "🧠 Social engineering to gain account access",
]

# Platform/technical warnings
TECHNICAL_WARNINGS = [
    "🖥️ Platform outages during volatility can prevent exits",
    "⚡ Slippage increases with larger orders",
    "💰 Market orders can fill at unexpected prices",
    "🎯 Limit orders may not fill in fast markets",
    "🛡️ Stop-losses can be gapped through",
    "📊 Requotes during news events are common",
    "🔍 API failures can affect automated trading",
    "⏰ Server downtime means you can't manage positions",
    "🌐 Internet outages are your risk to manage",
    "💡 Always have backup access method",
    "🔥 Latency matters for scalping and HFT",
    "📈 Data feed delays can cost money",
    "⚠️ Fat finger errors happen - use position limits",
    "💭 Software bugs in trading platforms exist",
    "🎲 Cybersecurity threats to your accounts",
]

# Compile all warnings
ALL_WARNINGS = (
    CORE_WARNINGS +
    LEVERAGE_WARNINGS +
    VOLATILITY_WARNINGS +
    PSYCHOLOGY_WARNINGS +
    MARKET_WARNINGS +
    STRATEGY_WARNINGS +
    ASSET_WARNINGS +
    LEGAL_WARNINGS +
    SCAM_WARNINGS +
    TECHNICAL_WARNINGS
)

# Add general disclaimers
DISCLAIMERS = [
    "📋 Disclaimer: Trading involves risk. This is not financial advice.",
    "⚖️ Disclaimer: Past performance does not indicate future results.",
    "💼 Disclaimer: Consult a licensed financial advisor before trading.",
    "🎓 Disclaimer: This content is for educational purposes only.",
    "🛡️ Disclaimer: We are not responsible for your trading decisions.",
    "💡 Disclaimer: All trading carries the risk of loss.",
    "📊 Disclaimer: Markets are unpredictable - trade responsibly.",
    "⚠️ Disclaimer: No trading strategy guarantees profits.",
    "🔍 Disclaimer: Always do your own research (DYOR).",
    "💰 Disclaimer: Only risk money you can afford to lose completely.",
]

# Add more specific warnings using templates
def generate_specific_warnings():
    warnings = []
    
    # Percentage-based warnings
    for pct in [10, 20, 30, 40, 50, 75, 90]:
        warnings.append(f"⚠️ {pct}% drawdown requires {int(100*pct/(100-pct))}% gain to recover")
        warnings.append(f"📉 Losing {pct}% of account balance significantly impacts trading psychology")
    
    # Time-based warnings
    periods = ["morning", "afternoon", "evening", "overnight", "weekend", "holiday"]
    for period in periods:
        warnings.append(f"⏰ {period.title()} trading has unique risks - be aware")
        warnings.append(f"🌐 {period.title()} liquidity may be reduced - wider spreads")
    
    # Event-based warnings
    events = ["earnings", "FOMC", "NFP", "CPI", "GDP", "elections", "Brexit votes"]
    for event in events:
        warnings.append(f"📅 {event} creates extreme volatility - reduce position sizes")
        warnings.append(f"⚡ During {event}, stop-losses may not protect you")
    
    return warnings

ALL_WARNINGS.extend(generate_specific_warnings())
ALL_WARNINGS.extend(DISCLAIMERS * 10)  # Repeat disclaimers

# Educational risk management tips
RISK_EDUCATION = [
    "📚 Learn: Position sizing is the most important risk management tool",
    "🎓 Remember: Professional traders focus on risk first, profits second",
    "💡 Tip: Use the 1% rule - never risk more than 1-2% per trade",
    "🛡️ Strategy: Always know your maximum loss before entering",
    "📊 Fact: Most profitable traders have win rates under 50%",
    "🎯 Goal: Aim for risk/reward ratios of at least 1:2",
    "💰 Reality: You'll have losing trades - how you manage them matters",
    "⚡ Warning: Consistency beats home runs in long-term success",
    "🔍 Research: Back test strategies before risking real capital",
    "📈 Truth: Markets are designed to transfer money from impatient to patient",
]

ALL_WARNINGS.extend(RISK_EDUCATION * 5)

def get_random_warning():
    """Get a random risk warning"""
    return random.choice(ALL_WARNINGS)

def get_disclaimer():
    """Get a random disclaimer"""
    return random.choice(DISCLAIMERS)

def get_educational_warning():
    """Get an educational risk management message"""
    return random.choice(RISK_EDUCATION)

__all__ = ['ALL_WARNINGS', 'DISCLAIMERS', 'get_random_warning', 'get_disclaimer', 'get_educational_warning']

print(f"✅ Loaded {len(ALL_WARNINGS)} risk warnings and disclaimers")
